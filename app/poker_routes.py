from flask import Blueprint, request, jsonify
from app.prisma import with_prisma
from app.jwt import require_auth
from app.poker import Deck, Card, Rank, Suit, evaluate_hand, compare_hands
import json

poker_bp = Blueprint("poker_bp", __name__)

@poker_bp.route("/create-game", methods=["POST"])
@with_prisma
@require_auth
async def create_game(_jwt, prisma):
    data = request.get_json()
    name = data.get("name", "Poker Game")
    max_players = data.get("max_players", 6)
    small_blind = data.get("small_blind", 10)
    big_blind = data.get("big_blind", 20)

    game = await prisma.game.create(data={
        "name": name,
        "max_players": max_players,
        "small_blind": small_blind,
        "big_blind": big_blind,
        "players": {
            "create": {
                "player_id": _jwt["id"],
                "position": 0
            }
        }
    })

    return jsonify(game.model_dump())

@poker_bp.route("/join-game/<game_id>", methods=["POST"])
@with_prisma
@require_auth
async def join_game(game_id, _jwt, prisma):
    game = await prisma.game.find_unique(
        where={"id": game_id},
        include={"players": True}
    )
    if not game:
        return jsonify({"custom": True, "_message": "Game not found"}), 404
    if game.status != "WAITING":
        return jsonify({"custom": True, "_message": "Game already started"}), 400
    if len(game.players) >= game.max_players:
        return jsonify({"custom": True, "_message": "Game full"}), 400
    if any(p.player_id == _jwt["id"] for p in game.players):
        return jsonify({"custom": True, "_message": "Already in game"}), 400

    position = len(game.players)
    player_in_game = await prisma.playerInGame.create(data={
        "game_id": game_id,
        "player_id": _jwt["id"],
        "position": position
    })

    return jsonify(player_in_game.model_dump())

@poker_bp.route("/start-game/<game_id>", methods=["POST"])
@with_prisma
@require_auth
async def start_game(game_id, _jwt, prisma):
    game = await prisma.game.find_unique(
        where={"id": game_id},
        include={"players": True}
    )
    if not game:
        return jsonify({"custom": True, "_message": "Game not found"}), 404
    if game.status != "WAITING":
        return jsonify({"custom": True, "_message": "Game already started"}), 400
    if len(game.players) < 2:
        return jsonify({"custom": True, "_message": "Need at least 2 players"}), 400

    # Deal hole cards
    deck = Deck()
    for pig in game.players:
        cards = deck.deal(2)
        card_strs = [str(c) for c in cards]
        await prisma.playerHand.create(data={
            "game_id": game_id,
            "player_id": pig.player_id,
            "cards": json.dumps(card_strs)
        })

    # Set dealer, current player
    dealer_pos = 0
    current_pos = (dealer_pos + 3) % len(game.players)  # After SB, BB, UTG
    current_player_id = game.players[current_pos].player_id

    await prisma.game.update(
        where={"id": game_id},
        data={
            "status": "ACTIVE",
            "current_round": "PRE_FLOP",
            "dealer_position": dealer_pos,
            "current_player": current_player_id
        }
    )

    updated_game = await prisma.game.find_unique(where={"id": game_id}, include={"players": {"include": {"hand": True}}})
    return jsonify(updated_game.model_dump())

@poker_bp.route("/bet/<game_id>", methods=["POST"])
@with_prisma
@require_auth
async def place_bet(game_id, _jwt, prisma):
    data = request.get_json()
    action = data.get("action")  # FOLD, CHECK, CALL, BET, RAISE
    amount = data.get("amount", 0)

    game = await prisma.game.find_unique(
        where={"id": game_id},
        include={"players": {"include": {"bets": True}}, "bets": True}
    )
    if not game or game.status != "ACTIVE":
        return jsonify({"custom": True, "_message": "Game not active"}), 400

    player_in_game = next((p for p in game.players if p.player_id == _jwt["id"]), None)
    if not player_in_game:
        return jsonify({"custom": True, "_message": "Not in game"}), 400
    if game.current_player != _jwt["id"]:
        return jsonify({"custom": True, "_message": "Not your turn"}), 400

    # Logic for bet, call, etc. Simplified
    bet = await prisma.bet.create(data={
        "game_id": game_id,
        "player_id": _jwt["id"],
        "round": game.current_round,
        "action": action,
        "amount": amount
    })

    # Update pot, chips, next player, etc. Simplified
    await prisma.game.update(
        where={"id": game_id},
        data={"pot": game.pot + amount}
    )
    await prisma.playerInGame.update(
        where={"game_id_player_id": {"game_id": game_id, "player_id": _jwt["id"]}},
        data={"chips": player_in_game.chips - amount}
    )

    # Next player logic - simplified
    current_pos = (player_in_game.position + 1) % len(game.players)
    next_player = game.players[current_pos]
    await prisma.game.update(
        where={"id": game_id},
        data={"current_player": next_player.player_id}
    )

    return jsonify({"message": "Bet placed"})

# More routes for fold, check, etc., but basic for now

@poker_bp.route("/game/<game_id>", methods=["GET"])
@with_prisma
@require_auth
async def get_game(game_id, _jwt, prisma):
    game = await prisma.game.find_unique(
        where={"id": game_id},
        include={
            "players": {
                "include": {
                    "hand": True,
                    "bets": True,
                    "player": True
                }
            },
            "bets": True
        }
    )
    if not game:
        return jsonify({"custom": True, "_message": "Game not found"}), 404

    # Hide other players' hole cards
    for pig in game.players:
        if pig.player_id != _jwt["id"]:
            if pig.hand:
                pig.hand.cards = "hidden"

    return jsonify(game.model_dump())
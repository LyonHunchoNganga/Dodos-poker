import random
from typing import List, Tuple
from enum import Enum

class Suit(Enum):
    HEARTS = 'H'
    DIAMONDS = 'D'
    CLUBS = 'C'
    SPADES = 'S'

class Rank(Enum):
    TWO = '2'
    THREE = '3'
    FOUR = '4'
    FIVE = '5'
    SIX = '6'
    SEVEN = '7'
    EIGHT = '8'
    NINE = '9'
    TEN = 'T'
    JACK = 'J'
    QUEEN = 'Q'
    KING = 'K'
    ACE = 'A'

class Card:
    def __init__(self, rank: Rank, suit: Suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank.value}{self.suit.value}"

    def __repr__(self):
        return self.__str__()

    @property
    def value(self) -> int:
        return list(Rank).index(self.rank) + 2

class Deck:
    def __init__(self):
        self.cards = [Card(rank, suit) for rank in Rank for suit in Suit]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, num: int) -> List[Card]:
        if num > len(self.cards):
            raise ValueError("Not enough cards")
        dealt = self.cards[:num]
        self.cards = self.cards[num:]
        return dealt

class HandRank(Enum):
    HIGH_CARD = 1
    PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    STRAIGHT = 5
    FLUSH = 6
    FULL_HOUSE = 7
    FOUR_OF_A_KIND = 8
    STRAIGHT_FLUSH = 9
    ROYAL_FLUSH = 10

def evaluate_hand(cards: List[Card]) -> Tuple[HandRank, List[int]]:
    # Sort cards by value descending
    sorted_cards = sorted(cards, key=lambda c: c.value, reverse=True)
    ranks = [c.value for c in sorted_cards]
    suits = [c.suit for c in sorted_cards]

    # Check for flush
    is_flush = len(set(suits)) == 1

    # Check for straight
    unique_ranks = list(set(ranks))
    unique_ranks.sort(reverse=True)
    is_straight = False
    straight_high = 0
    if len(unique_ranks) >= 5:
        for i in range(len(unique_ranks) - 4):
            if unique_ranks[i] - unique_ranks[i+4] == 4:
                is_straight = True
                straight_high = unique_ranks[i]
                break
        # Check ace-low straight
        if not is_straight and set([14,2,3,4,5]).issubset(set(ranks)):
            is_straight = True
            straight_high = 5

    if is_flush and is_straight:
        if straight_high == 14:  # Ace high
            return HandRank.ROYAL_FLUSH, ranks
        return HandRank.STRAIGHT_FLUSH, [straight_high]

    if is_flush:
        return HandRank.FLUSH, ranks

    if is_straight:
        return HandRank.STRAIGHT, [straight_high]

    # Count frequencies
    from collections import Counter
    rank_counts = Counter(ranks)
    sorted_counts = sorted(rank_counts.items(), key=lambda x: (x[1], x[0]), reverse=True)

    if sorted_counts[0][1] == 4:
        return HandRank.FOUR_OF_A_KIND, [sorted_counts[0][0], sorted_counts[1][0]]

    if sorted_counts[0][1] == 3 and sorted_counts[1][1] >= 2:
        return HandRank.FULL_HOUSE, [sorted_counts[0][0], sorted_counts[1][0]]

    if sorted_counts[0][1] == 3:
        return HandRank.THREE_OF_A_KIND, [sorted_counts[0][0]] + [c[0] for c in sorted_counts[1:]]

    if sorted_counts[0][1] == 2 and sorted_counts[1][1] == 2:
        return HandRank.TWO_PAIR, [sorted_counts[0][0], sorted_counts[1][0], sorted_counts[2][0]]

    if sorted_counts[0][1] == 2:
        return HandRank.PAIR, [sorted_counts[0][0]] + [c[0] for c in sorted_counts[1:]]

    return HandRank.HIGH_CARD, ranks

def compare_hands(hand1: List[Card], hand2: List[Card]) -> int:
    rank1, vals1 = evaluate_hand(hand1)
    rank2, vals2 = evaluate_hand(hand2)
    if rank1.value > rank2.value:
        return 1
    elif rank1.value < rank2.value:
        return -1
    else:
        for v1, v2 in zip(vals1, vals2):
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1
        return 0
from game import Game

def play_game():
    game=Game()

    human=game.human
    pc=game.pc

    game.turn=human
    #Step 1 request to make bet
    
    human_amount=human.place_initial_bet()
    #human.update_amount_bet(human_amount)
    human.bet=human_amount
    
    pc_amount=pc.auto_match_or_raise(human_amount)
    #pc.update_amount_bet(human_amount)
    pc.bet=pc_amount

    if pc_amount=="l":
        print("Towel throwin Human won")
        return
    
    game.turn=human
    #remove
    #game.pot=pc_amount+human_amount
    
    k =0
    #1 betting round
    print("-------------------")
    print("Starting 1st betting round")
    print("---------------------")
    while True:
        print("Round ",k)
        print("------------------\n")
        if k>=1 and pc.bet==human.bet:
            print("All bets are equal.End the betting round")
            #completed betting round
            break
        k=k+1

        #check_fold_raise
        human_choice=human.call_fold_raise(player=pc)

        if human_choice=="l":
            print("PC WON THE GAME")
            return

        
        print("-----------------------")
        print("Human amount",human.amount)
        print("Human bet amount",human.bet)

        pc_choice=pc.auto_call_raise(player=human,k=k)

        if pc_choice=="l":
            print("Human Won")
            return

        print("pc amount",pc.amount)
        print("pc bet amount",pc.bet)
        print("-----------------------")

    #2
    print("-------------------")
    print("Completed betting round")
    print("---------------------")
    deck=game.deck
    deck.burn_card()
    game.community_cards.append(deck.give_card())
    game.community_cards.append(deck.give_card())
    game.community_cards.append(deck.give_card())
    game.print_community_card()
    print("--------------------")
    game.pot=human.bet+pc.bet
    human.reset_bet()
    pc.reset_bet()
    #setter on pot
    print("All money moved to betting pot")
    print("POT AMOUNT ",game.pot)
    print("--------------------")

    print("-------------------")
    print("Starting 2nd betting round")
    print("---------------------")

    k=0
    while True:

        if k>0 and pc.bet==human.bet:
            print("All bets are equal.End the betting round")
            #completed betting round
            break
        k=k+1

                #check_fold_raise
        human_choice=human.call_fold_raise(player=pc)

        if human_choice=="l":
            print("PC WON THE GAME")
            return

        
        print("-----------------------")
        print("Human amount",human.amount)
        print("Human bet amount",human.bet)

        pc_choice=pc.auto_call_raise(player=human,k=k)

        if pc_choice=="l":
            print("Human Won")
            return

        print("pc amount",pc.amount)
        print("pc bet amount",pc.bet)
        print("-----------------------")

    print("-------------------")
    print("Completed 2nd betting round")
    print("---------------------")
    deck=game.deck
    deck.burn_card()
    game.community_cards.append(deck.give_card())
    game.print_community_card()
    print("--------------------")
    game.pot=human.bet+pc.bet
    human.reset_bet()
    pc.reset_bet()
    #setter on pot
    print("All money moved to betting pot")
    print("POT AMOUNT ",game.pot)
    print("--------------------")

    print("-------------------")
    print("Starting Final betting round")
    print("---------------------")

    k=0
    while True:

        if k>0 and pc.bet==human.bet:
            print("All bets are equal.End the betting round")
            #completed betting round
            break
        k=k+1

                #check_fold_raise
        human_choice=human.call_fold_raise(player=pc)

        if human_choice=="l":
            print("PC WON THE GAME")
            return

        
        print("-----------------------")
        print("Human amount",human.amount)
        print("Human bet amount",human.bet)

        pc_choice=pc.auto_call_raise(player=human,k=k)

        if pc_choice=="l":
            print("Human Won")
            return

        print("pc amount",pc.amount)
        print("pc bet amount",pc.bet)
        print("-----------------------")

    print("-------------------")
    print("Completed 3rd betting round")
    print("---------------------")
    deck=game.deck
    deck.burn_card()
    game.community_cards.append(deck.give_card())
    game.print_community_card()
    print("--------------------")
    game.pot=human.bet+pc.bet
    human.reset_bet()
    pc.reset_bet()
    #setter on pot
    print("All money moved to betting pot")
    print("POT AMOUNT ",game.pot)
    print("--------------------")

    print("-------------------")
    print("Starting 3nd betting round")
    print("---------------------")

    #check for the winner

    






       
play_game()
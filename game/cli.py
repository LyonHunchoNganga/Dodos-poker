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
    game.pot=pc_amount+human_amount
    
    k =0
    #1 betting round
    print("-------------------")
    print("Starting 1st betting round")
    print("---------------------")
    while True:
        
        if k>=1 and pc.amount==human.amount:
            #completed betting round
            break
        k=k+1

        print("Human amount",human.amount)
        print("Human bet amount",human.bet)

        human.call_fold_raise(player=pc)
        #pc.auto_call_fold_raise
       

        

play_game()
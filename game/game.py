from deck import Deck
from player import Player

class Game():

    #betting current_pot:500 betting pot
    #betting
    def __init__(self):
        self.pot=0
        deck=Deck()
        deck.shuffle()
        deck.shuffle()
        human_cards= [deck.give_card(),deck.give_card()]
        pc_card=[deck.give_card(),deck.give_card()]
        #chess engine<>Draw:
        #prediction Engine<>Draw<>
        self.human=Player(type="human",
                          cards=human_cards,
                          bet=0,
                          name="John",amount=2000)
        self.pc=Player(type="pc",
                          cards=pc_card,
                          bet=0,
                          name="Stockfish",amount=2000)
        self._turn=self.human
        self.deck=deck
        self.community_cards=[]
    
    @property
    def turn(self):
        return self._turn
    
    @turn.setter
    def turn(self,player):

        if isinstance(player,Player):
            self._turn=player
        
        else:
            raise ValueError("The turn must be assined to a player object")

    
    def print_community_card(self):
        print("Commnity cards")
        for card in self.community_cards:
            card.print_card()

    def check_winner(self):
        pass

    def check_rank_card(self,cards,rank):
        for card in cards:
            if card.rank==rank:
                return card
        return None


    def check_royal_flush(self,cards):

        royal=["A","K","Q","J","10"]
        checked_cards=[]
        #Sorting algorithims
        #[10,23,12,45,11,58] ->bubble sort
        #10,11,12,23,45,58
        for rank in royal:
            card=self.check_rank_card(cards=cards,rank=rank)
            if card:
                checked_cards.append(card)
            else:
                return None


        return
        for i,rank in enumerate(royal):
            found=False
            for j,card in enumerate(cards):
                if card.rank==rank:
                    found=True
                    checked_cards.append(card)
                    break
            if found==True:
                continue
            return None
        
        #five cards that are required for the royal flush
        suite=checked_cards[0].suite
        for card in checked_cards:
            if suite != card.suite:
                return None #dont have the royal flush
        
        #have royal flush
        return True
    
            


    
    def check_straight_flush(self):
        pc_cards=self.community_cards+self.pc.cards
        human_cards=self.community_cards+self.human.cards
        #come up with an algorithim to check for a royoal flush
    
#object oriented programming 
if __name__=="__main__":
    game=Game()
    game.deck.print_deck()
    print("This is the deck")
    print("Pc cards")
    game.pc.cards[0].print_card()
    game.pc.cards[1].print_card()
    print("This is the deck")
    print("Human cards")
    game.human.cards[0].print_card()
    game.human.cards[1].print_card()
    #


#[10,23,12,45,11,58] 
#itteration
#[10,12,23,45,11,58]
#[10,12,23,11,45,58]
#[10,12,23,11,45,58]
#[10,12,11,23,45,58]
#[10,11,12,23,45,58]
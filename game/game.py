
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
    
    @property
    def turn(self):
        return self._turn
    
    @turn.setter
    def turn(self,player):

        if isinstance(player,Player):
            self._turn=player
        
        else:
            raise ValueError("The turn must be assined to a player object")

    

        #self.turn=self.human
        
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
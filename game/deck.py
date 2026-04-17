from card import Card
import random

class Deck():

    def __init__(self):

        ranks=Card.RANKS
        suites=Card.SUITES
        deck=[]#datatype is an array


        for rank in ranks:
            for suite in suites:
                card=Card(suite=suite,rank=rank)
                deck.append(card)
        self.deck=deck

    
    def shuffle(self):
        newDeck=[]
        deck=self.deck
        while True:
            if len(deck)==1:
                card=deck[0]
                newDeck.append(card)
                break
            n=random.randint(0,len(deck)-1)
       
            card=deck[n] 
            deck.pop(n)
            newDeck.append(card)
        self.deck=newDeck

    def print_deck(self):
        deck=self.deck
        print("Deck size is",len(deck))
        print("..............")
        for card in deck:
            card.print_card()
            print("-------------")

    def burn_card(self):
        #print("before buring deck")
        #self.print_deck()
        #print("After buring")
        top_card=self.deck[0]
        self.deck.pop(0)
        self.deck.append(top_card)
        #self.print_deck()
        pass
    ##

    def give_card(self):
        #->take a card out of the deck from the end deck 
        #and give it out
        top_card=self.deck[0]
        self.deck.pop(0)
        return top_card
        
if __name__=="__main__":
    d1=Deck()
    d1.shuffle()
    human_cards=[d1.give_card(),
                 d1.give_card(),
                 d1.give_card(),
                 d1.give_card(),
                d1.give_card(),
                d1.give_card(),
                d1.give_card()
                 ]

    for card in human_cards:
        card.print_card()

    royal=["A","K","Q","J","10"]

    sorted_cards=[]

    for rank in royal:
        for card in human_cards:
            if card.rank==rank:
                sorted_cards.append(card)

    print("Sorted cards")
    for card in sorted_cards:
        card.print_card()

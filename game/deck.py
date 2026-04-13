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
        print("...............")
        for card in deck:
            card.print_card()
            print("—————————————")

    def burn_card(self):
        print("before burning deck")
        self.print_deck()
        print("After burning")
        self.deck.pop(0)
        self.print_deck()

    def give_card(self):
        #→take a card out of the deck from the end deck
        #and give it out
        top_card=self.deck[0]
        self.deck.pop(0)
        return top_card

if __name__=="__main__":
    d1=Deck()
    d1.shuffle()
    #d1.burn_card()
    card=d1.give_card()
    print("given card is")
    card.print_card()
    d1.print_deck()
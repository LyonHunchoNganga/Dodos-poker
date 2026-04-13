import random
import time

class Player():

    def __init__(self,type="pc",cards=[],bet=0,name="",amount=0):

        self.name=name
        self.type=type
        self.cards=cards
        self._bet=bet
        self.amount=amount

    @property
    def bet(self):

        return self._bet
    
    @bet.setter
    def bet(self,amount):
        #Checks -> safe bets
        #ensure you check amount is a number greater than 0
        self._bet=self._bet+amount
        self.amount=self.amount-amount

    def place_initial_bet(self):
        
        while True:
            amount=input(f"Place initial bet amount.Current amount is {self.amount}: ")

            if amount.isdigit():
                n=int(amount)
                if n>0 and n<=self.amount:
                    #self.amount=self.amount-n #use a setter 
                    self.bet=n
                    return n
                
                print("Invalid amount entered.")
                print(f"amount must range from 1 to {self.amount}")
                print("try again")
            
            else:
                print(f"enter a number as valid amount between 1 and {self.amount}")

    def call_fold_raise(self,player):
            choice=input("Press 1 to call \nPress 2 fold  \nPress 3 to raise ")
            if choice =='1':
                return self.call(player)
            if choice=='2':
                return self.fold(player)
            if choice=='3':
                return self.raise_stake(player)
            print(f"wrong choise {choice}. choose 1 to 3")
            self.call_fold_raise(player)
    
    def call(self,player):
        print("Amount Bet is ",player.amount)
        diff=self.bet-player.bet

        if diff>0:
            return True
        diff=abs(diff)
        if self.amount>diff:
            print("Cant call not enough money")
            return "l"
        self.bet=diff
        #self.amount=self.amount-diff
        print(f"I call your bet.\nI bet ${diff}")


    def fold(self,player):
        print('I Fold')
        return "l"
    
    def raise_stake(self,player):
        raise_amount=input(f"Enter raise amount. Max amount {self.amount}")
        raise_amount=int(raise_amount)
        if raise_amount>self.amount:
            print("check and restart propcess")
            self.raise_stake(player)
            return
        print(f"I raise by amount ",raise_amount)
        self.bet=raise_amount
        #self.amount=self.amount=raise_amount
        return raise_amount
        
    

    def auto_match_or_raise(self,amount):
        print("Pc thinking.What to do")
        time.sleep(2)
        to_do=random.randint(1,2)
        raise_amount=amount+random.randint(10,250)

        if raise_amount>self.amount:
            to_do=1

        #1 is match
        if to_do==1:
            if self.amount>amount:
                #self.amount-amount
                self.bet=amount
               
                print(f"Matching your action. Bet {amount}")
                return amount
            else :
                return "l"
        
        #self.amount=self.amount-raise_amount
        self.bet=raise_amount

        print("I have a good feeling. I raise by ",raise_amount)
        return raise_amount
    
   
        




                




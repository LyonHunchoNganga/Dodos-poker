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

    def reset_bet(self):
        self.bet=0

    def place_initial_bet(self):
        
        while True:
            amount=input(f"Place initial bet amount.Current amount is {self.amount}: ")

            if amount.isdigit():
                n=int(amount)
                if n>0 and n<=self.amount:
                    return n
                
                print("Invalid amount entered.")
                print(f"amount must range from 1 to {self.amount}")
                print("try again")
            
            else:
                print(f"enter a number as valid amount between 1 and {self.amount}")

    def call_fold_raise(self,player):
            choice=input("Press 1 to call \nPress 2 fold  \nPress 3 to raise\n")
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
        if diff>self.amount:
            print("Cant call not enough money")
            return "l"
        self.bet=diff
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
        
    
    def auto_call_raise(self,player,k):
      
        print("Pc thinking.What to do")
        human=player
        time.sleep(2)
        to_do=random.randint(1,2)

        print("Human Bet ",human.bet)
        print("PC bet is  ",self.bet)
        
        ## 200 ,100 ->100
        ## human: 100 pc 50 50-100
        diff=human.bet-self.bet
        print("Diff is ",diff)

        if diff<0:
            print("I Call your bet")
            return
        
        if diff>self.amount:
            print("I fold. Bet too high")
            return "l"
        
                #raise:
        raise_amount=random.randint(1,30)
        raise_stake=diff+raise_amount

        if raise_stake>self.amount or k>=3:
            to_do=1

        #Match the bet
        if to_do==1:
            self.bet=diff
            print(f"I call your bet. I bet ",diff)
            return
        
        self.bet=raise_stake
        print(f"I see your action. I raise you by {raise_amount} ")
                

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
                print(f"Matching your action. Bet {amount}")
                return amount
            else :
                return "l"
        
        #self.amount=self.amount-raise_amount
        self.bet=raise_amount

        print("I have a good feeling. I raise by ",raise_amount)
        return raise_amount

#Tối ưu hóa Player.point
#Deck
import random
import string
number=("A","2","3","4","5","6","7","8","9","10","J","Q","K")
adj=("♠","♣","♥","♦")
values={"A":11,
        "2":2,
        "3":3,
        "4":4,
        "5":5,
        "6":6,
        "7":7,
        "8":8,
        "9":9,
        "1":10,
        "J":10,
        "Q":10,
        "K":10}
Deck=[]
new_Deck=[]
for i in range(13):
    for j in range(4):
        Deck.append(number[i]+adj[j])
for i in range(13):
    for j in range(4):
        new_Deck.append(number[i]+adj[j]) 

class player():
    def __init__(self, name, money):
        self.card=[]
        self.name = name
        self.money = money
        self.point=0
        
        
    def __repr__(self):
        return f'Hello {self.name}, you have {self.money}.'
    
    def hit(self):
        global Deck
        a=random.choice(Deck)
        (self.card).append(a)
        Deck.remove(a)
        pass
    
    def points(self):
        self.point=0
        a=len(self.card)
        if self.name != "Dealer":
            print (f'{self.name}, here is your card: {self.card}')
            for i in range(a):
                if self.card[i][0] =="A" and self.point>10:
                    self.point+=1
                else:
                    self.point+=values[self.card[i][0]]
            print (f"{self.name} have {self.point} points.")
        elif self.name == "Dealer" and a>=2:
            print(f"{self.name}'s card: {self.card}")
            for i in range(a):
                self.point+=values[self.card[i][0]]
            print(f"{self.name} have {self.point} points.")
            pass
    
    def bet(self):
        b=input("How much you want to bet? ")
        a1=[]
        a=string.ascii_letters
        for i in range(len(a)):
            a1.append(a[i])
        for i in range(len(b)):
            while b[i] in a1:
                b=input("You must choose a number. How much you wanna bet? ")
        b=int(b)
        while b>self.money:
            print(f"You can't bet what you can't amount! You have {self.money}!")
            b=input("How much you want to bet? ")
            for i in range(len(b)):
                while b[i] in a1:
                    b=input("You must choose a number. How much you wanna bet? ")
            b=int(b)
        self.bet=b
        return b
    
    def play_again(self):
        global Deck, new_Deck
        self.card=[]
        Deck = new_Deck
    pass
#--------------------------------------------------------------------
show_dealer = True
def play():
    global show_dealer
    name=input("Welcome to BlackJack. What's your name? ")
    money=input("How much you wanna play todays? ")
    a1=[]
    a=string.ascii_letters
    for i in range(len(a)):
        a1.append(a[i])
    for i in range(len(money)):
        while money[i] in a1:
            money=input("You must choose a number. How much you wanna play today? ")
    money=int(money)
    a3=True
    while a3:
        Play = player(name, money)
        Dealer = player("Dealer",10**10)
        Play.bet()
        for i in range(2):
            Play.hit()
        Dealer.hit()
        Dealer.points()
        Play.points()
        if Play.point == 21:
            print("You get a blackjack.")
        else:
            while Play.point <21:
                
                a=input("Do you wanna hit or stay? (h or s) ")
                if a == "h":
                    Play.hit()
                    Play.points()
                    if Play.point == 21:
                        print("You get a blackjack.")
                    elif Play.point >21:
                        print("You get a Bust.")
                elif a == "s":
                    break

        #chốt bài của Dealer
        if Play.point<21:
            while Dealer.point<17:
               Dealer.hit()        #Dealer đã có 2 lá
               Dealer.points()         #tính điểm cho Dealer

        k=j=0
        if Play.point >21:
            print(f"{Play.name} lose this turn.")
            j=1
        elif Play.point == Dealer.point:
            print("This turn is tie.")
        elif Play.point==21:
            k=2
        elif Dealer.point >21 :
            print(f"{Dealer.name} get a Bust.")
            k=1
        elif Play.point > Dealer.point :
            print(f"Dealer has {Dealer.point}, you have {Play.point}.")
            print(f"{Play.name} win this turn.")
            k=1
        elif Play.point < Dealer.point :
            print(f"Dealer has {Dealer.point}, you have {Play.point}.")
            print(f"You lose this turn.")
            j=1

        if k==1:
            Play.money+=Play.bet
        elif k==2:
            Play.money+=1.5*Play.bet
        elif j==1:
            Play.money-=Play.bet
        elif k==j==0:
            pass
        print(f"{Play.name} has {Play.money}.")
        
        if Play.money <0:
            print(f"{Play.name} has lose all the money!")

        while Play.money >0:
            a2=input("Do you want to play again? (y/n): ") 
            if a2=="y":
               Play.play_again()
               break
            elif a2=="n":
                print(f"Thank for join the game!\n {Play.name} has {Play.money} $.\n See you again! ")
                a3=False
                break
        
play()
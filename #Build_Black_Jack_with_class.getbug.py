#Deck
import random
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
        
    def __repr__(self):
        return f'Hello {self.name}, you have {self.money}.'
    
    def hit(self):
        global Deck
        a=random.choice(Deck)
        (self.card).append(a)
        Deck.remove(a)
        pass
    
    def point(self):
        self.point=0
        print (f'{self.name}, here is your card: {self.card}')
        a=len(self.card)
        if self.name != "Dealer":
            for i in range(a):
                if self.card[i][0] =="A" and self.point>10:
                    self.point+=1
                else:
                    self.point+=values[self.card[i][0]]
            print (f"{self.name} have {self.point} points.")
        else:
            pass
#--------------------------------------------------------------------

def play():
    name=input("Welcome to BlackJack. What's your name? ")
    money=input("How much you wanna play todays? ")
    Player = player(name, money)
    Dealer = player("Dealer",10**10)
    for i in range(2):
        Player.hit()
    Dealer.hit()
    Dealer.point()
    Player.point()
    while True:
        a=input("Do you wanna hit or stay? (h or s) ")
        if a == "h":
            Player.hit()
            Player.point()
        elif a == "s":
            break
        
    pass

play()
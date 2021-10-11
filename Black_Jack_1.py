#BlackJack_checking1
import random 
import string
#Tạo một bộ bài
number=("A","2","3","4","5","6","7","8","9","10","J","Q","K")
adj=("♠","♣","♥","♦")
Deck = []
Player = []
Dealer= []
new_Deck=[]
for i in range(13):
    for j in range(4):
        Deck.append([number[i]+adj[j]])

for i in range(13):
    for j in range(4):
        new_Deck.append([number[i]+adj[j]])

#Tạo biến xác định game over
game_still_going = True
still_show_dealer = True
out_of_cash = False
#value_of_player_card
v=0
dp=0
player_acc=0
def check_game_over():
    global game_still_going, v, still_show_dealer
    if v==21:
        print("You get a blackjack.")
        game_still_going = False    
    elif v <21:
      game_still_going=True
    elif v>21:
        game_still_going = False
        still_show_dealer=False

#Quy định giá trị của quân bài
#Sử dụng dạng từ điển: dictionary
values={"A":"11",
        "2":"2",
        "3":"3",
        "4":"4",
        "5":"5",
        "6":"6",
        "7":"7",
        "8":"8",
        "9":"9",
        "1":"10",
        "J":"10",
        "Q":"10",
        "K":"10"}

#Chọn 2 lá bài cho nhà cái và người chơi
#Nhà cái: 1 là ngửa, 1 lá úp
def getcard():
    global Deck
    a=random.choice(Deck)
    Deck.remove(a)
    return a

def dealer():
    global Deck, Dealer
    Dealer=getcard()
    print("Bài của Dealer: ",Dealer,"--X")

def player():
    global Deck, v
    global Player
    for i in range(2):
        Player.append(getcard())
    print("Bài của người chơi: ",Player)
    v=0
    if Player[0][0][0] == Player[1][0][0]=="A":
        v=12
    else:
        for i in range(len(Player)):
            v+=int(values[Player[i][0][0]])
    print("Bài của bạn có: ",v, " điểm.")

def dealer_point():
    global Dealer, still_show_dealer, dp
    Dealer.append(getcard())
    dp=0
    for i in range(len(Dealer)):
        dp+=int(values[Dealer[i][0][0]])
    print("Dealer's card: ",Dealer)
    print("Dealer's point: ", dp)
    while dp < 17:
        dp1=0
        Dealer.append(getcard())
        for i in range(len(Dealer)):
            dp1+=int(values[Dealer[i][0][0]])
        dp=dp1
        print("Dealer's card: ",Dealer)
        print("Dealer's ponit: ", dp)
    still_show_dealer=False
    
def play_again():
    global v,dp,Player,Dealer,still_show_dealer,Deck,new_Deck,game_still_going, out_of_cash
    a1=True
    if not out_of_cash:
        while a1:
            a=input("Do you want to play again? (y or n): ")
            if a=="y":   
                v=0
                dp=0
                Player=[]
                Dealer = []
                still_show_dealer= True
                new_Deck=Deck
                game_still_going=True
                a1=False
            elif a=="n":
                out_of_cash = True
                a1=False
                pass

def check_account():
    global player_acc, out_of_cash
    if player_acc >0:
        out_of_cash=False
    if player_acc <=0:
        out_of_cash=True
        print("You lose all your money.")
    
def value_of_player():
    global Player, v
    a=len(Player)-1
    if Player[a][0][0] =="A" and v>11:
        v+=1
    else:
        v+=int(values[Player[a][0][0]])
    print("Bài của bạn có: ",v, " điểm.")
    
def player_acc():
    global player_acc
    a=string.ascii_letters
    a1=[]
    for i in range(len(a)):
        a1.append(a[i])
    b=input("How much you wanna play today? ")
    for i in range(len(b)):
        while b[i] in a1:
            b=input("You must choose a number. How much you want to play today? ")
    player_acc=int(b)
    
def play():
    global game_still_going, v, player_acc, still_show_dealer,player_acc,Player,Dealer,dp, out_of_cash
    player_acc()
    
    while not out_of_cash:
        b=input("How much you wanna bet? ")
        a1=[]
        a=string.ascii_letters
        for i in range(len(a)):
            a1.append(a[i])
        for i in range(len(b)):
            while b[i] in a1:
                b=input("You must choose a number. How much you wanna bet? ")
        b=int(b)
        dealer()
        player()
        check_game_over()
        while game_still_going:
            a=input("You wanna hit or stay? (h or s) ")
            if a=="h":
                Player.append(getcard())
                print("Bài của bạn: " , Player)
                value_of_player()
                check_game_over()
            elif a=="s":
                game_still_going=False
    
        while still_show_dealer:
            dealer_point()
        
        if v > 21:
            player_acc=player_acc-b
            print("You get a Bust lose this turn, you have: ", player_acc)
        elif v==21 and dp!=21:
            player_acc=player_acc+1.5*b
            print("You get blackjack have: ", player_acc)
        elif dp>21:
            player_acc=player_acc+b
            print("Dealer get a Bust. You won and have: ", player_acc)
        elif v>dp:
            player_acc=player_acc+b
            print("You win and have: ", player_acc)
        elif dp>v:
            player_acc=player_acc-b
            print("You lose and have: ", player_acc)
            print("diem nc: ",v," diem dl: ",dp)
        elif v==dp:
            print("Tie, you have: ", player_acc)  
        check_account()
        play_again()
            
play()
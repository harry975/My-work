#BlackJack
import random 
#Tạo một bộ bài
number=("A","2","3","4","5","6","7","8","9","10","J","Q","K")
adj=("♠","♣","♥","♦")
Deck = []
Player = []
Dealer= []
for i in range(13):
    for j in range(4):
        Deck.append([number[i]+adj[j]])

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
    if v <21:
        a=input("Do you wanna hit or stay? (h or s) ")
        if a=="h":
            game_still_going = True
        elif a=="s":
            game_still_going = False
            
    if v>21:
        print("You get a bust and lose your bet.")
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
    global Deck
    global Player
    for i in range(2):
        Player.append(getcard())
    print("Bài của người chơi: ",Player)

def value_of_player():
    global Player, v
    v=0
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
    print("Dealer's ponit: ", dp)
    while dp < 17:
        dp1=0
        Dealer.append(getcard())
        for i in range(len(Dealer)):
            dp1+=int(values[Dealer[i][0][0]])
        dp=dp1
        print("Dealer's card: ",Dealer)
        print("Dealer's ponit: ", dp)
    still_show_dealer=False
    
    
        
def bet():
    global v, dp, player_acc
    b=int(input("How much you wanna bet? ")
    if v>21:
        player_acc=player_acc-b
        print("You still have: ", player_acc)
    elif v<21 and dp>21:
        player_acc=player_acc+b
        Print("You won and have: ", player_acc)
    elif v=21 and dp<21:
        player_acc=player_acc+1.5*b
        print("You have: ", player_acc)
    elif v==dp:
        print("Tie")  
    v=0
    dp=0
    
def play_again():
    pass

def account():
    global play_acc, out_of_cash
    play_account=int(input("How much money you want to play? "))
    if play_acc >=0:
        out_of_cash=False
    if play_acc <0:
        out_of_cash=True
        

def play():
    global game_still_going, v, player_acc, still_show_dealer,play_acc
    account()
    dealer()
    player()
    value_of_player()
    check_game_over()
    while not out_of_cash:
        bet()
        while game_still_going:
            Player.append(getcard())
            print("Bài của người chơi: ",Player)
            value_of_player()
            check_game_over()
    
        while still_show_dealer:
            dealer_point()
    
    
play()
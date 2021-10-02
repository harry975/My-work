#ttt.youtube.py
#global variable
import random


game_still_going = True
winner = None
current_player = "X"

#board 
board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]
#display board

   
def choosewpf():
    global current_player
    list1 = [0, 1]
    k = random.choice(list1)
    print(k)
    if k==1:
        current_player = "X"
        print("nguoi choi truoc la X")
    elif k==0:
        current_player = "O"
        print("nguoi choi truoc la O")


def displayboard():
    print(board[0]+"|" +board[1]+"|"+board[2])
    print(board[3]+"|" +board[4]+"|"+board[5])
    print(board[6]+"|" +board[7]+"|"+board[8])
    


#play game
def playgame():
    
    global game_still_going, winner, how_win
    
    choosewpf()
    
    displayboard()
    
    while game_still_going:
        handleturn(current_player)
        
        check_game_over()
        
        flip_player()
        
    if winner == "X":
        print("Winner is X ") 
    elif winner == "O":
        print("Winner is O ") 
      
    else:
        print("No one wins!")
        
    play_again()
        
        
#handle turn
def handleturn(current_player):
    p=input(current_player +" choose the position form 1-9: ")
    while int(p) not in range(10):
        p= input(current_player +" please choose the position from 1-9: ")
    p=int(p)-1 
    while board[p] != " ":
        p = input(current_player+" please choose the empty place ")
        p= int(p) - 1
    
    board[p]=current_player
    displayboard()
    return
    

#check win
def check_win():
    global winner, game_still_going
    #check rows 
    if board[0] == board[1] == board[2] and board[0] != " ":
        winner = board[0]
        game_still_going = False
    if board[3] == board[4] == board[5] and board[3] != " ":
        winner = board[3]
        game_still_going = False
    if board[6] == board[7] == board[8] and board[6] != " ":
        winner = board[0]
        game_still_going = False
        
    #check columns 
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] and board[i] != " ":
            winner = board[i]
            game_still_going = False
               
    #check diagonals
    if board[0] == board[4] == board[8] and board[0] != " ":
        
        winner = board[0]
        game_still_going = False
    elif board[2] == board[4] == board[6] and board[2] != " ":
        winner = board[2]
        game_still_going = False
        
    
    return
        
        
#check tie
def check_tie():
    global winner,game_still_going
    if " " not in board and winner == None:
        game_still_going = False     
    return

def check_game_over():
    check_win()
    check_tie()
#flip_player()

def flip_player():
    global current_player
    
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    
    return

def play_again():
    global game_still_going, board
    p=input("Do you want to play again? (Y or N): ")
    p=p.upper()
    while p != "Y" and p != "N":
        p=input("Do you want to play again? (Y or N): ")
        p=p.upper()
    
    if p== "Y":
        game_still_going = True
        for i in range(9):
            board[i]=" "
        playgame()
    elif p == "N":
        game_still_going = False
        return
        
playgame()
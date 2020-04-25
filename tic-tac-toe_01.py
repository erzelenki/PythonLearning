from random import seed
from random import choice

def DisplayBoard(board):
    print("+-------+-------+-------+")
    for i in range(0,9,3):
        print("|       |       |       |")
        print("|   ",board[i],"   |   ",board[i+1],"   |   ",board[i+2],"   |",sep="")   
        print("|       |       |       |")
        print("+-------+-------+-------+")

def EnterMove(board):
    while True:
        user_move=int(input("Enter your move "))
        if user_move in range(1,10):
            if board[user_move-1]!="O" and board[user_move-1]!="X":
                board[user_move-1]="O"
                break
            else:
                print("This cell is already occupied, please chose another")
                continue
        else:
            print(user_move, "is not valid value, please chose value from 1 to 9")
            continue

def MakeListOfFreeFields(board):
    counter=0
    free_cells=[]
    for row in range (1,4):
        for collumn in range (1,4):
            if board[counter] != "O" and board[counter] != "X":
                free_cells.append((row,collumn))
            counter+=1
    return free_cells

def VictoryFor(board, sign):
    win_comb=((1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7))
    for i in range(len(win_comb)-1):
        win=True
        for j in range(3):
            win=board[win_comb[i][j]-1]==sign and win
        if win and sign=="X":
            print ("I win!")
            return True
            break
        if win and sign=="O":
            print ("You win!")
            return True
            break
    return False

def DrawMove(board):
    DisplayBoard(board)
    while MakeListOfFreeFields(board)!=[]:
        new_point=choice(MakeListOfFreeFields(board))
        board [new_point[1]+(new_point[0]-1)*3-1]= "O"
        DisplayBoard(board)
        if VictoryFor(board, "O"):
            return
        new_point=choice(MakeListOfFreeFields(board))
        board [new_point[1]+(new_point[0]-1)*3-1]= "X"
        DisplayBoard(board)
        if VictoryFor(board, "X"):
            return
    print("A tie!")

while True:
    DrawMove([1,2,3,4,"X",6,7,8,9])

        
    


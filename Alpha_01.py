import os
import msvcrt
playerX = 0
playerY = 0
board = []

for x in range(0,11):
    board.append(["*"]*11)

def print_board(board):
    for x in board:
        print(x)

while True:
   #check to see if we have to move player and update coordinate
    key = msvcrt.getch()
    if key == b'a':
       playerX-=3
       print_board(board)
    elif key == b'd':
       playerX+=3
       print_board(board)
    elif key == b'w':
       playerY-=1
       print_board(board)
    elif key == b's':
       playerY+=1
       print_board(board)

    os.system('cls')
    for i in range(playerY):
       print(" ")
    for i in range(playerX):
       print(" " ,end='')
    print("X",flush=True,end='')



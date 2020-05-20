from turtle import Screen, Turtle
board =[]

for x in range(0,11):
    board.append(["*"]*11)

def print_board(board):
    for x in board:
        print(x)

print_board(board)

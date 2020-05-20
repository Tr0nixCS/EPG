# Battleship Challenge - 101computing.net/battleship-challenge
import turtle
from random import randint

myPen = turtle.Turtle()
myPen.tracer(0)
myPen.speed(0)
myPen.color("#000000")
topLeft_x = -150
topLeft_y = 150


def addSubmarine(grid):
    # Place a submarine on the grid
    # A submarine is a small ship of size 1
    x = randint(0, 9)
    y = randint(0, 9)
    # Check that there is not already a boat at this location
    while grid[x][y] != 0:
        x = randint(0, 9)
        y = randint(0, 9)
    # Add submarine to the grid
    grid[x][y] = 1



def addDestroyer(grid):
    # Place a destroyer on the grid
    # A destroyer is a ship of size 2
    x = randint(0, 9)
    y = randint(0, 9)
    # The boat needs to be of size 2, either vertically or horizontally cannot go off the grid or use a position that is already used.
    ######################### Complete code here


def addCruiser(grid):
    # Place a cruiser on the grid
    # A cruiser is a ship of size 3
    x = randint(0, 9)
    y = randint(0, 9)
    # The boat needs to be of size 3, either vertically or horizontally cannot go off the grid or use a position that is already used.
    ######################### Complete code here


def addAircraftCarrier(grid):
    # Place an aircraft carrier on the grid
    # An aircraft carrier is a large ship of size 4
    x = randint(0, 9)
    y = randint(0, 9)
    # The boat needs to be of size 4, either vertically or horizontally cannot go off the grid or use a position that is already used.
    ######################### Complete code here


def drawGrid(intDim):
    for i in range(0, 11):
        myPen.penup()
        myPen.goto(topLeft_x, topLeft_y - i * intDim)
        myPen.pendown()
        myPen.goto(topLeft_x + 10 * intDim, topLeft_y - i * intDim)
    for i in range(0, 11):
        myPen.penup()
        myPen.goto(topLeft_x + i * intDim, topLeft_y)
        myPen.pendown()
        myPen.goto(topLeft_x + i * intDim, topLeft_y - 10 * intDim)
    for i in range(0, 10):
        myPen.penup()
        myPen.goto(topLeft_x + i * intDim + 10, topLeft_y + 10)
        myPen.write(chr(65 + i))
    for i in range(1, 11):
        myPen.penup()
        myPen.goto(topLeft_x - 15, topLeft_y - i * intDim + 10)
        myPen.write(str(i))

    myPen.setheading(0)
    myPen.goto(topLeft_x, topLeft_y - intDim)
    for row in range(0, 10):
        for column in range(0, 10):
            if grid[column][row] > 0:
                box(intDim)
            myPen.penup()
            myPen.forward(intDim)
            myPen.pendown()
        myPen.setheading(270)
        myPen.penup()
        myPen.forward(intDim)
        myPen.setheading(180)
        myPen.forward(intDim * 10)
        myPen.setheading(0)
        myPen.pendown()


# This function draws a box by drawing each side of the square and using the fill function
def box(intDim):
    myPen.begin_fill()
    # 0 deg.
    myPen.forward(intDim)
    myPen.left(90)
    # 90 deg.
    myPen.forward(intDim)
    myPen.left(90)
    # 180 deg.
    myPen.forward(intDim)
    myPen.left(90)
    # 270 deg.
    myPen.forward(intDim)
    myPen.end_fill()
    myPen.setheading(0)


####################### MAIN PROGRAM STARTS HERE ######################
# initialise empty 10 by 10 grid
grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

addSubmarine(grid)  # Place submarine on the grid
addDestroyer(grid)  # Place first destroyer on the grid
addDestroyer(grid)  # Place second destroyer on the grid
addCruiser(grid)  # Place first cruiser on the grid
addCruiser(grid)  # Place second cruiser on the grid
addAircraftCarrier(grid)  # Place aircraft carrier destroyer on the grid

drawGrid(25)  # 25 is the width of each square on the grid
myPen.getscreen().update()
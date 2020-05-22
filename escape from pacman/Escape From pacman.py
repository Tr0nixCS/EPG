# turtple graphics game
import turtle
import math
import random
from time import sleep

from pip._vendor.distlib.compat import raw_input

# screen set up
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.bgpic("backgound2.gif")
wn.tracer(100)
wn.register_shape("pacman.gif")
wn.register_shape("coin.gif")
# draw border
mypen = turtle.Turtle()
mypen.penup()
mypen.speed(0)
mypen.setposition(-300, -300)
mypen.pendown()
mypen.pensize(3)
for side in range(4):
    mypen.forward(600)
    mypen.left(90)
# draw grid
mypen.forward(60)
for i in range(10):
    for i in range(10):
        for squar in range(4):
            mypen.pendown()
            mypen.left(90)
            mypen.forward(60)
        mypen.penup()
        mypen.forward(60)
    mypen.right(180)
    mypen.forward(660)
    mypen.right(90)
    mypen.forward(60)
    mypen.right(90)
    mypen.forward(60)
mypen.hideturtle()

# pacman random possitions
pacxcor = [-270, -210, -150, -90, -30, 30, 90, 150, 210, 270]
pacycor = [-270, -210, -150, -90, -30, 30, 90, 150, 210, 270]

# the player
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(-270, -270)
# coin1
coin = turtle.Turtle()
coin.shape("coin.gif")
coin.penup()
coin.speed(0)
coin.setposition(270, -270)

# coin2

coin2 = turtle.Turtle()
coin2.shape("coin.gif")
coin2.penup()
coin2.speed(0)
coin2.setposition(270, 270)
coin2.hideturtle()

# finishline
finish = turtle.Turtle()
finish.shape("square")
finish.color("blue")
finish.penup()
finish.speed(0)
finish.setposition(-270, 270)

# win conditions
win1 = 0
win2 = 0
win3 = 0

# increase dificulty
goals1 = 0
goals2 = 0
pacmen2 = 0

# create pacmen
maxGoals = 6
goals = []
for count in range(maxGoals):
    turning = [90, 180, 270, 360]
    goals.append(turtle.Turtle())
    goals[count].penup()
    goals[count].color("red")
    goals[count].shape("pacman.gif")
    goals[count].speed(0)
    paca = random.randint(0, 9)
    pacb = random.randint(0, 9)
    if paca == 0 and pacb == 0:
        pacb = random.randint(0, 9)
    if paca == 9 and pacb == 0:
        pacb = random.randint(0, 9)
    goals[count].setposition(pacxcor[paca], pacycor[pacb])
    randompick = random.randint(0, 3)
    goals[count].right(turning[randompick])
    goals[count].showturtle()
maxpacmen = 5
pacmen = []
for count in range(maxpacmen):
    turning = [90, 180, 270, 360]
    pacmen.append(turtle.Turtle())
    pacmen[count].penup()
    pacmen[count].color("red")
    pacmen[count].shape("pacman.gif")
    pacmen[count].speed(0)
    paca = random.randint(0, 9)
    pacb = random.randint(0, 9)
    if paca == 0 and pacb == 0:
        pacb = random.randint(0, 9)
    if paca == 9 and pacb == 0:
        pacb = random.randint(0, 9)
    pacmen[count].setposition(pacxcor[paca], pacycor[pacb])
    randompick = random.randint(0, 3)
    pacmen[count].right(turning[randompick])
    pacmen[count].hideturtle()
# set speed
speed = 0


# define Functions
def win():
    if win1 == 1 and win2 == 1:
        print("YOU HAVE ESCAPED FROM PACMAN")
        sleep(1000)


def turnleft():  # turn left
    player.left(90)


def turnright():  # turn right
    player.right(90)


def forward():  # speedup
    player.forward(60)


def back():  # drop bomb
    player.forward(-60)


def isCollision(t1, t2):  # collision checking
    d = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if d < 20:
        return True
    else:
        return False


def goalsMove():  # pacmen movement
    for count in range(maxGoals):

        if goals[count].xcor() > 300 or goals[count].xcor() < -300:
            goals[count].right(180)
            goals[count].forward(60)
        if goals[count].ycor() > 300 or goals[count].ycor() < -300:
            goals[count].right(180)
            goals[count].forward(60)

        goals[count].forward(0.5)


def pacmen2Move():  # pacmen2 movement
    for count in range(maxpacmen):

        if pacmen[count].xcor() > 300 or pacmen[count].xcor() < -300:
            pacmen[count].right(180)
            pacmen[count].forward(60)
        if pacmen[count].ycor() > 300 or pacmen[count].ycor() < -300:
            pacmen[count].right(180)
            pacmen[count].forward(60)

        pacmen[count].forward(0.5)


# keyboard binding
turtle.listen()
turtle.onkey(turnleft, "Left")
turtle.onkey(turnright, "Right")
turtle.onkey(forward, "Up")
turtle.onkey(back, "Down")

while True:
    player.forward(speed)

    # boundary checking
    # chekcs if player is outside of boarder
    if player.xcor() > 300 or player.xcor() < -300:
        player.right(180)
        player.forward(60)
    if player.ycor() > 300 or player.ycor() < -300:
        player.right(180)
        player.forward(60)

    # collision checking
    for count in range(maxGoals):  # checks if player hits pacmen and resets
        if isCollision(player, goals[count]):
            player.setposition(-270, -270)
            win1 = 0
            win2 = 0
            goals1 = 0
            for count in range(maxGoals):
                paca = random.randint(0, 9)
                pacb = random.randint(0, 9)
                goals[count].setposition(pacxcor[paca], pacycor[pacb])
            for count in range(maxpacmen):
                paca = random.randint(0, 9)
                pacb = random.randint(0, 9)
                pacmen[count].setposition(pacxcor[paca], pacycor[pacb])
                pacmen[count].hideturtle()
            coin2.hideturtle()
            coin.showturtle()
    if isCollision(player, coin):  # checks if player collects coin1

        coin.hideturtle()
        coin2.showturtle()
        win1 = 1
        goals1 = 1
    if goals1 == 1:  # checks if player has collected coin1 and if so moves pacmen
        goalsMove()
    if goals2 == 1:  # checks if player has collected coin2 and if so spawns and moves more pacmen
        pacmen2Move()
    if isCollision(player, coin2):  # checks if player collects coin2
        if win1 == 1:

            coin2.hideturtle()
            for count in range(maxpacmen):
                pacmen[count].showturtle()
            pacmen2 = 1
            goals2 = 1
            win2 = 1
    if pacmen2 == 1:  # spawns second group of pacmen after collection coin2
        for count in range(maxpacmen):
            if isCollision(player, pacmen[count]):  # checks if player hits pacmen and resets game if so
                player.setposition(-270, -270)
                win1 = 0
                win2 = 0
                goals1 = 0
                for count in range(maxGoals):
                    paca = random.randint(0, 9)
                    pacb = random.randint(0, 9)
                    goals[count].setposition(pacxcor[paca], pacycor[pacb])
                for count in range(maxpacmen):
                    paca = random.randint(0, 9)
                    pacb = random.randint(0, 9)
                    pacmen[count].setposition(pacxcor[paca], pacycor[pacb])
                    pacmen[count].hideturtle()
                coin2.hideturtle()
                coin.showturtle()
                pacmen2 = 0

    if isCollision(player, finish):  # checks if player is a finishline and has collected coin1 and coin2
        win()
        break

turtle.done()

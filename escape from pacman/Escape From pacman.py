#turtple graphics game
import turtle
import math
import random
from time import sleep
from pip._vendor.distlib.compat import raw_input
#screen set up


wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.bgpic("backgound2.gif")
wn.tracer(100)
wn.register_shape("pacman.gif")
wn.register_shape("coin.gif")
#draw border
mypen = turtle.Turtle()
mypen.penup()
mypen.speed(0)
mypen.setposition(-300,-300)
mypen.pendown()
mypen.pensize(3)
for side in range(4):
    mypen.forward(600)
    mypen.left(90)
#draw grid
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

#ship random possitions
shipxcor = [-270,-210,-150,-90,-30,30,90,150,210,270]
shipycor = [-270,-210,-150,-90,-30,30,90,150,210,270]
#the player
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(-270,-270)
#coin1
coin = turtle.Turtle()
coin.shape("coin.gif")
coin.penup()
coin.speed(0)
coin.setposition(270,-270)

#coin2

coin2 = turtle.Turtle()
coin2.shape("coin.gif")
coin2.penup()
coin2.speed(0)
coin2.setposition(270,270)
coin2.hideturtle()

#finishline
finish = turtle.Turtle()
finish.shape("square")
finish.color("blue")
finish.penup()
finish.speed(0)
finish.setposition(-270,270)

#create goals
maxGoals = 6
goals = []
for count in range (maxGoals):
    goals.append(turtle.Turtle())
    goals[count].penup()
    goals[count].color("red")
    goals[count].shape("pacman.gif")
    goals[count].speed(0)
    shipa = random.randint(0,9)
    shipb = random.randint(0,9)
    if shipa == 0 and shipb == 0:
        shipb = random.randint(0,9)
    if shipa == 9 and shipb == 0:
        shipb = random.randint(0,9)
    goals[count].setposition(shipxcor[shipa], shipycor[shipb])
    goals[count].showturtle()
#set speed
speed = 0

#define Functions
win1 = 0
win2 = 0
win3 = 0
def win():
    if win1 == 1 and win2 == 1:
        print("YOU HAVE ESCAPED FROM PACMAN")
        sleep(1000)
def turnleft(): #turn left
    player.left(90)
def turnright(): #turn right
    player.right(90)
def increasespeed(): #speedup
    player.forward(60)
def back(): #drop bomb
    player.forward(-60)
def isCollision(t1, t2): #collision checking
    d = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if d < 20:
        return True
    else:
        return False




            #newshipx = random.randint(0,9)
            #newshipy = random.randint(0, 9)
            #goals[count].setposition(shipxcor[newshipx], shipycor[newshipy])

#keyboard binding
turtle.listen()
turtle.onkey(turnleft, "Left")
turtle.onkey(turnright, "Right")
turtle.onkey(increasespeed, "Up")
turtle.onkey(back,"Down")

while True:
    player.forward(speed)

    #boundary checking

    if player.xcor() > 300 or player.xcor() < -300:
        player.right(180)
        player.forward(60)
    if player.ycor() > 300 or player.ycor() < -300:
        player.right(180)
        player.forward(60)

    #collision checking
    for count in range(maxGoals):
        if isCollision(player, goals[count]):
            player.setposition(-270,-270)
    if isCollision(player, coin):
        coin.hideturtle()
        coin2.showturtle()
        win1 = 1
    if isCollision(player, coin2):
        coin2.hideturtle()
        win2 = 1
    if isCollision(player, finish):
        win()

delay = raw_input("press enter to end it")

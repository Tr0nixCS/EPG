# turtple graphics game
import turtle
import math
import random
from time import sleep

# screen set up
wn = turtle.Screen()
wn.bgcolor("lightgreen") #background color
wn.bgpic("backgound2.gif") #background pic
wn.tracer(70) #makes it draw grid and everything faster so you don't have to wait so long
wn.register_shape("pacman.gif") #pacmen pic
wn.register_shape("coin.gif") # coin pic
# draw border
mypen = turtle.Turtle()
mypen.penup()
mypen.speed(0)
mypen.setposition(-300, -300)
mypen.pendown()
mypen.pensize(3)
for side in range(4): #loop that draws the big squar
    mypen.forward(600)
    mypen.left(90)
# draw grid
mypen.forward(60)
for i in range(10): #loop that makes a grid
    for i in range(10): #loop that makes makes a line of boxes
        for squar in range(4): #loop that makes a box
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
coin.setposition(270, -270) #set coin 1 possition

# coin2
coin2 = turtle.Turtle()
coin2.shape("coin.gif")
coin2.penup()
coin2.speed(0)
coin2.setposition(270, 270) #set coin 2 possition
coin2.hideturtle()

# finishline
finish = turtle.Turtle()
finish.shape("square")
finish.color("blue")
finish.penup()
finish.speed(0)
finish.setposition(-270, 270) #set finifhline possition

# win conditions
win1 = 0
win2 = 0
win3 = 0

# increase dificulty
goals1 = 0
goals2 = 0
pacmen2 = 0

# create pacmen
maxGoals = 6 # set the amount of pacmen we want to deal with
goals = []
for count in range(maxGoals): #small loop that creats amount of pacmen equal to maxgoals
    turning = [90, 180, 270, 360] #random direction for the pacmen
    randompick = random.randint(0, 3)
    goals.append(turtle.Turtle())
    goals[count].penup()
    goals[count].color("red")
    goals[count].shape("pacman.gif") # custom shape for them
    goals[count].speed(0)
    paca = random.randint(0, 9) #picks a random x cordinat that the pacmen are spawned in
    pacb = random.randint(0, 9) #picks a random y cordinat that the pacmen are spawned in
    if paca == 0 and pacb == 0: #makes it so that the pacmen can't spawn on the player or the first coin
        pacb = random.randint(0, 9)
    if paca == 9 and pacb == 0:
        pacb = random.randint(0, 9)
    goals[count].setposition(pacxcor[paca], pacycor[pacb])
    goals[count].right(turning[randompick])
    goals[count].showturtle()

#creates more pacmen to be spawned in when the second coin is pick up
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
    pacmen[count].hideturtle() #hides the second pacmen so that you don't see them
#set speed
speed = 0


# define Functions
def win(): #win condition you have to have both coins
    if win1 == 1 and win2 == 1:
        print("YOU HAVE ESCAPED FROM PACMAN")



def turnleft():  # turn left
    player.setheading(180) #turns the player toward the left side and moves one square
    player.forward(60)


def turnright():  # turn right
    player.setheading(0) #turns the player toward the right side and moves one square
    player.forward(60)

def forward():  # speedup
    player.setheading(90) #turns the player towards north side and moves one square
    player.forward(60)


def back():  # drop bomb
    player.setheading(270) #turns the player towrds south side and moves one square
    player.forward(60)


def isCollision(t1, t2):  # collision checking
    #checks
    d = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if d < 15:
        return True
    else:
        return False


def goalsMove():  # pacmen movement
    for count in range(maxGoals):
        #set up boundary for the pacmen so they don't go outside of the screen
        if goals[count].xcor() > 300 or goals[count].xcor() < -300:
            goals[count].right(180)
            goals[count].forward(60)
        if goals[count].ycor() > 300 or goals[count].ycor() < -300:
            goals[count].right(180)
            goals[count].forward(60)
        # all pacmen move forward a 0.5 speed
        goals[count].forward(0.5)


def pacmen2Move():  # pacmen2 movement
    for count in range(maxpacmen):
        #does the same for second set of pacmen
        if pacmen[count].xcor() > 300 or pacmen[count].xcor() < -300:
            pacmen[count].right(180)
            pacmen[count].forward(60)
        if pacmen[count].ycor() > 300 or pacmen[count].ycor() < -300:
            pacmen[count].right(180)
            pacmen[count].forward(60)

        pacmen[count].forward(0.5)


# keyboard binding
turtle.listen()
turtle.onkey(turnleft, "Left") #when left arrow key is pressed moves left
turtle.onkey(turnright, "Right") #when right arrow key is pressed moves right
turtle.onkey(forward, "Up") #when up arrow key is pressed moves up
turtle.onkey(back, "Down") #when left down key is pressed moves down

while True: #the start of the game
    player.forward(speed) #makes it so the player doesn't move

    # chekcs if player is outside of boarder and moves back in if so same as for the pacmen
    if player.xcor() > 300 or player.xcor() < -300:
        player.right(180)
        player.forward(60)
    if player.ycor() > 300 or player.ycor() < -300:
        player.right(180)
        player.forward(60)

    # collision checking
    for count in range(maxGoals):  # checks if player hits pacmen and resets
        if isCollision(player, goals[count]): #checks if the player has touched any of the goals
            player.setposition(-270, -270) #sets the player back to start and resets the game
            win1 = 0
            win2 = 0
            goals1 = 0
            for count in range(maxGoals): #reposition all the pacmen
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
        if win1 == 1: #checks if player has collected the first coin if not nothing happens
            coin2.hideturtle() #hides the coin
            for count in range(maxpacmen):
                pacmen[count].showturtle() #show the new pacmen
            pacmen2 = 1 #new pacmen move
            goals2 = 1
            win2 = 1 #you have collected the seconed coin
    if pacmen2 == 1:  # spawns second group of pacmen after collection coin2
        #also makes it so player can't hit the extra pacmen before they are spawned
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
        exit()

#Her her vi vores biblioteker som vi har importet
import time
from random import randint
import os
import msvcrt
import turtle

#Her har vi vores variabler som vi har defineret

x_colon = 11
y_colon = 11
ships_amount = 5
max_ship_size = 5
min_ship_size = 2

Ashe_y = 0 #Spiller 1 hedder Bob (BOT)
Ashe_x = 0 #Spiller 2 hedder Ashe (SPILLER)

def movement_Ashe(): #Vores spiller bevægelser
    while True:
        key = msvcrt.getch()
        if key == b'a':
            Ashe_x-=3  #Ashe_x bevæger sig 3X mod venstre
        elif key == b'd':
            Ashe_x+=3  #Ashe_x bevæger sig 3X mod højre
        elif key == b'w':
            Ashe_y-=1  #Ashe_y bevæger sig 1Y opad
        elif key == b's':
            Ashe_y+=1  #Ashe_y bevæger sig 1Y nedad

os.system('cls')
for i in range(Ashe_y):
    print(" ")
for i in range(Ashe_x):
    print(" " ,end='')
print("=",flush=True,end='')


def ship_2():

def ship_3():

def ship_4():


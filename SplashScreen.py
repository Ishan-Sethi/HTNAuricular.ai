from tkinter import *
import random
import time
from tkinter import Tk, Canvas, Frame, BOTH, W
import math
tk = Tk()

Height = 500
Width = 800

canvas = Canvas (tk, width = Width, height = Height)

x = 165
y = -110
a = 550
m = -510
counter = 0
tk.title ("SplashScreen")
canvas.pack()

#lineaz = canvas.create_line(10, 10, 100, 100)
xspeed = 1 #movement variable x assignment
yspeed = 1 #movement variable y assignment

xdspeed = 1 #movement variable x due

title = canvas.create_text(x, y, anchor=W, font= ("Hp Simplified", 75), text = "Auricular.AI")

while True:

    print(m)
    if counter < 324:
        counter+=1
        y+=1
        canvas.move(title,0,yspeed) #Adds to the coordinates of line
    elif counter >= 324 and counter <= 590:
        counter+=1
        canvas.create_rectangle(-10, a, 800, a + 300, outline = "#add8e6", fill = "#add8e6")
        a-=1
    elif counter >= 590:
        canvas.create_rectangle(-10, m, 810, m+500, outline = "#059DC0", fill = "#059DC0")
        m+=5
        counter+=1


    tk.update() #update position of line
    time.sleep(0.01) #Rate of change

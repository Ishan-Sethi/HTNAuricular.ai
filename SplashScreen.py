from tkinter import *
import random
import time
from tkinter import Tk, Canvas, Frame, BOTH, W
import math
import random

def cubicInterpolate(y1, y2, mu):
   mu2 = (1-math.cos(mu*3.14))/2;
   return(y1*(1-mu2)+y2*mu2);

tk = Tk()

Height = 500
Width = 800

canvas = Canvas (tk, width = Width, height = Height)
x = 165
y = -110
a = 550
m = -510
siy=0
six=0

num = 0

counter = 0
tk.title ("SplashScreen")
canvas.pack()

#lineaz = canvas.create_line(10, 10, 100, 100)
xspeed = 1 #movement variable x assignment
yspeed = 1 #movement variable y assignment

xdspeed = 1 #movement variable x due

title = canvas.create_text(x, y, anchor=W, font= ("Hp Simplified", 75), text = "Auricular.AI")

randompoints = []
for i in range(10):
    randompoints.append(random.randint(0, 10))

while True:

    counter+=1



    six+=1
    siy = 20*math.sin(six)
    canvas.create_line(six, 250- siy, six, 250+siy, width =  1)




    tk.update() #update position of line
    time.sleep(0.01) #Rate of change

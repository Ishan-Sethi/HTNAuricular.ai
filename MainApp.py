import random
import time
import math
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from ttkthemes import ThemedStyle
import fileManager as fm
from fileManager import *

# helper to turn rgb to hex
def rgb_to_hex(r,g,b):
    return "#" + format(r,'02x') + format(g,'02x') + format(b,'02x')
# grayscale color to hex
def mono_to_hex(m):
    return "#" + format(m,'02x') + format(m,'02x') + format(m,'02x')
# smooth interpolation
def cosineInterpolate(y1, y2, mu):
   mu2 = (1-math.cos(mu*3.14)) / 2;
   return (y1*(1-mu2) + y2*mu2);

# Class to extend when making new frames for MainApp
class BasicFrame(ttk.Frame):
    def __init__(self, master, parent):
        tk.Frame.__init__(self, master)
        self.parent = parent
        self.configure(background='#f5f6f7')
        self.create_widgets()
        pass
    # Supply this with widgets to add
    def create_widgets(self):
        raise NotImplementedError("Implement this create_widgets(), bumboclat! %s" %(self.__class__.__name__))
    def hide_window(self):
        self.pack_forget()
        pass
    # Supply this with proper pack method
    def show_window(self):
        raise NotImplementedError("Implement this show_window(), bumboclat! %s" %(self.__class__.__name__))

# Splashscreen for program open
class SplashFrame(BasicFrame):

    def create_widgets(self):
        self.canvas = tk.Canvas(self, width=800, height=500)
        self.canvas.pack()
        print("function has run create")
        pass

    def reset_animation(self):
        self.counter = 0 #delta but never changes
        self.x, self.y, self.fontsize, self.titleColor = 400, 250, 45, 255
        self.a, self.m = 500, 0

        self.sinx, self.siny, self.index = 0, 0, 0
        self.randompoints = []
        self.randompoints.append(0)
        for i in range(100):
            self.randompoints.append(random.randint(0, 50))

        self.title = self.canvas.create_text(self.x, self.y, font=("TkMenuFont",self.fontsize), text="Auricular.AI", fill='#FFFFFF')
        self.oldRect = self.canvas.create_rectangle(0, self.m, 800, 0, outline="#f5f6f7", fill="#f5f6f7")

        print("function has run")
        pass

    def run_animation(self):
        print(self.counter)

        #Sinusoidal wave drawing
        self.counter+=1

        if self.counter % 50 == 0:
            self.index+=1

        if self.counter%2==0:
            self.sinx+=2
            self.siny = cosineInterpolate(self.randompoints[self.index], self.randompoints[self.index+1], (self.counter%50)/50)*math.sin(self.sinx)
            self.canvas.create_line(self.sinx, 250-self.siny, self.sinx, 250+self.siny, width=2, fill=rgb_to_hex(160,160,255))

        if self.counter < 300:
            self.fontsize = self.fontsize+0.25  if self.fontsize<75 else self.fontsize
            self.titleColor = self.titleColor-1 if self.titleColor>0 else self.titleColor
        self.newTitle = self.canvas.create_text(self.x, self.y, font=("TkMenuFont",int(self.fontsize)), text="Auricular.AI", fill=mono_to_hex(self.titleColor))
        self.canvas.delete(self.title)
        self.title = self.newTitle

        if self.counter >= 300 and self.counter < 450:
            self.a-=1
            self.canvas.create_line(0, self.a, 800, self.a, width=2, fill="#add8e6")
            self.canvas.create_line(0, 500-self.a, 800, 500-self.a, width=2, fill="#add8e6")
        elif self.counter >= 600 and self.counter < 700:
            self.m+=5
            self.newRect = self.canvas.create_rectangle(0, self.m, 800, 0, outline="#f5f6f7", fill="#f5f6f7")
            self.canvas.delete(self.oldRect)
            self.oldRect = self.newRect
        if self.counter == 700:
            self.hide_window()
            self.parent.mainFrame.show_window()
        else:
            self.master.after(5, self.run_animation)
        pass
    def show_window(self):
        self.pack(side="top", fill="both", ipadx=30, ipady=30, expand=True)
        pass

# Add cleaner visuals?
class MainFrame(BasicFrame):
    def create_widgets(self):
        self.heading = ttk.Label(self, text="Auricular.ai", style="heading.TLabel")
        self.heading.pack(side="top", pady=(80,30))
        self.record = ttk.Button(self, text="Process Recording", width=25, style="main.TButton", command=self.get_file_location)
        self.record.pack(side="top", pady=(50,0))
        self.note = ttk.Button(self, text="Notes", width=25, style="main.TButton", command=lambda:[self.hide_window(),self.parent.notesFrame.show_window()])
        self.note.pack(side="top", pady=(30,0))
        self.quit = ttk.Button(self, text="Quit Program", width=25, style="main.TButton", command=self.parent.root.destroy)
        self.quit.pack(side="top", pady=(30,0))
        pass

    def get_file_location(self):
        filedialog.askopenfilename(filetypes=[("Audio files", ".wav")])

    def show_window(self):
        self.pack(side="top", fill="both", ipadx=30, ipady=30, expand=True)
        pass

# Loading while waiting for backend to work
class LoadingFrame(BasicFrame):
    def create_widgets(self):
        pass

    def show_window(self):
        self.pack(side="top", fill="both", ipadx=30, ipady=30, expand=True)
        pass

# Screen to show what happened and stuff
class OutputFrame(BasicFrame):
    def create_widgets(self):
        pass

    def show_window(self):
        self.pack(side="top", fill="both", ipadx=30, ipady=30, expand=True)
        pass

# Show all saved notes and open em up
class NotesFrame(BasicFrame):
    def create_widgets(self):
        self.back = ttk.Button(self, text="Back", width=25, command=lambda:[self.hide_window(),self.parent.mainFrame.show_window()])
        self.back.pack(side="bottom", pady=(0,100))
        pass

    def show_window(self):
        self.pack(side="top", fill="both", ipadx=30, ipady=30, expand=True)
        pass

# Main Window Class
class MainApp(object):
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Auricular.ai")
        self.root.geometry("800x500")
        self.root.resizable(0, 0)

        self.style = ThemedStyle(self.root)
        self.style.set_theme("arc")

        self.ttkstyle = ttk.Style()
        self.ttkstyle.configure('heading.TLabel', font='TkDefaultFont 48')
        self.ttkstyle.configure('main.TButton', font='TkMenuFont 18')

        self.splashFrame = SplashFrame(self.root, self)
        self.mainFrame = MainFrame(self.root, self)
        self.notesFrame = NotesFrame(self.root, self)

        self.splashFrame.show_window()
        self.splashFrame.reset_animation()
        self.splashFrame.run_animation()
        pass

mainApp = MainApp()
mainApp.root.mainloop()

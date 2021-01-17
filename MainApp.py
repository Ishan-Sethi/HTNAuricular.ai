import random
import time
import math
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from ttkthemes import ThemedStyle
import fileManager as fm
from fileManager import *

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

# Aryan complete this
class SplashFrame(BasicFrame):

    def create_widgets(self):
        self.canvas = tk.Canvas(self, width=800, height=500)
        self.canvas.pack()
        print("function has run create")
        pass
    def reset_animation(self):
        self.counter = 0 #delta but never changes
        self.x, self.y, self.a, self.m = 145, -110, 550, -510
        self.xspeed, self.yspeed = 1, 1 #movement variable x and y
        self.title = self.canvas.create_text(self.x, self.y, anchor='w', font=("TkMenuFont",75), text="Auricular.AI")
        print("function has run")
        pass
    def run_animation(self):
        print(self.counter)
        self.counter+=1
        if self.counter < 324:
            self.y+=1
            self.canvas.move(self.title,0,self.yspeed) #Adds to the coordinates of line
        elif self.counter >= 324 and self.counter <= 590:
            self.a-=1
            self.canvas.create_rectangle(-10, self.a, 800, self.a+300, outline = "#add8e6", fill = "#add8e6")
        elif self.counter >= 590 and self.counter <= 692:
            self.m+=5
            self.canvas.create_rectangle(-10, self.m, 810, self.m+500, outline = "#f5f6f7", fill = "#f5f6f7")
        if self.counter == 693:
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
        self.heading.pack(side="top", pady=(0,50), ipady=(20,0))
        self.record = ttk.Button(self, text="Process Recording", width=25, command=self.get_file_location)
        self.record.pack(side="top", pady=(50,0))
        self.note = ttk.Button(self, text="Notes", width=25, command=lambda:[self.hide_window(),self.parent.notesFrame.show_window()])
        self.note.pack(side="top", pady=(30,0))
        self.quit = ttk.Button(self, text="Quit Program", width=25, command=self.parent.root.destroy)
        self.quit.pack(side="top", pady=(30,0))
        pass

    def get_file_location(self):
        print(filedialog.askopenfilename(filetypes=[("Image files", ".png .jpg .jpeg")]))

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
        self.ttkstyle.configure('heading.TLabel', font='TkDefaultFont 32')

        self.splashFrame = SplashFrame(self.root, self)
        self.mainFrame = MainFrame(self.root, self)
        self.notesFrame = NotesFrame(self.root, self)

        self.splashFrame.show_window()
        self.splashFrame.reset_animation()
        self.splashFrame.run_animation()
        pass

mainApp = MainApp()
mainApp.root.mainloop()

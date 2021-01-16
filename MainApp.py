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
    def hideWindow(self):
        self.pack_forget()
        pass
    # Supply this with proper pack method
    def showWindow(self):
        raise NotImplementedError("Implement this showWindow(), bumboclat! %s" %(self.__class__.__name__))

# Aryan complete this
class SplashFrame(BasicFrame):
    def create_widgets(self):
        self.back = ttk.Button(self, text="Back", width=25, command=lambda:[self.hideWindow(),self.parent.mainFrame.showWindow()])
        self.back.pack(side="bottom", pady=(0,100))
        pass

    def showWindow(self):
        self.pack(side="top", fill="both", ipadx=30, ipady=30, expand=True)
        pass

# Add cleaner visuals?
class MainFrame(BasicFrame):
    def create_widgets(self):
        self.heading = ttk.Label(self, text="Auricular.ai", style="heading.TLabel")
        self.heading.pack(side="top", pady=(20,0))
        self.record = ttk.Button(self, text="Process Recording", width=25, command=self.getFileLocation)
        self.record.pack(side="top", pady=(50,0))
        self.note = ttk.Button(self, text="Notes", width=25, command=lambda:[self.hideWindow(),self.parent.notesFrame.showWindow()])
        self.note.pack(side="top", pady=(30,0))
        self.quit = ttk.Button(self, text="Quit Program", width=25, command=self.parent.root.destroy)
        self.quit.pack(side="top", pady=(30,0))
        pass

    def getFileLocation(self):
        print(filedialog.askopenfilename(filetypes=[("Image files", ".png .jpg .jpeg")]))

    def showWindow(self):
        self.pack(side="top", fill="both", ipadx=30, ipady=30, expand=True)
        pass

# Loading while waiting for backend to work
class LoadingFrame(BasicFrame):
    def create_widgets(self):
        pass

    def showWindow(self):
        self.pack(side="top", fill="both", ipadx=30, ipady=30, expand=True)
        pass

# Screen to show what happened and stuff
class OutputFrame(BasicFrame):
    def create_widgets(self):
        pass

    def showWindow(self):
        self.pack(side="top", fill="both", ipadx=30, ipady=30, expand=True)
        pass

# Show all saved notes and open em up
class NotesFrame(BasicFrame):
    def create_widgets(self):
        self.back = ttk.Button(self, text="Back", width=25, command=lambda:[self.hideWindow(),self.parent.mainFrame.showWindow()])
        self.back.pack(side="bottom", pady=(0,100))
        pass

    def showWindow(self):
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

        self.mainFrame = MainFrame(self.root, self)
        self.notesFrame = NotesFrame(self.root, self)

        self.mainFrame.showWindow()
        pass

mainApp = MainApp()
mainApp.root.mainloop()

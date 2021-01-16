import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from ttkthemes import ThemedStyle

class BasicFrame(ttk.Frame):
    def __init__(self, master, parent):
        tk.Frame.__init__(self, master)
        self.parent = parent
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

class MainFrame(BasicFrame):
    def create_widgets(self):
        self.hi_there = ttk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")
        self.quit = ttk.Button(self, text="QUIT", width=30, command=lambda:[self.hideWindow(),self.parent.mainFrame2.showWindow()])
        self.quit.pack(side="bottom")
        pass
    def say_hi(self):
        print("hi there, everyone!")
        pass
    def showWindow(self):
        self.pack(side="top", fill="both", ipadx=30, ipady=30, padx=10, pady=10, expand=True)
        pass

class MainFrameTwo(BasicFrame):
    def create_widgets(self):
        self.racism = ttk.Label(self, text="china", width=20)
        self.racism.pack(side="top")
        pass
    def showWindow(self):
        self.pack(side="top", fill="both", padx=100, pady=100, expand=True)
        pass

# Main Window Class
class MainApp(object):
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("gay program")
        self.root.geometry("800x500")
        self.root.resizable(0, 0)

        self.style = ThemedStyle(self.root)
        self.style.set_theme("adapta")

        self.mainFrame = MainFrame(self.root, self)
        self.mainFrame2 = MainFrameTwo(self.root, self)

        self.mainFrame.showWindow()
        pass

mainApp = MainApp()
mainApp.root.mainloop()

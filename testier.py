import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from ttkthemes import ThemedStyle

# MainFrame class to play around with
# self.parent - MainApp variable
class MainFrame(tk.Frame):
    def __init__(self, master, parent):
        tk.Frame.__init__(self, master)
        self.parent = parent
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = ttk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = ttk.Button(self, text="QUIT", width=30, command=lambda:[self.hideWindow(),self.parent.mainFrame2.showWindow()])
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

    def hideWindow(self):
        self.pack_forget()
    def showWindow(self):
        self.pack(side="top", fill="both", ipadx=30, ipady=30, padx=10, pady=10, expand=True)
class MainFrameTwo(tk.Frame):
    def __init__(self, master, parent):
        tk.Frame.__init__(self, master)
        self.parent = parent
        self.create_widgets()

    def create_widgets(self):
        self.racism = ttk.Label(self, text="china", width=20)
        self.racism.pack(side="top")

    def say_hi(self):
        print("hi there, everyone!")

    def hideWindow(self):
        self.pack_forget()
    def showWindow(self):
        self.pack(side="top", fill="both", padx=100, pady=100, expand=True)

# Main Window Class
class MainApp(object):
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("gay program")
        self.root.geometry("800x500")
        self.root.resizable(0, 0)

        self.style = ThemedStyle(self.root)
        self.style.set_theme("yaru")

        self.mainFrame = MainFrame(self.root, self)
        self.mainFrame2 = MainFrameTwo(self.root, self)

        self.mainFrame.showWindow()

mainApp = MainApp()
mainApp.root.mainloop()

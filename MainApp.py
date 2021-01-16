import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from ttkthemes import ThemedStyle

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

class MainFrame(BasicFrame):
    def create_widgets(self):
        self.heading = ttk.Label(self, text="Auricular.ai", style="heading.TLabel")
        self.heading.pack(side="top", pady=(10,0))
        self.addFile = ttk.Button(self, text="Process Recording", width=25, command=self.getFileLocation)
        self.addFile.pack(side="top", pady=(50,0))
        self.addFile = ttk.Button(self, text="Notes", width=25)
        self.addFile.pack(side="top", pady=(30,0))
        self.addFile = ttk.Button(self, text="Quit Program", width=25, command=self.parent.root.destroy)
        self.addFile.pack(side="top", pady=(30,0))
        pass

    def getFileLocation(self):
        print(filedialog.askopenfilename(filetypes=[("Image files", ".png .jpg .jpeg")]))

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
        self.style.set_theme("arc")

        self.ttkstyle = ttk.Style()
        self.ttkstyle.configure('heading.TLabel', font='TkDefaultFont 32')

        self.mainFrame = MainFrame(self.root, self)
        self.mainFrame2 = MainFrameTwo(self.root, self)

        self.mainFrame.showWindow()
        pass

mainApp = MainApp()
mainApp.root.mainloop()

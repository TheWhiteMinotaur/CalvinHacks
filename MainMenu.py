import pygame
from tkinter import *
from tkinter.ttk import *


class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()
        self.master.title("The Fall of Bobs")

    def Close(self):
        exit()

    def Multiplayer(self):
        New_Window = Tk()
        New_Window.mainloop()

    def Singleplayer(self):
        New_Window = Tk()
        New_Window.mainloop()

    #Creation of init_window
    def init_window(self):

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # creating a button instance
        multButton = Button(self, text="Multiplayer", command =self.Multiplayer)
        singButton = Button(self, text="Singleplayer", command = self.Singleplayer)

        label = Label(self, command=self.showText())
        label.config(width=200)
        label.config(font=("Courier", 30))

        # placing the button on my window
        multButton.place(x=500, y=250)
        singButton.place(x=400, y=250)
        root.resizable(False, False)

    def showText(self):
        text = Label(self, text="Dungeon Maze")
        text.pack()

root = Tk()
root.geometry("1000x500")
app = Window(root)
root.mainloop()

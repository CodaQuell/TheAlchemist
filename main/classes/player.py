from classes.playerClass import *
import tkinter

app = tkinter.Tk()
W = app.winfo_screenwidth()
H = app.winfo_screenheight()

#init player from Player class
player = Player(H,W)
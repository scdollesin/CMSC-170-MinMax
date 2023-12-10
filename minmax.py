from tkinter import *
import tkinter as tk

#user = int(input("Which would you like to play as?\n[0] O\n[1] X\n> "))
user = input("X or O: ")
buttons = [['','',''],
           ['','',''],
           ['','','']]

window = Tk()
window.title("Tic Tac Toe")
board = Frame(window).grid(row=0, column=0)

def modify(r, c):
    buttons[r][c].config(text=user, fg='blue')
    buttons[r][c].grid(row=r, column=c)

for r in range(3):
    for c in range(3):
        buttons[r][c] = Button(board, text=buttons[r][c], font=('Cocogoose', 60), width=3, height=1, command= lambda row=r, col=c: modify(row, col))
        buttons[r][c].grid(row=r, column=c)

window.mainloop()
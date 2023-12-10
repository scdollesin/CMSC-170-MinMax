from tkinter import *
import tkinter as tk

#user = int(input("Which would you like to play as?\n[0] O\n[1] X\n> "))
#user = input("X or O: ")
user = "X"
buttons = [['','',''],
           ['','',''],
           ['','','']]
state = [['','',''],
         ['','',''],
         ['','','']]

window = Tk()
window.title("Tic Tac Toe")
board = Frame(window).grid(row=0, column=0)


def check():
    win = False
    #check rows
    for r in state:
        if all(e != '' and e == r[0] for e in r): win = True
    #check columns
    for c in range(3):
        col = []
        for r in range(3):
            col.append(state[r][c])
        if all(e != '' and e == col[0] for e in col): win = True
    #check both diagonals
    diagonal = [state[0][0],state[1][1], state[2][2]]
    if all(e != '' and e == diagonal[0] for e in diagonal): win = True
    diagonal = [state[0][2],state[1][1], state[2][0]]
    if all(e != '' and e == diagonal[0] for e in diagonal): win = True
    print(f"win = {win}")

def update(r, c):
    buttons[r][c].config(text=user, fg='blue')
    buttons[r][c].grid(row=r, column=c)
    state[r][c] = user
    print(state)
    check()

for r in range(3):
    for c in range(3):
        buttons[r][c] = Button(board, text=buttons[r][c], font=('Cocogoose', 60), width=3, height=1, command= lambda row=r, col=c: update(row, col))
        buttons[r][c].grid(row=r, column=c)

window.mainloop()
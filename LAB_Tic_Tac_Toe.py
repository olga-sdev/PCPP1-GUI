"""
Objectives
Learn practical skills related to:

dealing with the grid geometry manager,
defining and using callbacks,
identifying and servicing GUI events.

Scenario
Write a GUI program which pretends to play tic-tac-toe with the user.

To make your task a bit easier, let's simplify the game a bit.

There are our assumptions:
the computer (i.e., your program) plays 'X', and Xes are always red,
the user (e.g., you) plays 'O', and Os are always green,
the board consists of 9 tiles, and the tile role is played by a button,
the first move belongs to the computer - it always puts its first 'X' in the middle of the board,
the user enters her/his move by clicking the chosen tile (clicking the tiles which are not free is ineffective)
the program checks if the game over conditions are met, and if the game is over, a message box is displayed announcing the winner,
otherwise the computer responds with its move and the check is repeated,
use random to generate the computer's moves.
"""
import random
import tkinter as tk
from tkinter import messagebox


wnd = tk.Tk()
wnd.title("TicTacToe")

buttons = []


def change_name(node):
    global indexes
    if node not in indexes:
        buttons[node].config(text='O', fg='green', font=('Arial', '20', 'bold'))
        indexes.append(node)
        x_step()
        winner()


def x_step():
    global indexes
    random_index = random.randint(0, 8)
    print(f'random: {random_index}')
    if random_index not in indexes:
        buttons[random_index].config(text='X', fg='red', font=('Arial', '20', 'bold'))
        indexes.append(random_index)
    else:
        x_step()


def winner():
    if (buttons[0]['text'] == 'O' and buttons[1]['text'] == 'O' and buttons[2]['text'] == 'O') or \
            (buttons[3]['text'] == 'O' and buttons[4]['text'] == 'O' and buttons[5]['text'] == 'O') or \
            (buttons[6]['text'] == 'O' and buttons[7]['text'] == 'O' and buttons[8]['text'] == 'O') or \
            (buttons[0]['text'] == 'O' and buttons[4]['text'] == 'O' and buttons[8]['text'] == 'O') or \
            (buttons[2]['text'] == 'O' and buttons[4]['text'] == 'O' and buttons[6]['text'] == 'O') or \
            (buttons[0]['text'] == 'O' and buttons[3]['text'] == 'O' and buttons[6]['text'] == 'O') or \
            (buttons[1]['text'] == 'O' and buttons[4]['text'] == 'O' and buttons[7]['text'] == 'O') or \
            (buttons[2]['text'] == 'O' and buttons[5]['text'] == 'O' and buttons[8]['text'] == 'O'):
        messagebox.showinfo('Game over', 'You won!')
    elif (buttons[0]['text'] == 'X' and buttons[1]['text'] == 'X' and buttons[2]['text'] == 'X') or \
            (buttons[3]['text'] == 'X' and buttons[4]['text'] == 'X' and buttons[5]['text'] == 'X') or \
            (buttons[6]['text'] == 'X' and buttons[7]['text'] == 'X' and buttons[8]['text'] == 'X') or \
            (buttons[0]['text'] == 'X' and buttons[4]['text'] == 'X' and buttons[8]['text'] == 'X') or \
            (buttons[2]['text'] == 'X' and buttons[4]['text'] == 'X' and buttons[6]['text'] == 'X') or \
            (buttons[0]['text'] == 'X' and buttons[3]['text'] == 'X' and buttons[6]['text'] == 'X') or \
            (buttons[1]['text'] == 'X' and buttons[4]['text'] == 'X' and buttons[7]['text'] == 'X') or \
            (buttons[2]['text'] == 'X' and buttons[5]['text'] == 'X' and buttons[8]['text'] == 'X'):
        messagebox.showinfo('Game over', 'I won!')


for i in range(9):
    button = tk.Button(wnd, text='', width=5, height=2, state=tk.NORMAL, font=('Arial', '20', 'bold'),
                       command=lambda index=i: change_name(index))
    button.grid(row=i // 3, column=i % 3)
    buttons.append(button)

buttons[4].config(text='X', fg='red', font=('Arial', '20', 'bold'))
indexes = [4]

wnd.mainloop()

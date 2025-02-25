"""
unbind a callback from an event -> the widget stops reacting to the event.
bind   a callback from an event -> the widget reacts to the event.

bind and unbind -> with config()
"""


import tkinter as tk
from tkinter import messagebox


def on_off():
    global switch
    if switch:
        button.config(command=lambda: None)
        button.config(text="OFF")
    else:
        button.config(command=greeting)
        button.config(text="ON")
    switch = not switch


def greeting():
    messagebox.showinfo('ON', 'Greeting')


switch = True
widget = tk.Tk()
widget.title('Config')

var = tk.IntVar()
checkbutton = tk.Checkbutton(widget, text="ON | OFF", variable=var, command=on_off)
checkbutton.pack()

button = tk.Button(widget, text="Greeting", command=greeting)
button.pack()

widget.mainloop()

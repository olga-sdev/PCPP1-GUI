"""
unbind a callback from an event -> the widget stops reacting to the event.
bind   a callback from an event -> the widget reacts to the event.

bind and unbind -> with config()

unbind_all() -> unbind the same callback to all existed widgets
bind_all()   -> bind the same callback to all existed widgets
"""

# Example with config function
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


# Example with bind and unbind fuctions
def on_off():
    global switch
    if switch:
        text.unbind("<Button-1>")
    else:
        text.bind("<Button-1>", info_on)
    switch = not switch


def info_on(i):
    text.config(text='The switcher is ON')


switch = False

widget = tk.Tk()
node = tk.Button(widget, text="ON | OFF", command=on_off)
node.pack()

text = tk.Message(widget, text='Click here')
text.bind("<Button-1>", info_on)
text.pack()

widget.mainloop()


# Example with bindall() and unbindall()
def greet(dummy):
    messagebox.showinfo("", "greeting!")


widget = tk.Tk()

click = tk.Button(widget, text="Greeting")
click.pack()

frame = tk.Frame(widget)
frame.pack()

widget.bind_all("<Button-1>", greet)

widget.mainloop()

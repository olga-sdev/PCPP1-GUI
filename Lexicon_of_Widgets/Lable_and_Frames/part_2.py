# Example with Lable

import random
import tkinter as tk


def color():
    global text_of_color
    list_of_colors = ['red', 'green', 'blue', 'yellow', 'white']
    color_of_button = random.choice(list_of_colors)
    text_of_color.set(color_of_button)
    button['bg'] = color_of_button


widget = tk.Tk()

button = tk.Button(widget, text='Colorful Button', command=color)
button.pack()

text_of_color = tk.StringVar()
label = tk.Label(widget, textvariable=text_of_color)
label.pack()

widget.mainloop()


# Example with Message

import tkinter as tk


def subtraction():
    if text.get() <= 0:
        button.config(text='Reload App', state=tk.DISABLED, bg='pink')
    if text.get() > 0:
        text.set(text.get() - 1)


widget = tk.Tk()

button = tk.Button(widget, text='Subtract', bg='white', command=subtraction)
button.pack()

number = 6
text = tk.IntVar()
message = tk.Message(widget, textvariable=text)
text.set(number)
message.pack()

widget.mainloop()

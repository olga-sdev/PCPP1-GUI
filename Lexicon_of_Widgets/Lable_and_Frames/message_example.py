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

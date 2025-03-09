# Example with Button and Checkbutton properties

import tkinter as tk


def state_switcher():
    if button['state'] == tk.DISABLED:
        button.config(state=tk.NORMAL, bg='green')
        button.flash()
    else:
        button.config(state=tk.DISABLED, bg='pink')


widget = tk.Tk()
switch = tk.IntVar()

button = tk.Button(widget, text='Node')
button.pack()

checkbutton = tk.Checkbutton(widget, text='State Switcher', variable=switch, command=state_switcher)
checkbutton.pack()

widget.mainloop()

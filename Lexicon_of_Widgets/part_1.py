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


# Example with Button and Radiobuttons (same logic from previous example)

def enable():
    button.config(state=tk.NORMAL, bg='green')
    button.flash()
    radio_disable_var.set(radio_enable_var.get())


def disable():
    button.config(state=tk.DISABLED, bg='pink')
    radio_enable_var.set(radio_disable_var.get())


widget = tk.Tk()

button = tk.Button(widget, text='Node')
button.pack()

radio_enable_var = tk.IntVar()
radiobutton_enable = tk.Radiobutton(widget, text='Enable', variable=radio_enable_var, value=1, command=enable)
radiobutton_enable.pack()

radio_disable_var = tk.IntVar()
radiobutton_disable = tk.Radiobutton(widget, text='Disable', variable=radio_disable_var, value=2, command=disable)
radiobutton_disable.pack()
radiobutton_disable.select()

widget.mainloop()

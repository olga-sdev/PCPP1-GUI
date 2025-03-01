"""
When working with Tkinter in Python, you'll encounter a variety of widget properties (also known as options) to customize the appearance and behavior of widgets. 
Common properties:
Text Properties
Geometry Management
State and Behavior
Layout Management
Miscellaneous

Possible ways of reading and setting widget properties’ values:
* dictionary which exists inside every widget -> widget['property'] = new_value
* widget methods: cget() -> read the property’s value, config() -> set a new value to the property
"""

import tkinter as tk


# Example with dict
def switch_color(i):
    global frame
    color = frame["bg"]
    if color == "green":
        color = "blue"
    else:
        color = "green"
    frame["bg"] = color


widget = tk.Tk()

widget.title("Tkinter Frame")
widget.geometry("300x300")
frame = tk.Frame(widget, bg="green")
frame.pack(fill="both", expand=True)

widget.bind_all("<Button-1>", switch_color)
frame.mainloop()


# Example with cget() and config()
def change_color(i):
    global frame
    color = frame.cget("bg")
    if color == "orange":
        color = "grey"
    else:
        color = "orange"
    frame.config(bg=color)


widget = tk.Tk()
widget.title('Colored Frame')

widget.geometry("100x600")
frame = tk.Frame(widget, bg='orange')
frame.pack(fill='both', expand=True)

widget.bind('<Button-1>', change_color)
frame.mainloop()

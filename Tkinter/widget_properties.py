"""
When working with Tkinter in Python, you'll encounter a variety of widget properties (also known as options) to customize the appearance and behavior of widgets. 
Common properties:
Text Properties
Geometry Management
State and Behavior
Layout Management
Miscellaneous

Possible ways of reading and setting widget properties’ values:
*  dictionary which exists inside every widget -> widget['property'] = new_value
"""

import tkinter as tk


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

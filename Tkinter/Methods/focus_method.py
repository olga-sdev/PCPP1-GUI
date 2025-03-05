"""
Tkinter provides several methods for managing the focus of widgets in a GUI application:

focus() -> Set the focus to a specific widget.
focus_set() -> Similar to focus(), but ensures that the widget gets the focus even if the window is not currently focused.
focus_force() -> Forces the focus to the widget, regardless of whether the window is focused or not.
focus_get() -> Returns the widget that currently has the focus.
focus_displayof() -> Returns the widget that has the focus in the same display as the current widget.
"""
import tkinter as tk


widget = tk.Tk()


def change_focus(i):
    if node.focus_get():
        node.focus_set()
    node.focus_get()


node = tk.Button(widget, width=10, height=10, bg='green')
node.pack()

node.bind('<Enter>', change_focus)

widget.mainloop()

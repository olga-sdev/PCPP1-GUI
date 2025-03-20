"""
Restrict widget size with:
minsize -> widget's minimum size in Tkinter
maxsize -> widget's maximum size in Tkinter

Set widget Size and Position:
geometry -> widget's Size and Position

resizable -> define widget to be flexible (True) or inflexible (False)
"""

import tkinter as tk


def hover(*args):
    widget.geometry("700x700")


def unhover(*args):
    widget.geometry("250x220")


widget = tk.Tk()
widget.minsize(width=250, height=220)
widget.maxsize(widget=900, height=900)
widget.resizable(width=True, height=True)

widget.bind("<Enter>", hover)
widget.bind("<Leave>", unhover)
widget.mainloop()

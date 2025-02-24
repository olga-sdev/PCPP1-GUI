import tkinter as tk
from tkinter import messagebox


# Event handling for None and non-None events
def click(event=None):
    if event is None:
        tk.messagebox.showinfo("Click", "Click")
    else:
        string = "[x=" + str(event.x) + "; y=" + str(event.y) + "]"
        tk.messagebox.showinfo("Click", string)


widget = tk.Tk()
label = tk.Message(widget, text="Text")
label.bind("<Enter>", click)
label.pack()

button = tk.Button(widget, text="Click", command=click)
button.pack(fill=tk.X)

widget.mainloop()

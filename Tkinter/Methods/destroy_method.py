"""
In Tkinter, the destroy() method is used to close a Tkinter window.
This method used to programmatically close / destroy a window.
"""
import tkinter as tk


widget = tk.Tk()


def close_widget(i):
    widget.destroy()


label = tk.Label(widget, text="Hover to close the widget")
label.pack()

label.bind('<Enter>', close_widget)

widget.mainloop()

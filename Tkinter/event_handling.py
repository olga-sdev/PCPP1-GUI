"""
Event handling -> mechanisms that allow a program to respond to events.md such as user actions or system-generated events.md.

Event Source: Object where event initially occurred.
Event Object: Information about the event that occurred.
Event Listener: Interface that defines the method to handle the event.
Event Handler: Method that gets called in response to an event.

Example of events -> Tkinter/events.md
"""

import tkinter as tk
from tkinter import messagebox


# Example with messagebox.showinfo()
def click():
    messagebox.showinfo('Info', 'Important info')


widget = tk.Tk()
widget.title('Information')

button_show = tk.Button(widget, text='Info', command=click,
                        bg="aquamarine",
                        fg="CadetBlue",
                        activeforeground="DimGray",
                        activebackground="ForestGreen")
button_show.pack(fill=tk.BOTH)

button_close = tk.Button(widget, text='Close', command=widget.destroy,
                         bg="#FFFFFF",
                         fg="#000000",
                         activeforeground="#0000FF",
                         activebackground="#00FFFF")
button_close.pack(fill=tk.BOTH)

widget.mainloop()


# Example with bind -> connect a widget with an event

def enter(event):
    messagebox.showinfo("Great", "Great")


widget = tk.Tk()
widget.title('Events')

message = tk.Message(widget, text="How is it going?")
message.bind("<Enter>", enter)
message.pack()

widget.mainloop()

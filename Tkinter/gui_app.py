"""
Label –> non-clickable component with text info.

Frame -> non-clickable component for grouping and separating other components.

IntVar class -> invisible object to store integer value and organize internal communication between different widgets.
set() of cls IntVar store the value for it.
"""

import tkinter as tk


widget = tk.Tk()

label = tk.Label(widget, text="Widget Label")
label.pack()

frame = tk.Frame(widget, height=40, width=120, bg="YellowGreen")
frame.pack(fill=tk.BOTH)

button = tk.Button(widget, text="Click")
button.pack(fill=tk.BOTH)

switch = tk.IntVar()
switch.set(1)

widget.mainloop()

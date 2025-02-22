"""
Label –> non-clickable component with text info.

Frame -> non-clickable component for grouping and separating other components.

IntVar class -> invisible object to store integer value and organize internal communication between different widgets.
set() of cls IntVar store the value for it.

Checkbutton -> checkbox, graphical control element with a tick mark (ON state) or empty (OFF state).

Entry -> one-line data, text.

Radiobuttons -> graphical control element to select one option from a predefined set of options.

Checkbutton and Radiobutton are synchronized with switch object and depends on changes in one of elements.
"""

import tkinter as tk


widget = tk.Tk()

frame = tk.Frame(widget, height=40, width=120, bg="YellowGreen")
frame.pack(fill=tk.BOTH)

label = tk.Label(widget, text="Job Application\n Enter name:")
label.pack()

entry = tk.Entry(widget, width=20)
entry.pack()

switch = tk.IntVar()
switch.set(0)  # switch value impacts to state of checkbutton, where 1 - ON state, 0 - OFF state

checkbutton = tk.Checkbutton(widget, text="Work Permission Confirm", variable=switch)
checkbutton.pack()

radiobutton_eu = tk.Radiobutton(widget, text="EU", variable=switch, value=1)
radiobutton_eu.pack()
radiobutton_non_eu = tk.Radiobutton(widget, text="Non-EU", variable=switch, value=0)
radiobutton_non_eu.pack()

button = tk.Button(widget, text="Apply")
button.pack(fill=tk.BOTH)

widget.mainloop()

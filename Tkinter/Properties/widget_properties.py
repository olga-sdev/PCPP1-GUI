"""
font (tuples type) -> property for Button, Frame, Label:
("font_family_name", "font_size", "font_style")

font_family_name ->
Arial
Courier
Helvetica
Times
Verdana

font_style ->
"bold"
"italic"
"underline"
"overstrike"

Widgets sizes -> Tkinter/Properties/properties.md
"""

import tkinter as tk


widget = tk.Tk()
widget.title('Fonts Example')
widget.geometry('400x400')

button = tk.Button(widget, text='Font', font=('Arial', '30', 'italic'))
button.pack()

button["borderwidth"] = 40
button["highlightthickness"] = 20
button["wraplength"] = 20

widget.mainloop()


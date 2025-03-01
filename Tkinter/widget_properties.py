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
"""

import tkinter as tk


widget = tk.Tk()
widget.title('Fonts Example')
widget.geometry('400x400')

button = tk.Button(widget, text='Button with Font', font=('Arial', '30', 'italic'))
button.pack()

widget.mainloop()

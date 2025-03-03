"""
In Tkinter, the cursor property allows you to change the mouse cursor when it hovers over a widget.
Set this property to different cursor styles, such as an arrow, a cross, a hand, etc.

Cursor will change to a hand when you hover over the button. Some common cursor styles you can use are:
arrow
circle
clock
cross
dotbox
exchange
fleur
heart
man
mouse
pirate
plus
shuttle
sizing
spider
spraycan
star
target
tcross
umbrella
watch
"""

import tkinter as tk

weather_widget = tk.Tk()

label_03_03 = tk.Label(weather_widget, height=2, text="03th of March 2025 | Rainy", cursor="umbrella")
label_03_03.pack()

weather_widget.mainloop()

"""
create_arc() -> draw arc shapes, which can be segments of an ellipse or circles.

x0, y0, x1, y1 -> define the bounding box for the ellipse (or circle).
style -> CHORD, PIESLICE, ARC.
start -> starting angle of the arc in degrees (0 degrees points to the right, angles increase counterclockwise).
extent -> width of the arc in degrees.
fill -> fill color for the arc (default is no fill).
outline -> color of the arc outline.
"""

import tkinter as tk


widget = tk.Tk()
canvas = tk.Canvas(widget, width=250, height=250, bg='green')
canvas.pack()

# Draw CHORD
canvas.create_arc(50, 50, 200, 200, style=tk.CHORD, start=45, extent=90, fill="white", outline="white")

# Draw PIESLICE
canvas.create_arc(50, 50, 200, 200, style=tk.PIESLICE, start=90, extent=180, fill="blue", outline="white")

# Draw ARC
canvas.create_arc(50, 50, 200, 200, style=tk.ARC, start=270, extent=180, outline="white")

# Draw CHORD
canvas.create_arc(50, 50, 200, 200, style=tk.CHORD, start=225, extent=90, fill="aquamarine", outline="white")

widget.mainloop()

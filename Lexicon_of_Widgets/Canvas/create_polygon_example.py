"""
create_polygon method in Tkinter -> draws polygons on a canvas.
Specify the coordinates of the vertices, the outline color, fill color, and other attributes to customize appearance.

points -> list of coordinates for the vertices of the polygon. Each pair represents (x, y) positions
fill -> specifies the color inside the polygon
outline -> sets the border color, and  controls the thickness of the outline
width -> width of borderline of polygon
"""

import tkinter as tk

# Create the main window
widget = tk.Tk()
widget.title("Polygon Example")

# Create a canvas widget
canvas = tk.Canvas(widget, width=400, height=300)
canvas.pack()

# Draw a polygon
points = [100, 150, 200, 50, 300, 150, 200, 250]  # Coordinates
canvas.create_polygon(points, fill='green', outline='aquamarine', width=4)

# Run the Tkinter event loop
widget.mainloop()

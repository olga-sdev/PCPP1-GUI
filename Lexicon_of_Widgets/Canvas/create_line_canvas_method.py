"""
The create_line method of the Canvas widget in Tkinter allows to draw straight lines. 
Specify the coordinates of the start and end points of the line, along with optional parameters to customize its appearance, such as color and thickness.
"""

import tkinter as tk


# Create a Tkinter window
widget = tk.Tk()
widget.title("Canvas create_line() Example")

# Create a canvas widget
canvas = tk.Canvas(widget, width=400, height=400, bg="aquamarine")
canvas.pack()

# Draw lines using create_line. Coordinates a sequence of x and y values for the line's points (e.g., x1, y1, x2, y2).
canvas.create_line(5, 5, 5, 400, fill="green", width=2)  # Vertical line
canvas.create_line(400, 5, 400, 400, fill="green", width=2)  # Vertical line
canvas.create_line(5, 400, 400, 400, fill="green", width=2)  # Horizontal line
canvas.create_line(0, 0, 200, 200, fill="green", width=2, dash=(1, 1))  # Dashed diagonal line
canvas.create_line(200, 200, 400, 0, fill="green", width=2, dash=(1, 1))  # Dashed diagonal line

# Run the Tkinter event loop
widget.mainloop()

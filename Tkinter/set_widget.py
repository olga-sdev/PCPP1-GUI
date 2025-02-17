"""
In Python's Tkinter library, geometry managers control the placement of widgets in a window:

* Pack -> packs widgets into the window one after another, either vertically or horizontally;
* Grid -> arranges widgets in a grid-like structure with rows and columns;
* Place -> precise control over widget placement by using x and y coordinates by pixel.
"""
import tkinter as tk


class PlaceExample:
    place_window = tk.Tk()

    node = tk.Button(place_window, text='Node')
    node.place(x=30, y=120, width=140, height=70)
    place_window.mainloop()


class GridExample:
    grid_window = tk.Tk()

    node_1 = tk.Label(grid_window, text='9')
    node_2 = tk.Label(grid_window, text='12')
    node_3 = tk.Label(grid_window, text='3')
    node_4 = tk.Label(grid_window, text='6')

    node_1.grid(row=1, column=0)
    node_2.grid(row=0, column=1)
    node_3.grid(row=1, column=2)
    node_4.grid(row=2, column=1)

    grid_window.mainloop()

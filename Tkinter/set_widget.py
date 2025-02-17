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
    node_3 = tk.Label(grid_window, text='2')
    node_4 = tk.Label(grid_window, text='6')
    node_5 = tk.Label(grid_window, text='4')

    node_1.grid(row=1, column=0)
    node_2.grid(row=0, column=1)
    node_3.grid(row=0, rowspan=2, column=2)
    node_4.grid(row=2, column=1)
    node_5.grid(row=1, rowspan=2, column=2)

    grid_window.mainloop()


class PackExample:
    pack_window = tk.Tk()

    node_1 = tk.Button(pack_window, text='Node Left')  # toward the window's left boundary
    node_2 = tk.Button(pack_window, text='Node Right')  # toward the window's right boundary
    node_3 = tk.Button(pack_window, text='Node Top')  # the widget is packed toward the window's top
    node_4 = tk.Button(pack_window, text='Node Bottom')  # the widget is packed toward the window's bottom

    node_1.pack(side=tk.LEFT, fill=tk.Y)  # expand it in the vertical direction
    node_2.pack(side=tk.RIGHT, fill=tk.BOTH)  # expand it in both directions
    node_3.pack(side=tk.TOP, fill=tk.X)  # expand it in the horizontal direction
    node_4.pack(side=tk.BOTTOM, fill=tk.NONE)  # do not expand the widget (default behavior)

    pack_window.mainloop()

"""
In order to color Button in widget there are additional arguments are required to be added:
bg -> “background-color”
fg -> “foreground-color”

activeforeground -> “foreground-color” used by the event controller when the button is pressed
activebackground -> “background-color” used by the event controller when the button is pressed

Tkinter recognizes over 750 colors -> https://www.tcl-lang.org/man/tcl8.4/TkCmd/colors.htm

mixing three primary colors: red (R), green (G) and blue (B)
all the components are set to zero -> black as a result
all the components are set to 255 -> white as a result

6 hexadecimal #:
#000000 is black
#FFFFFF is white
#FF0000 is red
#00FF00 is green
#0000FF is blue
#00FFFF is turquoise
#FF00FF is violet
"""

import tkinter as tk

widget_color = tk.Tk()
node_color = tk.Button(widget_color,
                       text="Node Color Name",
                       bg="aquamarine",
                       fg="CadetBlue",
                       activeforeground="DimGray",
                       activebackground="ForestGreen")

node_hex = tk.Button(widget_color,
                     text="Node Hex Name",
                     bg="#00FF00",
                     fg="#FFFFFF",
                     activeforeground="#0000FF",
                     activebackground="#00FFFF")

node_color.pack()
node_hex.pack()
widget_color.mainloop()

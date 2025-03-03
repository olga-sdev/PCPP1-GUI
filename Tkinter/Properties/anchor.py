"""
The anchor option in Tkinter widgets allows you to position and align text within a widget. 
For example, with the Label widget, you can use the anchor option to control the placement of text within the label.

The anchor option accepts several values, such as:
n (north)
ne (northeast)
e (east)
se (southeast)
s (south)
sw (southwest)
w (west)
nw (northwest)
center
"""
import tkinter as tk

widget = tk.Tk()

# 1st line
node_nw = tk.Button(widget, text='NW', width=5, height=2, padx=5, pady=5, anchor='nw')
node_nw.grid(row=0, column=0)

node_n = tk.Button(widget, text='N', width=5, height=2, padx=5, pady=5, anchor='n')
node_n.grid(row=0, column=1)

node_ne = tk.Button(widget, text='NE', width=5, height=2, padx=5, pady=5, anchor='ne')
node_ne.grid(row=0, column=2)

# 2nd line
node_w = tk.Button(widget, text='W', width=5, height=2, padx=5, pady=5, anchor='w')
node_w.grid(row=1, column=0)

node_c = tk.Button(widget, text='Center', width=5, height=2, padx=5, pady=5, anchor='center')
node_c.grid(row=1, column=1)

node_e = tk.Button(widget, text='E', width=5, height=2, padx=5, pady=5, anchor='e')
node_e.grid(row=1, column=2)

# 3d line
node_sw = tk.Button(widget, text='SW', width=5, height=2, padx=5, pady=5, anchor='sw')
node_sw.grid(row=2, column=0)

node_s = tk.Button(widget, text='S', width=5, height=2, padx=5, pady=5, anchor='s')
node_s.grid(row=2, column=1)

node_se = tk.Button(widget, text='SE', width=5, height=2, padx=5, pady=5, anchor='se')
node_se.grid(row=2, column=2)

widget.mainloop()

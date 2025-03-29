"""
create_image -> only GIF and PNG formats are accepted.
"""


import tkinter as tk


window = tk.Tk()
canvas = tk.Canvas(window, width=400, height=400, bg='dodgerblue4')

image = tk.PhotoImage(file='robo.png')
canvas.create_image(200, 200, image=image)

canvas.grid()

window.mainloop()

'''
# Example with jpeg files
import tkinter as tk
import PIL


widget = tk.Tk()
canvas = tk.Canvas(widget, width=400, height=400, bg='dodgerblue4')
jpg = PIL.Image.open('robo.jpg')
image = PIL.ImageTk.PhotoImage(jpg)
canvas.create_image(200, 200, image=image)

canvas.grid()

widget.mainloop()
'''

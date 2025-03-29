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

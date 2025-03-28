import tkinter as tk


widget = tk.Tk()
canvas = tk.Canvas(widget, width=300, height=300, bg='aquamarine')

canvas.create_oval(130, 10, 170, 290, outline='blue', width=2, fill='green')
canvas.create_oval(10, 130, 290, 170, outline='green', width=2, fill='blue')

canvas.grid()
widget.mainloop()

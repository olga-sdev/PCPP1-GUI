import tkinter as tk


widget = tk.Tk()

canvas = tk.Canvas(widget, width=300, height=300, bg='aquamarine')

canvas.create_rectangle(50, 50, 250, 250, outline='blue', width=4, fill='green')

label = tk.Label(widget, text='canvas.create_rectangle')

canvas.grid(row=1)
label.grid(row=0)

widget.mainloop()

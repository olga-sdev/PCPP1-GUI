import tkinter as tk


widget = tk.Tk()
canvas = tk.Canvas(widget, width=350, height=350, bg='azure')
canvas.pack()

canvas.create_text(340, 40, text='Open To Work', anchor='ne', font=('Arial', '20', 'italic'), fill='deepskyblue3')

canvas.create_text(180, 170, text='QA Engineer & Python', anchor='center', font=('Arial', '24', 'bold'), fill='cadetblue3')

canvas.create_text(10, 300, text='LN @olga-sdet', anchor='nw', font=('Arial', '10', 'underline'), fill='deepskyblue3')

widget.mainloop()

# Exmple with Label inside the colored Frame

import tkinter as tk


widget = tk.Tk()

frame = tk.Frame(widget, width=730, height=130, bg='yellow')

label = tk.Label(frame, text="The message inside the Tkinter Frame")
label.place(x=160, y=60)

frame.pack()

widget.mainloop()

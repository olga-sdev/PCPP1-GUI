import tkinter as tk


widget = tk.Tk()

text = tk.StringVar()
entry = tk.Entry(widget, textvariable=text)

text.set('')
text.trace('w', text.get())

entry.pack()

widget.mainloop()

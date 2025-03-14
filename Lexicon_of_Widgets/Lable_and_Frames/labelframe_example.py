import tkinter as tk


widget = tk.Tk()

label_frame = tk.LabelFrame(widget, text='Label\nFrame', labelanchor='e',
                            width=400, height=300, bg='aquamarine')

label = tk.Label(label_frame, text="Label inside the ->", bg='aquamarine')
label.place(x=130, y=135)

label_frame.pack()

widget.mainloop()

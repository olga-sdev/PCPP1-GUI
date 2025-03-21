"""
messagebox methods ->

* askyesno()
* askokcancel()
* askretrycancel()
* askquestion()
* showerror()
* showwarning()
"""


import tkinter as tk
from tkinter import messagebox


widget = tk.Tk()
widget.title('messagebox methods')

button_askyesno = tk.Button(widget, text="askyesno",
                            command=lambda: messagebox.askyesno("askyesno", "askyesno"))
button_askyesno.pack()

button_askokcancel = tk.Button(widget, text="askokcancel",
                               command=lambda: messagebox.askokcancel("askokcancel", "askokcancel"))
button_askokcancel.pack()

button_askretrycancel = tk.Button(widget, text="askretrycancel",
                                  command=lambda: messagebox.askretrycancel("askretrycancel", "askretrycancel"))
button_askretrycancel.pack()

button_askquestion = tk.Button(widget, text="askquestion",
                               command=lambda: messagebox.askquestion("askquestion", "askquestion"))
button_askquestion.pack()

button_showerror = tk.Button(widget, text="showerror",
                             command=lambda: messagebox.showerror("showerror", "showerror"))
button_showerror.pack()

button_showwarning = tk.Button(widget, text="showwarning",
                               command=lambda: messagebox.showwarning("showwarning", "showwarning"))
button_showwarning.pack()

widget.mainloop()

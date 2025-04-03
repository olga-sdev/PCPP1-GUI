"""
Objectives
Learn practical skills related to:

using the Entry, Radiobutton and Button widgets,
managing widgets with the grid manager,
checking the validity of user input and handling errors.

Scenario
Calculator contains two fields that the user can use to enter arguments, a radio button to select the operation to perform, and a button initiating the evaluation:

Calculator - reference

Expect the calculator to behave in the following way:

if both fields contain valid (integer or float) numbers, clicking the Evaluate button should display an info window showing the evaluation's result;
if any of the fields contains invalid data (e.g., a string, or a field is empty), clicking the Evaluate button should present an error window describing the problem
Don't forget to protect your code from dividing by zero, and use the grid manager to compose the window interior.
"""

import tkinter as tk
from tkinter import messagebox


widget = tk.Tk()
widget.title('Calculator')
widget.config(bg='darkseagreen1')
widget.geometry('240x200')

canvas = tk.Canvas(widget, height=140, width=140, bg='darkseagreen1')
canvas.place(x=40, y=40)


def evaluation():
    if resolve() is None:
        messagebox.showerror(message=f'The field contains invalid data.'
                                     f'\nFirst entry: {first_entry.get()}'
                                     f'\nSecond entry: {second_entry.get()}')
    else:
        messagebox.showinfo(title='Result', message=f'The result is: {resolve()}')


def resolve():
    global result
    try:
        if selected_option.get() == "+":
            result = float(first_entry.get()) + float(second_entry.get())
        elif selected_option.get() == "-":
            result = float(first_entry.get()) - float(second_entry.get())
        elif selected_option.get() == "/":
            result = float(first_entry.get()) / float(second_entry.get())
        elif selected_option.get() == "*":
            result = float(first_entry.get()) * float(second_entry.get())
        return result
    except ValueError as err:
        print(f'Enter int or float values: {err}')
    except ZeroDivisionError as err:
        print(f"Invalid operation: Cannot divide by zero: {err}")


first_value = tk.IntVar()
first_entry = tk.Entry(canvas, width=7, textvariable=first_value)
first_entry.delete(0, tk.END)
first_entry.grid(column=0, row=2)

second_value = tk.IntVar()
second_entry = tk.Entry(canvas, width=7, textvariable=second_value)
second_entry.delete(0, tk.END)
second_entry.grid(column=2, row=2)

selected_option = tk.StringVar()
selected_option.set("+")

radio_plus = tk.Radiobutton(canvas, text='+', variable=selected_option, value='+',
                            bg='darkseagreen1', command=resolve)
radio_plus.grid(column=1, row=0)

radio_minus = tk.Radiobutton(canvas, text='-', variable=selected_option, value='-',
                             bg='darkseagreen1', command=resolve)
radio_minus.grid(column=1, row=1)

radio_divis = tk.Radiobutton(canvas, text='/', variable=selected_option, value='/',
                             bg='darkseagreen1', command=resolve)
radio_divis.grid(column=1, row=2)

radio_mult = tk.Radiobutton(canvas, text='*', variable=selected_option, value='*',
                            bg='darkseagreen1', command=resolve)
radio_mult.grid(column=1, row=3)

button_evaluate = tk.Button(canvas, text='Evaluate', fg='darkslategray', bg='darkseagreen3',
                            font=('Arial', '9', 'bold'), command=evaluation)
button_evaluate.grid(column=1, row=5)

widget.mainloop()

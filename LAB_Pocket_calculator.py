"""
Objectives
Learn practical skills related to:

dealing with observable variables,
working with the Entry widget,
constructing complex interfaces with many cooperating Button widgets.

Scenario
Implement four-function "pocket" calculator.
Feel free to equip it with many extra functions, but adding, subtracting, multiplying and dividing is a must.
The calculator needs a change sign function, a decimal point button and the clear button.
We don't have to mention that your calculator should be resistant to zero-division attempts,
in which case it should display an error message instead of producing any garbage result or raising an exception.


Here are some of our assumptions:

respond only to mouse clicks; keyboard presses can be silently ignored,
the display's width is 10 - use a fixed-width font to work with it,
you are not allowed to fill the display with more than 10 characters (including the decimal point and minus sign if it is needed);
if the result needs more characters to be presented, you should display an error message,
you are allowed to remove some less significant digits located after the decimal point to shorten the result in effect,
if the result has no significant digits after the decimal point, the point should not appear on the display.
"""
import tkinter as tk


widget = tk.Tk()
widget.title('Calculator')
widget.config(bg='snow1')
widget.resizable(width=False, height=False)


def evaluate():
    text_of_label.set(eval(text_of_label.get()))


def set_value(value):
    text = text_of_label.get()
    text_of_label.set(value) if text == '0' else text_of_label.set(text + value)


def set_abs():
    evaluate()
    text = int(text_of_label.get())
    if text == abs(text):
        text = -abs(text)
        text_of_label.set(str(text))
    elif text == -abs(text):
        text = abs(text)
        text_of_label.set(str(text))


def clean_result():
    text_of_label.set('0')


text_of_label = tk.StringVar()
text_of_label.set('0')

label = tk.Label(widget, textvariable=text_of_label, height=3, width=20, bg='snow1',
                 font=('Arial', '15', 'bold'), anchor='e')
label.grid(row=0, column=0, columnspan=4)

button_0 = tk.Button(widget, text='0', width=10, height=2, bg='white', command=lambda: set_value('0'))
button_0.grid(row=5, column=1)

button_1 = tk.Button(widget, text='1', width=10, height=2, bg='white', command=lambda: set_value('1'))
button_1.grid(row=4, column=0)

button_2 = tk.Button(widget, text='2', width=10, height=2, bg='white', command=lambda: set_value('2'))
button_2.grid(row=4, column=1)

button_3 = tk.Button(widget, text='3', width=10, height=2, bg='white', command=lambda: set_value('3'))
button_3.grid(row=4, column=2)

button_4 = tk.Button(widget, text='4', width=10, height=2, bg='white', command=lambda: set_value('4'))
button_4.grid(row=3, column=0)

button_5 = tk.Button(widget, text='5', width=10, height=2, bg='white', command=lambda: set_value('5'))
button_5.grid(row=3, column=1)

button_6 = tk.Button(widget, text='6', width=10, height=2, bg='white', command=lambda: set_value('6'))
button_6.grid(row=3, column=2)

button_7 = tk.Button(widget, text='7', width=10, height=2, bg='white', command=lambda: set_value('7'))
button_7.grid(row=2, column=0)

button_8 = tk.Button(widget, text='8', width=10, height=2, bg='white', command=lambda: set_value('8'))
button_8.grid(row=2, column=1)

button_9 = tk.Button(widget, text='9', width=10, height=2, bg='white', command=lambda: set_value('9'))
button_9.grid(row=2, column=2)

button_plus = tk.Button(widget, text='+', width=10, height=2, bg='lavender', command=lambda: set_value('+'))
button_plus.grid(row=4, column=3)

button_minus = tk.Button(widget, text='-', width=10, height=2, bg='lavender', command=lambda: set_value('-'))
button_minus.grid(row=3, column=3)

button_mult = tk.Button(widget, text='*', width=10, height=2, bg='lavender', command=lambda: set_value('*'))
button_mult.grid(row=2, column=3)

button_div = tk.Button(widget, text='/', width=10, height=2, bg='lavender', command=lambda: set_value('/'))
button_div.grid(row=1, column=3)

button_eval = tk.Button(widget, text='=', width=10, height=2,
                        bg='dodgerblue4', fg='white',
                        font=('Arial', '9', 'bold'),
                        command=evaluate)
button_eval.grid(row=5, column=3)

button_dot = tk.Button(widget, text='.', width=10, height=2, bg='white', command=lambda: set_value('.'))
button_dot.grid(row=5, column=2)

button_plus_min = tk.Button(widget, text='+/-', width=10, height=2, bg='white', command=set_abs)
button_plus_min.grid(row=5, column=0)

button_c = tk.Button(widget, text='C', width=33, height=2, bg='lavender',
                     command=clean_result)
button_c.grid(row=1, column=0, columnspan=3)


widget.mainloop()

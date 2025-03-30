"""
Objectives
Learn practical skills related to:

using screen coordinates,
managing widgets with the place manager,
binding events using the bind() method.
Scenario
Write a simple game - an infinite game which humans cannot win. Here are the rules:

the game goes on between TkInter and the user (probably you)
TkInter opens a 500x500 pixel window and places a button saying "Catch me!" in the top-left corner of the window;
if the user moves the mouse cursor over the button, the button immediately jumps to another location inside the window; 
assure that the new location is distant enough to prevent the user from making an instant click,
the button must not cross the window's boundaries during the jump!

Use the place() method to move the button, and the bind() method to assign your own callback.
"""

import tkinter as tk
import random


widget = tk.Tk()
widget.title('Speedy Button')
widget.geometry('400x400')
widget.config(bg='dodgerblue4')


def relocate(event):
    speedy_button.place(x=random.randint(40, 300),
                        y=random.randint(40, 300))


speedy_button = tk.Button(widget, text='Speedy Button', bg='cadetblue3', fg='dodgerblue4',
                          relief='ridge', font=('Arial', '9', 'bold'))

speedy_button.grid(row=0, column=0)

speedy_button.bind('<Enter>', relocate)

widget.mainloop()

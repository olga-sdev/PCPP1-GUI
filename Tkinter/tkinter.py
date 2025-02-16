"""
In Python TkInter is a package named tkinter.

tk elements:

importing tkinter components;
creating an ap’s window;
adding a set of widgets;
launching the event controller.

The main app window is created by the tkinter method Tk().

To start controller -> invoke the main window's method mainloop().

Exiting the main loop -> finish the app.

place() button method -> coordinates x, y refer to the pixel occupied by the upper-left corner;
widget's location is measured in pixels;
widget's size is determined by the constructor.

Event handler is a piece of code responsible for responding to all clicks addressed to our button.

destroy() terminates app.

Function designed to be invoked by someone/something else -> callback | handler.

Argument 'command' will be invoked when the button is clicked.

One and same callback can be bound with more than one widget.

messagebox -> create dialog boxes intended to ask questions, display messages, and to receive a user's reply.


"""

import tkinter
from tkinter import messagebox


widget_app = tkinter.Tk()
widget_app.title('WiAPP')


def click():
    confirm = messagebox.askokcancel("Close widget", "Confirm to close widget")
    if confirm:
        widget_app.destroy()


button = tkinter.Button(widget_app, text="Hej då", command=click)
button.place(x=80, y=80)

widget_app.mainloop()

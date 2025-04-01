"""
Objectives
Learn practical skills related to:

dealing with Canvas and some of its methods,
using different colors.
Scenario
Look at the snippet in the editor - can you see that mysterious tuple consisting of four three-element tuples? 
Can you guess what information it carries?

It's a set of rules describing the behavior of British-style traffic lights. 
Assume that the very first element of all inner tuples is assigned to the red light, 
the second - to the yellow, and the third - to the green one. 
True means that the light is on, False - off.

As you see, there are four different phases:

the red light is lit,
the red and yellow lights are lit together,
the green light is lit,
the yellow light is lit.
Your task is to implement a model which will show how such a traffic signal works. The model should look as follows:

Red Red-Yellow Green Yellow

The model consists of three widgets.

the canvas being a background for all the three lights,
the button named "Next" - clicking it switches the signal to the next phase,
the button named "Quit" - clicking it immediately exits the program.
Note: use the phases tuple as a "knowledge base" for your whole code. 
The code has to adapt to any change done to the tuple, e.g., 
there can be more or less than four phases and the lights' combinations can be different also.

"""

from tkinter import Tk, Button, Canvas


phases = ((True,  False, False),
          (True,  True,  False),
          (False, False, True),
          (False, True,  False))

phase = 0


def change_phase(event):
    global phase
    print(phase)
    if phase == 3:
        canvas.create_oval(4, 4, 200, 200, outline='black', width=4, fill='lavenderblush4')
        canvas.create_oval(204, 4, 400, 200, outline='black', width=4, fill='yellow')
        canvas.create_oval(404, 4, 596, 200, outline='black', width=4, fill='lavenderblush4')
        phase = 0
    elif phase == 2:
        canvas.create_oval(4, 4, 200, 200, outline='black', width=4, fill='lavenderblush4')
        canvas.create_oval(204, 4, 400, 200, outline='black', width=4, fill='lavenderblush4')
        canvas.create_oval(404, 4, 596, 200, outline='black', width=4, fill='green')
        phase = 3
    elif phase == 1:
        canvas.create_oval(4, 4, 200, 200, outline='black', width=4, fill='red')
        canvas.create_oval(204, 4, 400, 200, outline='black', width=4, fill='yellow')
        canvas.create_oval(404, 4, 596, 200, outline='black', width=4, fill='lavenderblush4')
        phase = 2
    elif phase == 0:
        canvas.create_oval(4, 4, 200, 200, outline='black', width=4, fill='red')
        canvas.create_oval(204, 4, 400, 200, outline='black', width=4, fill='lavenderblush4')
        canvas.create_oval(404, 4, 596, 200, outline='black', width=4, fill='lavenderblush4')
        phase = 1


widget = Tk()
widget.title('Traffic Lights')
widget.geometry('600x260')

canvas = Canvas(widget, width=600, height=200, bg='darkslategray')

canvas.create_oval(4, 4, 200, 200, outline='black', width=4, fill='red')
canvas.create_oval(204, 4, 400, 200, outline='black', width=4, fill='lavenderblush4')
canvas.create_oval(404, 4, 596, 200, outline='black', width=4, fill='lavenderblush4')

canvas.grid(row=0)

button_next = Button(widget, text='Next', width=7)
button_next.grid(row=1)

button_next.bind('<Button-1>', change_phase)

button_quit = Button(widget, text='Quit', width=7, command=lambda: widget.quit())
button_quit.grid(row=2)

widget.mainloop()

"""
Objectives
Learn practical skills related to:

writing event handlers and assigning them to widgets using the bind() method,
managing widgets with the grid manager,
using the after() and after_cancel() methods.

Scenario
Write a game, which can help many people to improve their perception skills and visual memory: The Clicker as clicking is what we expect from the player.

The Clicker's board consists of 25 buttons and each of the buttons contains a random number from range 1..999. Note: each number is different!

The board there is a timer which initially shows 0. The timer starts when the user clicks the board for the first time.

The player clicks all the buttons in the order imposed by the numbers - from the lowest to the highest one. 

Additional rules say that:

the properly clicked button changes the button's state to DISABLED (it greys the button out)
the improperly clicked button shows no activity,
the timer increases its value every second,
when all the buttons are greyed out (i.e., the player has completed his/her task) the timer stops immediately.

Hint: consider using the <Button-1> event instead of setting the command button property - it may simplify your code.
"""
import random
import tkinter as tk


widget = tk.Tk()
widget.title('Clicker')

counter = 0


def change_status(node):
    global counter
    node['state'] = tk.DISABLED
    counter += 1
    text_label.set(counter)
    if counter == 25:
        text_label.set(0)


buttons = []
button_names = random.sample(range(1, 999), 25)

for i, name in enumerate(button_names):
    button = tk.Button(widget, text=name, width=7, state=tk.NORMAL,
                       command=lambda index=i: change_status(buttons[index]))
    button.grid(row=i // 5, column=i % 5)
    buttons.append(button)


text_label = tk.IntVar()
s = 0
text_label.set(s)
label = tk.Label(widget, textvariable=text_label)
label.grid(row=5, column=2)


widget.mainloop()

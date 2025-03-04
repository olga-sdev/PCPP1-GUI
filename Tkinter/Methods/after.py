"""
after() and after_cancel() methods are used for scheduling and managing timed operations within a tkinter app.

after(delay_ms, callback=None, *args) ->
* schedules a callback (function) to be called after a specified amount of time (in milliseconds).
* If provide only the delay_ms without a callback, it simply delays execution for that period.
* If used with a callback, it will return an (ID) for the scheduled action, to cancel the callback.

after_cancel(id) ->
cancels a callback that was scheduled using after(), provided you pass the (id) returned by the after() method.
"""

import tkinter as tk


def greeting():
    lb = tk.Label(widget, text='Hi')
    lb.pack()


widget = tk.Tk()
frame = tk.Frame(widget, width=70, height=70, bg='yellow')
frame.pack()
frame.after(3000, greeting)

widget.mainloop()

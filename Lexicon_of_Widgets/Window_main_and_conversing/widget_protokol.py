"""
In Tkinter, protocols are used to handle special events or interactions between app and the OS.

"WM_DELETE_WINDOW" -> triggered when user attempts to close the application window (e.g., by clicking the "X" button).

"WM_DELETE_WINDOW" the only one actual protokol.
"""

import tkinter as tk
from tkinter import messagebox


widget = tk.Tk()

widget.protocol("WM_DELETE_WINDOW", lambda: widget.destroy() if messagebox.askyesno(
            "Confirmation", "Confirm the widget to be closed.") else True)

widget.mainloop()

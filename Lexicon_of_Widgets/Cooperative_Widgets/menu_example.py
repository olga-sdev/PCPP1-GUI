"""
In tkinter, a Menu widget is used to create menus in a GUI application.
It can be associated with the main window or any other toplevel window.

Here's an overview of how to use it:

Creating a Menu
Attach to a Window: The Menu widget is typically attached to a Tk or Toplevel window using the config(menu=menu_bar) method.

Add Menu Items: You can add submenus, commands, separators, or checkboxes to your menu.

Key Points
* add_command: Adds an actionable menu item.
* add_cascade: Creates a submenu.
* add_separator: Adds a horizontal line to separate items.
* tearoff: Affects whether a menu can be "torn off" into its own window (set to 0 to disable this feature).

accelerator -> string naming the key
entryconfigure -> sub-menu item's configurator method with 2 parameters 'index' and 'property'
"""

import tkinter as tk
from tkinter import messagebox


widget = tk.Tk()
widget.title('Code Editor')
widget.geometry('250x170')


def about(event=None):
    messagebox.showinfo('App','Code Editor Menu')


menu_bar = tk.Menu(widget)

list_menu = tk.Menu(menu_bar, tearoff=0)
list_menu.add_command(label='File')
list_menu.add_command(label='Edit')
list_menu.add_command(label='View')
list_menu.add_command(label='Code')
list_menu.add_command(label='Refactor')

sub_settings = tk.Menu(list_menu, tearoff=0)
sub_settings.add_command(label='Plugins')
sub_settings.add_command(label='Frameworks')
sub_settings.entryconfig(0, state=tk.DISABLED)

list_menu.add_cascade(label='Settings', menu=sub_settings)

list_menu.add_separator()
list_menu.add_command(label='About', command=about, accelerator='Ctrl+A')
list_menu.add_command(label='Exit', command=widget.quit)

# Set key Alt+A with underline=0
menu_bar.add_cascade(label='App menu', menu=list_menu, underline=0)

widget.config(menu=menu_bar)

widget.bind_all("<Control-a>", about)

widget.mainloop()

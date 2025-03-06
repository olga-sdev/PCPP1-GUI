"""
In Tkinter, observable variables are used to create dynamic, data-bound interfaces. 
These special variables can be observed for changes, and when they change, any widgets bound to them will automatically update:

StringVar: For string values.
IntVar: For integer values.
DoubleVar: For floating-point values.
BooleanVar: For boolean values.

It is typed.

To assign a value to an observable variable use set().

Each observable variable can be enriched with a number of observers (function - callback).

trace() -> add observer to a variable.

Arguments of trace():

- a string describing which events should trigger an observer:
"r" – if you want to be aware of the variable reads (accessing its value through get())
"w" – if you want to be aware of the variable writes (changing its value through set())
"u" – if you want to be aware of the variable’s annihilation (removing the object through del)
- a reference to a function which will be invoked when the specified event occurs.
"""
import tkinter as tk


class ObservableApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Observable Variables in Tkinter")
        self.geometry("210x120")

        self.string_var = tk.StringVar(value="")
        self.string_var.trace_add("write", self.variable_updated)

        self.label = tk.Label(self, text='Write your text:')
        self.label.pack(pady=10)

        self.entry = tk.Entry(self, textvariable=self.string_var)
        self.entry.pack(pady=10)

    def variable_updated(self, *args):
        print("Variable updated to:", self.string_var.get())


if __name__ == "__main__":
    app = ObservableApp()
    app.mainloop()

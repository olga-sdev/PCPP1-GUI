"""
Tkinter, the Python GUI library, allows you to use images in your interface quite easily with the PhotoImage.

A few notes:

Replace "path_to_image/logo.png" with the actual path to your image file.

The PhotoImage class only supports .png, .gif, and .ppm/.pgm formats.
If logo is in another format (e.g., .jpg) -> use the Pillow library (PIL) for loading it.

If logo isn’t appearing, it might be due to the Python garbage collection removing the image.
To fix that, make sure keep a reference to the PhotoImage object.
"""

import tkinter as tk
from tkinter import PhotoImage


# Create the main window
widget = tk.Tk()
widget.title("Logo Widget")
widget.geometry("270x70")

# Load the image (Make sure the file path is correct)
photo_logo = PhotoImage(file="icon.png")  # Replace with your image path

# Create a label and set the image
label = tk.Label(widget, image=photo_logo, bg='green')
label.pack()

# Set the image for title of widget
widget.tk.call('wm', 'iconphoto', widget._w, photo_logo)

# Run the application
widget.mainloop()

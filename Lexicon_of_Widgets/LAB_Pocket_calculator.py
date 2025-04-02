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


Some of assumptions:

respond only to mouse clicks; keyboard presses can be silently ignored,
the display's width is 10 - use a fixed-width font to work with it,
you are not allowed to fill the display with more than 10 characters (including the decimal point and minus sign if it is needed); 
if the result needs more characters to be presented, you should display an error message,
you are allowed to remove some less significant digits located after the decimal point to shorten the result in effect,
if the result has no significant digits after the decimal point, the point should not appear on the display.
"""

import tkinter as tk


# Write your code here.


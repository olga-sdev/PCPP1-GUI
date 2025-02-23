
| Property name | Property role                                                                                      | 
|---------------|----------------------------------------------------------------------------------------------------|
| widget        | The widget’s object (not the widget’s name!) to which the event is addressed                       | 
| x             | The mouse cursor’s coordinates at the moment of the ...                                            | 
| y             | ... event’s occurrence (both coordinates are counted relative to the target widget)                | 
| x_root        | As above, but relative to the screen                                                               | 
| y_root        |                                                                                                    |
| char          | The pressed key character code (only for keyboard events)                                          |
| keysym        | The pressed key symbol (only for keyboard events)  https://www.tcl.tk/man/tcl8.4/TkCmd/keysyms.htm | 
| keycode       | The pressed key numerical code (only for keyboard events)                                          | 
| num           | The number of the clicked mouse button (only for mouse events)                                     | 
| type          | The event’s type                                                                                   |

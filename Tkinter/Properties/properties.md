
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



| Widget sizes property name | Property role                                                                                                        | 
|----------------------------|----------------------------------------------------------------------------------------------------------------------|
| borderwidth                | The width of the 3D-frame surrounding some widgets (e.g., Button)                                                    | 
| highlightthickness         | The width of the additional frame drawn around the widget when it gains the focus                                    | 
| padx                       | The width/height of an additional empty space/margin around the widget                                               | 
| pady                       | The width/height of an additional empty space/margin around the widget                                               | 
| wraplength                 | If the text filling the widget becomes longer than this property’s value, it'll be wrapped (possibly more than once) | 
| height                     | The height of the widget                                                                                             | 
| underline                  | The index of the character inside the widget’s text, which should be presented as underlined or -1 otherwise         |
| width                      | The width of the widget                                                                                              |

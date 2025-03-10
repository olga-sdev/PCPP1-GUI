
| Radiobutton property | Method role                                                                                                                                                                   | 
|----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| command              | the callback being invoked when the Radiobutton (not the group it belongs to!) changes its state                                                                              | 
| justify              | the same as for Button                                                                                                                                                        | 
| state                | the same as for Button                                                                                                                                                        | 
| variable             | an observable IntVar or StringVar variable reflecting the current selection within the Radiobutton’s group; changing the variable’s value automatically changes the selection | 
| value                | a unique (inside the group) value identifying the Radiobutton; can be an integer value or a string, and should be compatible with the variable’s type                         | 


	
| Radiobutton method | Method role                                                | 
|--------------------|------------------------------------------------------------|
| deselect()         | unchecks the widget                                        | 
| flash()            | the same as for Button                                     | 
| invoke()           | the same as for Button                                     | 
| select()           | checks the widget                                          |
	

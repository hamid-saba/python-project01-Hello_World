from tkinter import *

#window -- has to go first
root = Tk()

#define then put on screen thats how tkinter works
#creating a label widget
myLabel = Label(root, text="Hello World!")

#now put to root widget
#we can pack it into window widget
myLabel.pack()

#create an event unit -  a graphic unit loops to notice graphical updates and inputs
#main loop of program
root.mainloop()

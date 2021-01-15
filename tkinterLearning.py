#!/usr/bin/env python3
from tkinter import *
from PIL import Image, ImageTk
import calculator, astroapi, nasaapis, apod
import os, sys, pprint, io
path = '../'
sys.path.append(path)
#this is declaring a window
root = Tk()
title = "Python script Runner 2000"
root.title(title)

#entry widget - text entry field
textEntry = Entry(root, width=50, fg="red", bg="black")
#default text goes like this - it IS part of the text entry
textEntry.insert(0, "Type the name of the python script here")
images = []
#functions that buttons or other things can call on as events
def runBtnClick():
    # grab things from the text entry field
    userEntry = textEntry.get()
    #define something, just like normal window
    newLabel = Label(root, text=f'Calling python script {userEntry}.py')
    #show the label
    newLabel.grid()
    # assigns the imported module based on the user entry into the text field
    moduletocall = sys.modules[userEntry]
    #assigns the main method as the method to use, allowing the script to run in the terminal
    methodtocall = getattr(moduletocall, 'main')
    #display picture if calling apod
    raw_data = methodtocall()
    programAnswer = Message(root, text=raw_data)
    if userEntry == 'apod':
        im = Image.open(io.BytesIO(raw_data))
        image = ImageTk.PhotoImage(im)
        label1 = Label(root, image=image)
        label1.grid(column=3)

        #need to keep a local refernce to the image or it breaks
        images.append(image)
    else:
        programAnswer.grid(column=3)

#clears the text widget on event - have to pass an event to be able to bind it do a widget
def clearTextEntry(event):
    event.widget.delete(0, 'end')

#some examples of binding - focus in is when the widget receives focus from a function or from tabbing around
textEntry.bind("<FocusIn>", clearTextEntry)
#clears the text field when left clicked onto the field
textEntry.bind("<Button-1>", clearTextEntry)


#define labels
titleLabel = Label(root, text=title)
# myLabel2 = Label(root, text="Hello World1")
# myLabel3 = Label(root, text="Hello World1")
# myLabel4 = Label(root, text="Hello World1")
# myLabel5 = Label(root, text="Hello World1")
resultsLabel = Label(root, text="Results")

#buttons - declare, use Button(window that it goes in, padding (x or y) - think css), command(same as an event))
#also has fg color, bg color
runBtn = Button(root, text="Run it!", padx=10, pady=10, fg="orange", bg="green", command=runBtnClick)

#display the widget, period
# myLabel.pack()

#display the widget in a grid - cannot use grid and pack for the same widget
titleLabel.grid(row=0, column=0, columnspan=3)
# myLabel2.grid(row=1, column=1)
# myLabel3.grid(row=2, column=2)
# myLabel4.grid(row=3, column=3)
# myLabel5.grid(row=4, column=4)
runBtn.grid(row=1, column=0, columnspan=3, sticky="N")
textEntry.grid(row=2, column=0, columnspan=2)
resultsLabel.grid(row=2, column=2, sticky="N")




#event loop needs to be started - the loop is what everything in the window exists in until the window is closed
root.mainloop()

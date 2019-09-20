'''
This example shows you how you can capture mouse click events in tkinter
'''
#import the library
from tkinter import *
#create a window object
root = Tk()
#create the function to handle the click events
#note that event is a special object in tkinter that will be generated each time there is a click
def callback(event):
    #note that we can do other things with our x and y now that we know how to get them
    print ("clicked at", event.x, event.y)

#setup the window size
frame = Frame(root, width=400, height=400)
#everything in the window will be considered a button, which calls the callback function when pressed
frame.bind("<Button-1>", callback)
#put the sizing and button definition into our window (pack is the simplest method)
frame.pack()

#title the overall window
root.title("Example of capturing a mouse click location.")
#show the window - windows run in a loop listening for the window close button to break the loop
root.mainloop()

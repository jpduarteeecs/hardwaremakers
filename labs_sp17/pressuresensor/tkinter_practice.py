#Juan Duarte
#Reference
#https://www.youtube.com/watch?v=RJB1Ek2Ko_Y&list=PL6gx4Cwl9DGBwibXFtPtflztSNPGuIB_d
from tkinter import *
from PIL import Image, ImageTk

'''#Tutorial 1
root = Tk() #tkinter class, blank windows

theLabel = Label(root, text="hello")
theLabel.pack()

root.mainloop() #keep this in an infinite loop, so it does not close
'''

'''#Tutorial 2: stacking buttoms
root = Tk() #tkinter class, blank windows

topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text="Button 1",fg="red")
button2 = Button(topFrame, text="Button 2",fg="green")
button3 = Button(topFrame, text="Button 3",fg="purple")
button4 = Button(bottomFrame, text="Button 4",fg="purple")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)

root.mainloop() #keep this in an infinite loop, so it does not close'''

'''#tutorial 4, 5
root = Tk() #tkinter class, blank windows

label_1 = Label(root, text="Name")
label_2 = Label(root, text="Password")
entry_1 = Entry(root)
entry_2 = Entry(root)

label_1.grid(row=0, sticky=E)
label_2.grid(row=1,  sticky=E)

entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)

c = Checkbutton(root, text="Keep me looged in")
c.grid(columnspan=2)

root.mainloop()'''

"""#Tutorial 6, A
root = Tk() #tkinter class, blank windows

def printName():
    print("hello my name is Juan")

button_1 = Button(root, text="Print my name", command=printName)
button_1.pack()
``
root.mainloop()"""

'''#Tutorial 6, B
root = Tk() #tkinter class, blank windows

def printName(event):
    print("hello my name is Juan")

button_1 = Button(root, text="Print my name")
button_1.bind("<Button-1>",printName)
button_1.pack()

root.mainloop()'''

'''
#tutorial 7, left, middle right click

root = Tk() #tkinter class, blank windows

def leftClick(event):
    print("Left")
def middleClick(event):
    print("middle")
def rightClick(event):
    print("right")

frame = Frame(root, width=300, height=250)
frame.bind("<Button-1>",leftClick)
frame.bind("<Button-2>",middleClick)
frame.bind("<Button-3>",rightClick)
frame.pack()'''

#tutorial 8

class BuckysButtons:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.printButton = Button(frame, text="Print Message", command=self.printMessage)
        self.printButton.pack(side=LEFT)

        self.quitButton = Button(frame, text="Quit", command = frame.quit)
        self.quitButton.pack(side=LEFT)

    def printMessage(self):
        print("Wow, this work")

root = Tk() #tkinter class, blank windows
b = BuckysButtons(root)
root.mainloop()

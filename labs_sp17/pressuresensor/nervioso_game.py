#Juan Duarte
import time
import random
from serial import *
from tkinter import *
from PIL import ImageTk, Image #to import images

#serial port set-up
serialPort = "/dev/ttyACM0"
baudRate = 9600
ser = Serial(serialPort , baudRate, timeout=0, writeTimeout=0) #ensure non-blocking

#card set-up
home_dir = "/home/juan/research"
path = home_dir+"/hardwaremakers/labs_sp17/pressuresensor/png/"

#make a TkInter Window
root = Tk()
root.wm_title("Nervioso Game")


var = StringVar()
var.set('hello')
l = Label(root, textvariable = var)
l.pack()

img = ImageTk.PhotoImage(Image.open(path+"red_joker.png"))
panel = Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")

number_of = ["ace_of", "2_of", "3_of", "4_of", "5_of", "6_of", "7_of", "8_of", "9_of", "10_of", "jack_of", "queen_of", "king_of"]
suite_png = ["_clubs.png", "_hearts.png", "_diamonds.png", "_spades.png"]
s = ""

start=0
end=0
time_elapse_card = 1 #1 second

def readSerial():
    global start
    global end
    while True:

        c = ser.readline() # attempt to read a character from Serial

        #was anything read?
        if len(c) == 0:
            break
        #else:
        #    print(c)

    end = time.time()
    if (end - start)>time_elapse_card:
        start = time.time()
        s = random.choice(number_of)
        s += random.choice(suite_png)
        print(s + "\n")
        # make a scrollbar
        img2 = ImageTk.PhotoImage(Image.open(path+s))
        panel.configure(image = img2)
        panel.image = img2
        var.set(s)
        root.update_idletasks()

    root.after(10, readSerial) # check serial again soon


# after initializing serial, an arduino may need a bit of time to reset
root.after(100, readSerial)

root.mainloop()

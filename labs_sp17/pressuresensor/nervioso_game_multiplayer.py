############################## Decal Hardware Makers
#Juan Duarte and Thomas Asmar, Feb 2017
#Nervioso Game
############################## Libraries
import time
import random
from serial import *
from tkinter import *
from PIL import ImageTk, Image #to import images

##############################serial port set-up
serialPort = "/dev/ttyACM0"
baudRate = 9600
ser = Serial(serialPort , baudRate, timeout=0, writeTimeout=0) #ensure non-blocking

##############################card path set-up
home_dir = "/home/juan/research"
path = home_dir+"/hardwaremakers/labs_sp17/pressuresensor/png/"

##############################card name variables
number_of = ["ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king"]
suite_png = ["_clubs.png", "_hearts.png", "_diamonds.png", "_spades.png"]
s = ""

##############################Time variables
start=0
end=0
time_elapse_card = 1 #1 second

##############################make a TkInter Window
root = Tk()
root.wm_title("Nervioso Game")

##############################Top button set up
card_count= 0
flag_stop_start = False
def printName(event):
    print("stop or start pressed")
    global card_count, flag_stop_start, start
    card_count = 0
    if flag_stop_start==True:
        var_start_stop.set("Start")
        flag_stop_start = False
        card_count=0
    else:
        var_start_stop.set("Stop")
        flag_stop_start = True
        start = time.time()
        card_count=0
    root.update_idletasks()

var_start_stop = StringVar()
var_start_stop.set('Start')
button_1 = Button(root, textvariable=var_start_stop)
button_1.bind("<Button-1>",printName)
button_1.pack()

############################## display name of current card to match
var = StringVar()
var.set('Card Name: WAITING...')
l = Label(root, textvariable = var)
l.pack()

############################## card image set up
img = ImageTk.PhotoImage(Image.open(path+"red_joker.png"))
panel = Label(root, image = img)
panel.pack( fill = "both", expand = "yes")

############################## display name of current card to match
var3 = StringVar()
var3.set('Response Time:')
l3 = Label(root, textvariable = var3)
l3.pack()

############################## loop to read serial and update GUI, TODO: change this to thread
def readSerial():
    global start
    global end
    global card_count
    global flag_stop_start

    bytes_from_serial = ser.readline() # attempt to read a character from Serial
    #was anything read?
    if len(bytes_from_serial) > 0:
        time_response_info = (bytes_from_serial.decode("utf-8"))
        time_response_info_list = time_response_info.split()
        player_name = time_response_info_list[0]
        time_response = time_response_info_list[1]
        print (time_response)
        flag_stop_start = False
        var_start_stop.set("Start")
        var3.set('Winer: '+player_name+', Time: '+ str(time_response) + " ms")
        root.update_idletasks()

    end = time.time()
    if ((end - start)>time_elapse_card) and (flag_stop_start):
        ser.write(str.encode('0'))
        start = time.time()
        #choose random card and check match
        s = random.choice(number_of)
        if (s==number_of[card_count]):
            print ("Match")
            ser.write(str.encode('1'))
        s += "_of"+random.choice(suite_png)
        print(s + "\n")

        #Update card image
        img2 = ImageTk.PhotoImage(Image.open(path+s))
        panel.configure(image = img2)
        panel.image = img2
        #update name of card
        var.set("Card Name: "+ number_of[card_count])
        root.update_idletasks()
        #update card count
        card_count=card_count+1
        if (card_count>len(number_of)-1):
            card_count=0

    root.after(10, readSerial) # check serial again soon


# after initializing serial, an arduino may need a bit of time to reset
root.after(100, readSerial)

root.mainloop()

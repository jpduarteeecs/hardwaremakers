'''
Angklung Player by Juan Pablo Duarte, Dic 2016
This python program takes the data from an ultrasonic sensor and base on this data it plays a given note on an Angklung instrument
'''
from time import sleep #this library allows us to make stop in the execution of the program
import serial #this library is to connect using serial port, library pyserial is needed for this
from pydub import AudioSegment
from pydub.playback import play
import time

#Mina Azhar (Juan's wife) did all the mp3 conversion, thank you!
path = "/home/juan/research/hardwaremakers/labs_sp17/angklung/mp3files/" #change to your own path
fname = path+"low_do_long.mp3" #change to another note as needed
note = AudioSegment.from_mp3(fname)

ser = serial.Serial('/dev/ttyACM0', 9600) # Establish the connection on a specific port, for windows use COMX with X the port number

ser.write(str.encode('1')) #this let redbear duo to continue sending data

while True:#we use a "while True:" so the serial connection is always open

    #ser.write(bytearray(struct.pack("f", 5.1)))
    bytes_from_serial = ser.readline() #read serial, return a byte result
    print (bytes_from_serial.decode("utf-8") ) # print in serial form, it transform the byte data to string

    value_sensor = int(bytes_from_serial.decode("utf-8") ) #transfor data to a int number

    if (value_sensor<1000 ): #only distance signal less than 1000us
        ser.write(str.encode('0')) #this stop the redbear duo from sending new data
        play(note[:int(note.duration_seconds*value_sensor)]) #play sound
        ser.write(str.encode('1')) #this let redbear duo to continue sending data
    else:
        ser.write(str.encode('1')) #this let redbear duo to continue sending data

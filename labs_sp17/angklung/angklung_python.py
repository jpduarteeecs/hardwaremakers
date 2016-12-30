from time import sleep
import serial
ser = serial.Serial('/dev/ttyACM1', 9600) # Establish the connection on a specific port
counter = 32 # Below 32 everything in ASCII is gibberish
while True:
     counter +=1
     #ser.write(str(chr(counter))) # Convert the decimal number to ASCII then send it to the Arduino
     string_from_serial = ser.readline()
     print (string_from_serial[0:]) # Read the newest output from the Arduino
"""The b prefix in Python 3 just means that it is a bytes literal. It's not part of the output, that's just telling you the type.
The \r\n is a common Carriage-Return and Newline line-ending characters. You can remove that from your string by calling strip()."""
     sleep(.1) # Delay for one tenth of a second
     if counter == 255:
         counter = 32

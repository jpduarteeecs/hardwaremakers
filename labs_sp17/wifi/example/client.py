# client.py
import socket

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()
host = '192.168.1.146'
port = 23

# connection to hostname on the port.
s.connect((host, port))

while True:

    # Receive no more than 1024 bytes
    tm = s.recv(1024)
    print("The time got from the server is %s" % tm.decode('ascii'))


s.close()

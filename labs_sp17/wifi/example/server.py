# server.py
import socket
import time


# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #this is to be able to start the port 9996 again later without closing it



'''
#how to get local ip
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("gmail.com",80))
print(s.getsockname()[0])
s.close()'''
# get local machine name
host = "192.168.1.109"#socket.gethostname()
IP = socket.gethostbyname(host)
print(host)
print(IP)
port = 9996

# bind to the port
serversocket.bind((host, port))

# queue up to 5 requests
serversocket.listen(5)

state = 0
timeout_in_seconds=1


clientsocket,addr = serversocket.accept()
clientsocket.settimeout(5.0)
print("Got a connection from %s" % str(addr))
clientsocket.settimeout(5.0)
#currentTime = time.ctime(time.time()) + "\r\n"
#clientsocket.send(currentTime.encode('ascii'))

while True:
    if (state==0):
        stringtosend = "hello client" + "\r\n"
        clientsocket.send(stringtosend.encode('ascii'))

        try:
            tm = clientsocket.recv(1024)
            print("Data from client is: %s" % tm.decode('ascii'))


        except socket.timeout:
            print("timeout")
            continue


#clientsocket.close()

# Connecting Hardware Wireless: Wifi, Second Part

This week we are continuing learning the Server-Client Model from previous experience. In this case, we will locate the server in our PCs and a remote client in the RedBear Duos.

## WiFi for Server-Client Model (Review)

WiFi is a communication technology for wireless local area networking. It can be use for a Server-Client model, which is a distributed application structure that distributes tasks between servers (offer or deliver a particular service) and clients (request particular service).

![turnstile](pics/clientserver.png)

For exampple, a printer can be a server which is connected to a wireless network. Then, a computer, the client, send a request to the server, which print your work:

![turnstile](pics/Wi-Fi.gif)

## Creating a Server in Python

There are so many programming languages that can be use to create a server. We are going to use Python this time, but feel free to use whatever you want. A simple reference to code server-client in python can be found [here](http://www.bogotobogo.com/python/python_network_programming_server_client.php). Using this reference, we modified it to create a server that communicate to the client in our Redbear Duo (code [here]()):

```Python
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

```

## Creating a Client in a RedBear Duo

We want to send data from our hardware to our PCs. There are several ways to create server-client frameworks that can do this. Today, we will create a client in the RedBear duo that connects to a server and deliver/recieve data to the server it is connected (servert can be at your computer or any another development board).

Using WiFi technology, available in RedBear Duo and Particle Photon boards, we will connect to a local network. Then, we will create a client that connect to our server.

Compile and upload the following [code]() to your RedBear Duo board:


```Arduino

/*
 client example
 Juan Duarte
 */
#if defined(ARDUINO)
SYSTEM_MODE(SEMI_AUTOMATIC);
#endif

// your network name also called SSID
char ssid[] = "juanito";
// your network password
char password[] = "holahola";

// if you don't want to use DNS (and reduce your sketch size)
// use the numeric IP instead of the name for the server:
//IPAddress server(10,122,6,172);  // numeric IP for Google (no DNS)
char server[] = "192.168.1.109";    // name address for Google (using DNS)

// Initialize the Ethernet client library
// with the IP address and port of the server
// that you want to connect to (port 80 is default for HTTP):
TCPClient client;

void printWifiStatus();

void setup() {
  //Initialize serial and wait for port to open:
  Serial.begin(115200);

  // attempt to connect to Wifi network:
  Serial.print("Attempting to connect to Network named: ");
  // print the network name (SSID);
  Serial.println(ssid);

  // Connect to WPA/WPA2 network. Change this line if using open or WEP network:
  WiFi.on();
  WiFi.setCredentials(ssid,password);
  WiFi.connect();

  while ( WiFi.connecting()) {
    // print dots while we wait to connect
    Serial.print(".");
    delay(300);
  }

  Serial.println("\nYou're connected to the network");
  Serial.println("Waiting for an ip address");

  IPAddress localIP = WiFi.localIP();
  while (localIP[0] == 0) {
    localIP = WiFi.localIP();
    Serial.println("waiting for an IP address");
    delay(1000);
  }

  Serial.println("\nIP Address obtained");
  printWifiStatus();

  Serial.println("\nStarting connection to server...");
  // if you get a connection, report back via serial:
  if (client.connect(server, 9996)) {
    Serial.println("Connected to server");
    // Make a HTTP request:
    client.println("Hello Server");
    client.println("This is a student from DeCal HWMKS");
    client.println("I am trying to learn server-client framework");
    client.println();
  }
}

void loop() {
  // if there are incoming bytes available
  // from the server, read them and print them:
  while (client.available()) {
    Serial.print("client receive data: ");
    /*//only for a single character
    char c = client.read();
    Serial.write(c);*/
    //buffer input, so we recieve entire string
    char buffer[255] = {0};
    client.read((uint8_t*)buffer, client.available());
    Serial.println(buffer);    
  }

  // if the server's disconnected, stop the client:
  if (!client.connected()) {
    Serial.println();
    Serial.println("disconnecting from server.");
    client.stop();

    // do nothing forevermore:
    while (true);
  }
}

void printWifiStatus() {
  // print the SSID of the network you're attached to:
  Serial.print("SSID: ");
  Serial.println(WiFi.SSID());

  // print your WiFi shield's IP address:
  IPAddress ip = WiFi.localIP();
  Serial.print("IP Address: ");
  Serial.println(ip);

  // print the received signal strength:
  long rssi = WiFi.RSSI();
  Serial.print("signal strength (RSSI):");
  Serial.print(rssi);
  Serial.println(" dBm");
}
```
There are several parts that you need to understand from the previous code, head, setup, and main loop:

### Head Code

* We defined the name of the network and password using `ssid[]` and `password[]`, respectively
* A client was created. `TCPClient client` function was used, for details read [this](https://docs.particle.io/reference/firmware/photon/#tcpclient).
* Server address is needed `char server[] = "192.168.1.109";`. Check your IP address of your local computer (ask Juan for help).

### Setup Part

* WiFi was turned on, setup and connected using `WiFi.on()`,`  WiFi.setCredentials(ssid,password)`, and `WiFi.connect()`.
* Local IP is obtained using `WiFi.localIP()`. This address you need to later connect your client to this server.
* It connects to a server using `client.connect(server, port_number)`

### Loop Part

* The code check if client is connected to server using `client.available()`
* It buffer any data comming from server using `client.read((uint8_t*)buffer, client.available());`
* If connection is lost (`!client.connected()`), client is closed using `client.stop();`

Open your serial monitor and check if your client is able to connect to your server. 

## Acknowledgment
The material of today's experience was designed and tested by Juan Duarte.

## References:

* [SOCKETS - SERVER & CLIENT ](http://www.bogotobogo.com/cplusplus/sockets_server_client.php)
* [Python Server and Client](http://www.bogotobogo.com/python/python_network_programming_server_client.php)

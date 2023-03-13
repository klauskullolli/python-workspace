# server.py
import socket
import time

# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 9998

# bind to the port
serversocket.bind(("", port))

print('The server is ready to receive')

# queue up to 5 requests
serversocket.listen(5)

while True:
    # establish a connection
    clientsocket,addr = serversocket.accept()

    print("Got a connection from %s" % str(addr))
    currentTime = time.ctime(time.time())+ "\r\n"
    clientsocket.send(currentTime.encode('ascii'))
    clientsocket.close()
import socket

# Create a socket object
s = socket.socket()

# Define the port on which you want to connect
PORT = 1235

# connect to the server on local computer
s.connect(('127.0.0.1', PORT))

str = 'CEN 307 Computer'.encode()

s.send(str)     # data that the client will send to the server

# receive data from the server
data = s.recv(1024)

print(repr(data)) # print received data
# close the connection
s.close()
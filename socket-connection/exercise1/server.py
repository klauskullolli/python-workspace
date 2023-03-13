# first of all import the socket library
import socket

# next create a socket object
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print ("Socket successfully created")
except socket.error as err:
    print ("socket creation failed with error %s" %(err))

# reserve a port on your computer in our
PORT = 1235

# Next bind to the port
s.bind(('', PORT))

# put the socket into listening mode
s.listen()
print ("socket is listening")

# a forever loop until we interrupt it or
# an error occurs
while True:

   # Establish connection with client.
   c, addr = s.accept()
   print ('Got connection')

   data = c.recv(1024)   # receive the data from the client
   c.send(data)

   # Close the connection with the client
   c.close()

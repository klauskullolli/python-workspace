from socket import *
#create prot for connection
sP = 5000
#creat server socket
sS = socket(AF_INET, SOCK_STREAM)
#determine server name and the sokcet port
sS.bind(('127.0.0.1', sP))

# listen one request
sS.listen(1)
print('The server is ready to receive')
#server stays open 
while True:
    #welcome client socket and determine their address 
    conS, addr = sS.accept()
    sen = conS.recv(1024)
    #notify into the terminal the establishment of the connection 
    print(f"Connection from {addr} has been established")
    # input stream convert to upper 
    cap = sen.upper()
    # send to client back
    conS.send(cap)
    # close client connection 
    conS.close()

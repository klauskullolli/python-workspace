from socket import *

# determine server's name 
sName = '127.0.0.1'
# server socket port 
sP = 5000
# create client socket 
cS = socket(AF_INET, SOCK_STREAM)
# connect to the server to specified port
cS.connect(('127.0.0.1', sP))
print("Enter a message")
# input data from keyboard 
sentence = input()
# send data to server socket
cS.send(sentence.encode())
# recieve data from server 
modifiedS = cS.recv(1024)
# print the data steam coming from server 
print('From Server:', bytes.decode(modifiedS))
#  close socket
cS.close()

from socket import *

PORT = 3300
ADD = '127.0.0.1'
BUFF = 2048
serverADD = (ADD, PORT)

client_socket = socket(AF_INET, SOCK_DGRAM)

while(1):
    message = input('Please type a message: ')
    print('Sending message to ' +str(ADD)+' at port '+str(PORT))

    client_socket.sendto(message.encode(), serverADD)
    print('Message Sent')

    serverMessage = client_socket.recv(BUFF)
    print('Message from Server: ' + serverMessage.decode())


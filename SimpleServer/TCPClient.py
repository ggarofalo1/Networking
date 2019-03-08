from socket import *

'''
Description: a Simple TCP client that responds to a message
@Author: Galen Garofalo
Date: 1/8/19
'''

PORT = 3300
ADD = '127.0.0.1'
BUFF = 2048
serverADD = (ADD, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.settimeout(30)
client_socket.connect(serverADD)

while(1):
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.settimeout(30)
    try:
        client_socket.connect(serverADD)
    except ConnectionRefusedError:
        print('Refused connection')

    message = input('Please type a message: ')
    print('Sending message to ' +str(ADD)+' at port '+str(PORT))

    client_socket.send(message.encode())
    print('Message Sent')
    try:
        serverMessage = client_socket.recv(BUFF)
        print('Message from Server: ' + serverMessage.decode())
    except timeout:
        print('Server Did not respond..')

    quit = input("Would you like to quit(Y/N): ")
    if quit.lower() == 'y':
        print("Good Bye...")
        exit()

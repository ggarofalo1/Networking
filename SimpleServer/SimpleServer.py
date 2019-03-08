from socket import *

def processData(somestring):
    resultString = somestring.capitalize()
    return resultString

PORT = 3300
ADD = 'localhost'
servADD = (ADD, PORT)
BUFFER = 2040

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(servADD)
print("Server is Running...")

while(1):
    clientMessage, clientAddress = serverSocket.recvfrom(BUFFER)

    clientIP, clientPort = clientAddress

    outputMessage = processData(clientMessage.decode())

    print('Server sending '+ outputMessage + ' to IP address '+ clientIP + ' and port ' +clientIP)

    serverSocket.sendto(outputMessage.encode(), clientAddress)

    quit = input("Would you like to quit(Y/N): ")
    if quit.lower() == 'y':
        print("Good Bye...")
        exit()


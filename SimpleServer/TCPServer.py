from socket import *

def processData(somestring):
    if somestring.lower() == 'hello' or somestring.lower() == 'hi':
        resultString = 'Hello, I am a simple TCP Server nice to connect with you...'
    else:
        resultString = "What did you call me... I'm Terminating the connection!"
    return resultString

PORT = 3300
ADD = 'localhost'
servADD = (ADD, PORT)
BUFFER = 2048

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(servADD)
serverSocket.settimeout(40)
serverSocket.listen(3)

print("Server is Running...")

while(1):
    conSocket, clientAddress = serverSocket.accept()
    clientMessage = conSocket.recv(BUFFER)

    clientIP, clientPort = clientAddress

    outputMessage = processData(clientMessage.decode())

    print('Server sending '+ outputMessage + ' to IP address '+ clientIP + ' and port ' +clientIP)

    conSocket.send(outputMessage.encode())
    conSocket.close()

    quit = input("Would you like to quit(Y/N): ")
    if quit.lower() == 'y':
        print("Good Bye...")
        exit()


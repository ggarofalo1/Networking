# PingerServer.py
# We will need the following module to generate randomized lost packets
import random
import time
from socket import *

# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket(AF_INET, SOCK_DGRAM)

HOST = input('Enter host: ')
PORT = input('Enter port: ')
ENDTIME = 300

if not HOST:
    HOST= '127.0.0.1'
else:
    HOST= str(HOST)

if not PORT:
    PORT = 65535
else:
    PORT = int(PORT)

ADDR = (HOST, PORT)

# Assign IP address and port number to socket
serverSocket.bind(ADDR)
print('Server Started on: '+ str(ADDR))
print('Server Ready...')
Start = time.time()
Run= True
count =0

while (Run):
    if(time.time()-Start) > ENDTIME:
        SystemExit()
        continue

    # Generate random number in the range of 0 to 10
    rand = random.randint(0, 10)

    # Receive the client packet along with the address it is coming from
    message, address = serverSocket.recvfrom(1024)
    print('Connection['+str(count)+'] to: ' + str(address))

    # Capitalize the message from the client
    message = message.upper()

    # If rand is less is than 4, we consider the packet lost and do nothing
    if rand < 4:
        continue
    # Otherwise, the server responds
    serverSocket.sendto(message, address)
    count += 1

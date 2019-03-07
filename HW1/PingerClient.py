# PingerClient.py
# Used to send Ping packets to a server
# Name: Galen Garofalo
# Date: 2/23/19

import time
from socket import *

HOST = input('Enter host: ')
PORT = input('Enter port: ')
PING = input('How Many Pings: ')
userInput = input('Type Something: ')

# Sets the Input if no input given
if not HOST:
    HOST= '127.0.0.1'
else:
    HOST= str(HOST)

if not PORT:
    PORT = 65535
else:
    PORT = int(PORT)

if not PING:
    PING = 10
else:
    PING = int(PING)

if not userInput:
    userInput = 'Test'
else:
    userInput = str(userInput)


MAXBUFF = 1024
ADDR = (HOST, PORT)
client_socket = socket(AF_INET, SOCK_DGRAM)

# times out after 1 second
client_socket.settimeout(1)

# variables for time
timerStart = []
timerStop = []
pingTime =0

for i in range(PING):
    # Starts the timer and sends the ping msg
    timerStart.append(time.time())
    client_socket.sendto(userInput.encode(), ADDR)
    print('Sending msg['+ str(i) +'] to: '+str(ADDR))

    # waits for msg form server if timeout then set time to 0
    try:
        data = client_socket.recv(MAXBUFF)
        timerStop.append(time.time())
        pingTime = timerStop[i] - timerStart[i]

        print('Received msg['+ str(i)+ '] Time: ' +str(pingTime) +' Response: ', repr(data))
    except:
      print('Lost msg['+ str(i)+ '] Time: -')
      timerStop.append(0)



# variables for finding ping stats
totalTime = 0
lostPackets = 0
min = pingTime
max = pingTime

# Finds the ping stats for the test
for i in range(PING):
    if timerStop[i] == 0:
        lostPackets = lostPackets + 1
        continue
    ptime = timerStop[i] - timerStart[i]
    if (ptime) < min:
        min = ptime
    if ptime > max:
        max = ptime
    totalTime = totalTime + ptime

avgr = totalTime/(PING - lostPackets)
pLoss = (lostPackets/PING)*100

print('==============================')
print('Min RTT: ' + str(min))
print('Max RTT: ' + str(max))
print('Average RTT: ' + str(avgr))
print('Packet Loss: ' + str(pLoss) + '%')
print('===============================')
input('Press Enter To Quit...')

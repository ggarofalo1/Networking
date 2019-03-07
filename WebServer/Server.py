#import socket module
import socket
import time
import sys # In order to terminate the program

HOST = '127.0.0.1'
PORT = 65535
MAXBUFF = 1024

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Prepare a sever socket
#Fill in start
serverSocket.bind((HOST, PORT))
serverSocket.listen(5)
#Fill in end

while True:
    #Establish the connection
    print('Ready to serve...')
    print('Running on '+ str(serverSocket.getsockname()))
    print('Connect with: http://127.0.0.1:65535')
    connectionSocket, addr = serverSocket.accept() #Fill in start #Fill in end
    try:
        print('Connection to: ' + str(addr))
        start = time.time()
        #message = serverSocket.recv() #Fill in start #Fill in end
        #filename = message.split()[1]

        '''filename = serverSocket.recv(MAXBUFF)
        filename = bytes.decode(filename)
        print(str(filename))
        filename = filename.split(' ') # split on space "GET /file.html" -into-> ('GET','file.html',...)
        filename = filename[1]         # get 2nd element
        filename = filename.split('?')[0]   #Check for URL arguments. Disregard them

        if (filename == '/' |filename == '' ):  # in case no file is specified by the browser
                 filename = 'HelloWorld.html' # load index.html by default
        '''

        filename = '/HelloWorld.html'
        f = open(filename[1:], 'rb')
        outputdata = f.read()
        f.close()
        #Fill in start #Fill in end
        #Send one HTTP header line into socket
        #Fill in start
        current_date = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())
        header = 'HTTP/1.0 200 OK\r\n'
        header += 'Date: ' + current_date + '\r\n'
        header += 'Server: SimpleHTTPSever\r\n'
        header += 'Connection: open\r\n\r\n'
        serverResponse = header.encode() + outputdata
        #Fill in end
        #Send the content of the requested file to the client
        connectionSocket.send(serverResponse)

        if(time.time()-start) > 0.5:
            connectionSocket.close()
        print('Connection Closed')
    except IOError:
        #Send response message for file not found
        #Fill in start
        connectionSocket.send(b'HTTP/1.0 404 Not Found\r\n Content-Type: text/html\r\n\r\n <html><h1>404 Web Page Not Found</h1></html>')
        #Fill in end
        #Close client socket
        #Fill in start
        if(time.time()-start) > 0.5:
            connectionSocket.close()
        print('Connection Closed Error File Not Found')
        #Fill in end

serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data

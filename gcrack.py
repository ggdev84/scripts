# Programme de brute forcing de hashs MD5 / SHA256 / SHA512

import hashlib
import os, sys

def crck256(passs):
    test = hashlib.sha256(passs.encode()).hexdigest()
    if test == hashhs:
        return 1

def crck512(passs):
    test = hashlib.sha512(passs.encode()).hexdigest()
    if test == hashhs:
        return 1

def crckmd5(passs):
    test = hashlib.md5(passs.encode()).hexdigest()
    if test == hashhs:
        return 1

	
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

global hashhs, typehs
typehs = sys.argv[1]
wordlist = sys.argv[2]
hashhs = sys.argv[3]

if os.path.exists(wordlist) == False:
    print(bcolors.FAIL + "\nWordlist Not Found\n" + bcolors.ENDC)
    sys.exit(0)
filehs = open(wordlist,"r")

print("\nhash type : {0}\n".format(typehs))
print("hash : {0}\n".format(hashhs))
file = open(wordlist, "r")
password = file.readlines()
longueur = len(password)
print("Opening the file..\n\nTesting {0} passwords".format(longueur))
for i in password:
    passs = i.strip("\n")
    try:
        if typehs == "md5":
            response = crckmd5(passs)
        elif typehs == "sha256":
            response = crck256(passs)
        elif typehs == "sha512":
            response = crck512(passs)
        else:
            sys.exit(bcolors.FAIL + "No Valid Hash Type. Md5/Sha-256/Sha-512\n" + bcolors.ENDC)
    except KeyboardInterrupt:
        sys.exit("\nUser Interrupt\n")
    if response == 1:
        print(bcolors.BOLD + bcolors.OKGREEN + "\nPassword found : {0}\n".format(passs) + bcolors.ENDC)
        filehs.close()
        sys.exit("")

print(bcolors.WARNING + "\nNo Valid Password Found\n" + bcolors.ENDC)
filehs.close()

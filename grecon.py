# Programme de reconnaissance wi-fi et bluetooth.

import bluetooth
import wifi
import sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


print(bcolors.OKBLUE + "\n\
 ██████╗   ██████╗  ███████╗ ██████╗  ██████╗  ███╗    ██╗ \n\
 ██╔════╝  ██╔══██╗ ██╔════╝ ██╔════╝██╔═══██╗ ████╗   ██║\n \
██║  ███╗ ██████╔╝ █████╗   ██║     ██║   ██║ ██╔██╗  ██║\n \
██║   ██║ ██╔══██╗ ██╔══╝   ██║     ██║   ██║ ██║╚██╗ ██║\n \
╚██████╔╝ ██║  ██║ ███████╗╚██████╗ ╚██████╔╝ ██║  ╚████║\n \
 ╚═════╝  ╚═╝  ╚═╝ ╚══════╝ ╚═════╝  ╚═════╝  ╚═╝   ╚═══╝\n \
" + bcolors.ENDC)

if len(sys.argv) == 1:
	print("Usage : python3 grecon.py INTERFACE\n")
	exit()
interface = sys.argv[1]

bluetoothlist = []

wifilist = wifi.Cell.all(interface)

print(bcolors.WARNING + bcolors.UNDERLINE + bcolors.BOLD + "\nWIFI Access Points :\n" + bcolors.ENDC)

for ap in wifilist:
    if ap.encrypted == False:
        print(bcolors.FAIL + "[+] {}  {}  {}  {}".format(ap.ssid,ap.address,ap.signal,ap.encryption_type) + bcolors.ENDC)

    if ap.encrypted == True:
        if ap.encryption_type == "wep":
            print(bcolors.WARNING + "[+] {}  {}  {}  {}".format(ap.ssid,ap.address,ap.signal,ap.encryption_type) + bcolors.ENDC)

        if ap.encryption_type == "wpa" or ap.encryption_type == "wpa2":
            print(bcolors.OKGREEN + "[+] {}  {}  {}  {}".format(ap.ssid,ap.address,ap.signal,ap.encryption_type) + bcolors.ENDC)

bluetoothlist = bluetooth.discover_devices()
print(bcolors.OKBLUE + bcolors.UNDERLINE + bcolors.BOLD + "\nBluetooth Devices :\n" + bcolors.ENDC)

if len(bluetoothlist) == 0:
    print("No bluetooth device")
else:
	for bluedevice in bluetoothlist:
		print(bcolors.OKBLUE + "[+]  {}  {}".format(bluedevice,bluetooth.lookup_name(bluedevice)) + bcolors.ENDC)

print(bcolors.OKGREEN + "\n\nScan Done\n " + bcolors.ENDC)

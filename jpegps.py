# Programme qui permet de géolocaliser précisément une photo avec les données EXIF.

import urllib.request, shutil,os,sys
from geopy.geocoders import Nominatim
from PIL import Image
from pygeoexif import get_exif_data, get_lat_lon
import random, string

class colors:
    blue = '\033[94m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    end = '\033[0m'
    bold = '\033[1m'

def printmenu():
    print("MENU : \n1] Single JPG file\n2] Entier Folder\n3] Single JPG URL\n4] JPG URL List\n")

def findgeolocation(file1,images):
    latitude, longitude = get_lat_lon(get_exif_data(images))
    latandlon = str(latitude) + ", " + str(longitude)
    locate = Nominatim()
    location = locate.reverse(latandlon)
    print(colors.green + "\n### {} ###\n".format(file1) + colors.end)
    print(colors.green + location.address+"\n" + colors.end)
    print(colors.green + "########################\n"+ colors.end)


print(colors.bold + colors.blue + "\
\n \
\t\t ┬┌─┐┌─┐┌─┐┌─┐┌─┐ \n \
\t\t │├─┘├┤ │ ┬├─┘└─┐ \n \
\t\t└┘┴  └─┘└─┘┴  └─┘ \n \
" + colors.end)

i=0
try:
    while True:
        printmenu()
        choice = input("What's your choice ? > ")
# File which is on the system
        if choice == "1":
            try:
                file1 = input("File Location > ")
                images = Image.open(file1)
                try:
                    findgeolocation(file1,images)
                except:
                    print(colors.yellow + "[+] Can't get geolocation or locate the localisation\n"+colors.end)
            except:
                print(colors.yellow+"[+] Can't open file"+colors.end)
# Scan an entire folder on the computer
        elif choice == "2":

            directory = input("Enter directory > ")
            for root,dirs,files in os.walk(directory):
                for file1 in files:
                    if file1.endswith(".jpg"):
                        file2 = os.path.join(root,file1)
                        images = Image.open(file2)
                        try:
                            findgeolocation(file2,images)
                        except:
                            print(colors.yellow+ "[+]" + file2+ ": Can't get Geolocation"+colors.end)
# Download a file by URL and scan it
        if choice == "3":
            url = input("Enter URL > ")
            name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
            try:
                urllib.request.urlretrieve(url,name)
                try:
                    images = Image.open(name)
                    findgeolocation(name,images)
                except:
                    print(colors.yellow + "[+] Can't get geolocation or locate the localisation\n"+colors.end)
            except:
                print(colors.red+"[+] Can't get the file"+colors.end)

            finally:
                os.remove(name)

# Scan several jpg files with an url wordlist and scan all them
        elif choice == "4":
            folder = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
            os.mkdir(folder)
            os.chdir(folder)
            wordlist = input("Enter URL List > ")
            try:

                urllist = open(wordlist,"r")
                urls = urllist.readlines()
                try:
                    for url in urls:
                        try:
                            filename = str(i)+".jpg"
                            urllib.request.urlretrieve(url,filename)
                            images = Image.open(filename)
                            findgeolocation(filename,images)

                        except:
                            print(colors.yellow + "[+] " +filename +" : No geolocation in picture\n"+colors.end)
                        finally:
                            i+=1
                except:
                    pass
            except:
                print(colors.red+"[+] Can't open/find URL list"+colors.end)
            finally:
                os.chdir("..")
                shutil.rmtree(folder)
		


except KeyboardInterrupt:
    print(colors.green + "\nUser Exit"+colors.end)
    sys.exit()

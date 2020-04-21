# Fonctionnalité unshadow du brute forceur John recodé en Python.

temposh = []
finalwork = []
tempops = []
text = ""

shadow = open("/etc/shadow","r")
passwd = open("/etc/passwd","r")
shadowl = shadow.readlines()
passwdl = passwd.readlines()
for sh in shadowl:
    tempo = sh.split(":")
    temposh.append(tempo[0] + ":" + tempo[1])

for ps in passwdl:
    tempo = ps.split(":")
    tempo.remove(tempo[0])
    tempo.remove(tempo[0])
    a = ":".join(tempo)
    tempops.append(a)


for i in range(len(temposh)):
    finalwork.append(temposh[i] + ":" + tempops[i])

for i in finalwork:
    text += i

print(text)













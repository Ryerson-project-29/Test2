import getpass
import sys
import datetime
import time
import telnetlib

HOST = "10.10.10.102"

currentDT = datetime.datetime.now()
print("\n***************************")
print (str(currentDT))
print("Project29 second python code")


user = input("Enter remote account: \n")
password = getpass.getpass()
print ("You entered:", password)

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
print("Login username is: ",user)

tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"configure terminal\n")

#add loop to create vlan 2-9
for n in range (2,10):
    tn.write(b"vlan " + str(n).encode('ascii') + b"\n")
    tn.write(b"name Python_VLAN_" + str(n).encode('ascii') + b"\n")

tn.write(b"end\n")
tn.write(b"exit\n")
print(tn.read_all().decode('ascii'))

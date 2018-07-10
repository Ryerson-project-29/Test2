import telnetlib
import datetime
import time
import sys
import getpass

currentDT = datetime.datetime.now()
print("\n***************************")
print (str(currentDT))
print("Project29 first python code")

HOST = input("IP Address: ")

user = input("Enter remote account: \n")
password = getpass.getpass()
print ("You entered:", password)

tn = telnetlib.Telnet(HOST)

#tn.read_until(b"login: ")
tn.read_until(b"Username: ")
print("Login username is: ",user)

tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

# to make show run command show in full , not in seperated screen
tn.write(b"terminal length 0\n")

tn.write(b"show run\n\n")
tn.write(b"exit\n")
print(tn.read_all().decode('ascii'))

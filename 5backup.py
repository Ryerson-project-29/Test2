import telnetlib
import datetime
import time
import sys
import getpass

print("\n***************************")

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

tn.write(b"terminal length 0\n")
time.sleep(1)
tn.write(b"wr\n")
time.sleep(1)
print (1)

print(tn.read_very_eager().decode('ascii'))
#print(tn.read_all().decode('ascii'))

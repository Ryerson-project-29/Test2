import telnetlib
import datetime
import time
import sys
import getpass


print("\n***************************")

HOST = input("IP Address: \n")
user = input("Enter remote account: \n")
password = getpass.getpass()
print ("You entered:", password)

tn = telnetlib.Telnet(HOST)

#tn.read_until(b"Username: ")
tn.read_until(b"Username: ")
print("Username username is: ",user)

tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")
a=tn.read_until(b"Username: ",timeout=0.5)
if len(a)<=2:
    print ("wrong user or password")
else:
	tn.write(b"terminal length 0\n")
	tn.write(b"show ip int b\n\n")	
	tn.write(b"exit\n")
	print(tn.read_all().decode('ascii'))

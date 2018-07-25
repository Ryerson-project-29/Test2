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
tn.write(b"config t\n")
time.sleep(1)
print(tn.read_very_eager().decode('ascii'))
tn.write(b"int Ethernet0/1\n")
time.sleep(1)

print(tn.read_very_eager().decode('ascii'))
tn.write(b"ip address 10.10.11.4 255.255.255.0\n")
time.sleep(1)
#tn.write(b"no shutdown\n")

print(tn.read_very_eager().decode('ascii'))
#tn.write(b"exit\n")
tn.write(b"end\n")
time.sleep(1)

print(tn.read_very_eager().decode('ascii'))
#print(tn.read_all().decode('ascii'))

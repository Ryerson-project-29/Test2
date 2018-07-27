import telnetlib
import datetime
import time
import sys
import getpass

	def connetion(self):
		self.tn.read_until(b"Username: ")
		print("Username username is: ",self.user)
		self.tn.write(self.user.encode('ascii') + b"\n")
		if self.password:
    		self.tn.read_until(b"Password: ")
    		self.tn.write(self.password.encode('ascii') + b"\n")
		a=self.tn.read_until(b"Username: ",timeout=0.5)
		if len(a)<=2:
    		print ("wrong user or password")
    		else:
    		print ("%s Login successfully!"%(self.Username))
	
	def show_version(self):
		self.tn.write(b"terminal length 0\n")
		self.tn.write(b"show version\n\n")
		time.sleep(0.2)
		print(tn.read_very_eager().decode('ascii'))
		#self.tn.write(b"exit\n")
		#print(tn.read_all().decode('ascii'))

	def show_run(self):
		self.tn.write(b"terminal length 0\n")
		self.tn.write(b"show run\n\n")
		time.sleep(0.2)
		print(self.tn.read_very_eager().decode('ascii'))
		#self.tn.write(b"exit\n")
		#print(tn.read_all().decode('ascii'))

	def show_ip_int_b(self):
		self.tn.write(b"terminal length 0\n")
		self.tn.write(b"show ip int b\n\n")
		time.sleep(0.2)
		print(self.tn.read_very_eager().decode('ascii'))
		#self.tn.write(b"exit\n")
		#print(tn.read_all().decode('ascii'))

	def telnet_port_on(self,port):
		self.tn.write(b"terminal length 0\n")
		self.tn.write(b"config t\n")
		time.sleep(0.2)
		print(self.tn.read_very_eager().decode('ascii'))
		self.tn.write(b"int %s\n"%(port))
		time.sleep(0.2)
		print(self.tn.read_very_eager().decode('ascii'))
		self.tn.write(b"no shutdown\n")
		time.sleep(0.2)
		print(self.tn.read_very_eager().decode('ascii'))
		#tn.write(b"exit\n")
		self.tn.write(b"end\n")
		time.sleep(0.2)
		print(self.tn.read_very_eager().decode('ascii'))

	def telnet_port_down(self,port):
		self.tn.write(b"terminal length 0\n")
		self.tn.write(b"config t\n")
		time.sleep(1)
		print(self.tn.read_very_eager().decode('ascii'))
		self.tn.write(b"int %s\n"%(port))
		time.sleep(0.2)
		print(self.tn.read_very_eager().decode('ascii'))
		self.tn.write(b"shutdown\n")
		time.sleep(0.2)
		print(self.tn.read_very_eager().decode('ascii'))
		#tn.write(b"exit\n")
		self.tn.write(b"end\n")
		time.sleep(0.2)
		print(self.tn.read_very_eager().decode('ascii'))

	def telnet_set_ip(self,port,ip,mask):
		self.tn.write(b"terminal length 0\n")
		self.tn.write(b"config t\n")
		time.sleep(1)
		print(self.tn.read_very_eager().decode('ascii'))
		self.tn.write(b"int %s\n"%(port))
		time.sleep(0.5)
		print(self.tn.read_very_eager().decode('ascii'))
		tn.write(b"ip address %s %s\n"%(ip,mask))
		time.sleep(0.5)
		#tn.write(b"no shutdown\n")
		print(self.tn.read_very_eager().decode('ascii'))
		#tn.write(b"exit\n")
		self.tn.write(b"end\n")
		time.sleep(0.2)
		print(self.tn.read_very_eager().decode('ascii'))

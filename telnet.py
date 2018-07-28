import telnetlib
import datetime
import time
import sys
import getpass

class mytelnet():
	def __init__(self,HOST,user,password):
		self.Username = user
		self.password = password
		self.tn = telnetlib.Telnet(HOST)
	def connection(self):
		self.tn.read_until(b"Username: ")
		print("Username username is: ",self.Username)
		self.tn.write(self.Username.encode('ascii') + b"\n")
		if self.password:
			self.tn.read_until(b"Password: ")
			self.tn.write(self.password.encode('ascii') + b"\n")
		a=self.tn.read_until(b"Username: ",timeout=0)		
		if len(a)<=2:
			print ("wrong user or password")
		else:
			print ("%s Login successfully!"%(self.Username))
	def show_version(self):
		self.tn.write(b"terminal length 0\n")
		self.tn.write(b"show version\n\n")
		time.sleep(0.2)
		print(self.tn.read_very_eager().decode('ascii'))
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
		time.sleep(1)
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
		time.sleep(0.2)
		print(self.tn.read_very_eager().decode('ascii'))
		self.tn.write(b"ip address %s %s\n"%(ip,mask))
		time.sleep(0.2)

		#tn.write(b"no shutdown\n")
		print(self.tn.read_very_eager().decode('ascii'))
		#tn.write(b"exit\n")
		self.tn.write(b"end\n")
		time.sleep(0.2)
		print(self.tn.read_very_eager().decode('ascii'))
	def close_telnet(self):
		self.tn.close()
if __name__ == '__main__':
	test_telnet=mytelnet("10.10.10.3","admin","cisco1234")
	test_telnet.connection()
	print ("********************************")
	print ("show version start:")
	test_telnet.show_version()
	print ("********************************")
	print ("show run start:")
	test_telnet.show_run()
	print ("********************************")
	print ("show ip int b start:")
	test_telnet.show_ip_int_b()
	print ("********************************")
	print ("telnet port on start:")
	test_telnet.telnet_port_on("Ethernet0/1")
	print ("********************************")
	print ("telnet port down start:")
	test_telnet.telnet_port_down("Ethernet0/1")
	print ("********************************")
	print ("set ip start:")
	test_telnet.telnet_set_ip("Ethernet0/1","10.10.11.4","255.255.255.0")
	print ("********************************")
	print ("telnet  close start:")
	test_telnet.close_telnet()

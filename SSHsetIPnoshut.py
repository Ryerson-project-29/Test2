from netmiko import ConnectHandler

iosv_R2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.111.3',
    'username': 'admin',
    'password': 'cisco1234',
    }

net_connect = ConnectHandler(**iosv_R2)
#net_connect.find_prompt()

net_connect.find_prompt()

#output = net_connect.send_command("show ip int brief")
#print(output)

net_connect.enable()
net_connect.config_mode()
net_connect.send_config_set(["int e0/1","ip address 192.168.112.3 255.255.255.0","no shut"])
net_connect.exit_config_mode()
net_connect.exit_enable_mode()
output = net_connect.send_command("show ip int brief")
print(output)




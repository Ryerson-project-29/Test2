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

output = net_connect.send_command("show ip int brief")
print(output)




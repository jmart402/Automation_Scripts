from netmiko import ConnectHandler

R1 = {
	'device_type':'cisco_ios',
	'ip': '192.168.1.1',
	'username': 'admin',
	'password': 'pass123'
	
}

net_connect = ConnectHandler(**R1)

output = net_connect.send_command('show ip int brief')
print(output)

net_connect.disconnect()

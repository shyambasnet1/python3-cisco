from netmiko import ConnectHandler

iosv_l2_s4 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.120',
    'username': 'shyam',
    'password': 'cisco',
}

iosv_l2_s5 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.121',
    'username': 'shyam',
    'password': 'cisco',
}



with open('layer2') as f:
    lines = f.read().splitlines()
    print (lines)

all_devices = [iosv_l2_s4, iosv_l2_s5]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print (output)

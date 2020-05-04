from netmiko import ConnectHandler

with open('commands_file') as f:
    commands_list = f.read().splitlines()

devices_list = {'192.168.1.91', '192.168.1.92'}
for devices in devices_list:
    print ('Connecting to device" ' + devices)
    ip_address_of_device = devices
    ios_device = {
        'device_type': 'cisco_ios',
        'ip': ip_address_of_device,
        'username': 'shyam',
        'password': 'cisco'
    }

    net_connect = ConnectHandler(**ios_device)
    output = net_connect.send_config_set(commands_list)
    print (output)

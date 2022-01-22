from netmiko import ConnectHandler


with open('devices_file') as f:
    devices_list = f.read().splitlines()

for devices in devices_list:
    print ('Connecting to device" ' + devices)
    ip_address_of_device = devices
    ios_device = {
        'device_type': 'juniper',
        'ip': ip_address_of_device,
        'username': 'shyam',
        'password': 'cisco'
    }
    net_connect = ConnectHandler(**ios_device)
    output = net_connect.send_config_set(commands_list)
    print (output)

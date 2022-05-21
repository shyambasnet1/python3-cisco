https://docs.microsoft.com/en-us/cli/azure/azure-cli-vm-tutorial-3
    https://github.com/PaloAltoNetworks/azure/tree/master/two-tier-sample
from netmiko import ConnectHandler

iosv_l2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.92',
    'username': 'shyam',
    'password': 'cisco'
}

net_connect = ConnectHandler(**iosv_l2)
output = net_connect.send_command('show ip int brief')
print (output)

config_commands = ['int loop 0', 'ip address 1.1.1.1 255.255.255.0']
output = net_connect.send_config_set(config_commands)
print (output)

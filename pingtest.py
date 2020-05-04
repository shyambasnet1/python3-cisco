# import built-in os library

import os

# Open file for saving ping result to results.txt file
results_file = open("results.txt", "w")

# list of ip address to need to ping
ip_list = ["192.168.1.92", "8.8.8.8"]



# Loop to ping ip_list and check if device up or down
# Outputs to results.txt file
for ip in ip_list:
    response = os.popen(f"ping {ip} -c 5").read() # if windows use os.popen(f"ping {ip} -n 1)
    if "Received = 1" and "Approximate" in response:
        print(f"UP {ip} Ping Successful")
        results_file.write(f"UP {ip} Ping Successful" + "\n")
    else:
        print(f"Down {ip} Ping Unsuccessful")
        results_file.write(f"Down {ip} Ping Unsuccessful" + "\n")

# Close file when script completes
results_file.close()

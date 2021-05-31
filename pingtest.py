import os
from datetime import datetime
import time
import threading  #implements threading in Python
start = time.time()
with open ("device") as file:
    dump = file.read()
    dump = dump.splitlines()
    print(dump)

def ping(ip):
    res = os.popen(f"ping {ip} -c 3").read()
    if "100% packet loss" in res:
        print(f"down {ip} ")
    #else:
     #   print(f"up {ip}")
threads = list()

for ip in dump:
    th = threading.Thread(target=ping, args=(ip,))
    threads.append(th)  # appending the thread to the list
# starting the threads
for th in threads:
    th.start()

# waiting for the threads to finish
for th in threads:
    th.join()

end = time.time()


print(f'Total excecution time: {end-start}')


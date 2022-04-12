"""This program will gather basic system information from a windows operating system
Information includes current user,other user accounts,system info,running services, scheduled tasks,running process and
active network connections """


from datetime import datetime
import os
import subprocess
print("Date & Time : ",datetime.now())
windows = os.name
print("Current User : ",os.getlogin())
print("Accounts : ", subprocess.run(["net","user"]))
if windows == "nt":
    print("Operating System : Windows")
else:
    exit()
systeminfo = subprocess.run(["systeminfo"])
services = subprocess.run(["sc","query"])
scheduled_tasks = subprocess.run(["schtasks"])
network = subprocess.run(["netstat","-an"])
process = subprocess.run(["tasklist"])
print("============================================")

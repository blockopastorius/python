# TCP server. Might be useful for writing command shells or crafting a proxy.
# standard multi-threaded TCP server.
"""
a socket in networking is defined to be the unique identification to or 
from which information is transmitted in the network.
"""

import socket
import threading

IP = '0.0.0.0'
port = 9998

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT)) # pass ip and port to listen on
    server.listen(5) # start listening with maximum backlog of connections == 5
    print(f'[*] Accepted connection from {address[0]}:{address[1]}')
    client_handler = threading.Thread(target=handle_client, args=(client,))
    # wait for a client to connect
    while True:
        client, address = server.accept() # receive client socket in the client variable, and remote connection details in the address variable
        print(f'[*] Accepted connection from {address[0]}:{address[1]')
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()


def handle_client(client_socket):
    while client_socket as sock:
        request = sock.recv(1024)
        print(f'[*] Received: {request.decode("utf-8")}')
        sock.send(b'ACK')

if __name__ == '__main__':
    main()

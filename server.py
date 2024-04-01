# ****************************************************************************
#                         Activity #5
# Full Name: Franz Luiz Sy
# Student ID#: 116322223
# Email: fsy1@myseneca.ca
# Section: NCC
# Date Of Completion: 03/31/2024

# Authenticity Declaration:

# I declare that this submittion is the reslt of my own work and has not been
# shared to any other student or any 3rd party content distributer/provider.
# This submitted piece of work is entirely of my creation.

# ****************************************************************************

import socket
import threading


def acceptConn(clientConn, ClientAddress):
    """ Accepts connection and handles connection related tasks here """
    
    with clientConn:
        print(f'[SERVER] Connected by {ClientAddress}')
    
        while True:
        
            # Start receiving data from client    
            data = clientConn.recv(1024).decode('utf-8')
            if not data or data == "quit":
                break
        
            # Send back data to client
            clientConn.sendall(data)

        print(f'[SERVER] Connection with {ClientAddress} closed')

def start_Server(host='127.0.0.1', port=65432):
    """ Starts Socket server """

    MAX_CONN = 5
    listOfConns = []
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serverSock:
    
        # Avoids [Errno 48] when running server after immediately shutting it down
        serverSock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        # Binds socket 
        serverSock.bind((host, port))
        print(f'[SERVER] Started, listening on [{host} : {port}]')

        
        while True:
            if len(listOfConns) <= MAX_CONN:
                # Listens for connection
                serverSock.listen()
                        
                # Accepts a connection
                conn, addr = serverSock.accept()
                
                # Spawn connection Thread
                conn.sendall(b"Connected")
                currentThr = threading.Thread(target=acceptConn, args=(conn, addr)) # TODO: not working as intended
                currentThr.start()
                
                # Append to list of threads to keep track of current connections
                listOfConns.append(currentThr) # TODO: implement remove-threads-from-list-when-finished logic
            else:                
                print(f'[Server Log] Client {addr} attempted to connect, but server is full')
                conn.sendall(b'full')
                # conn.close() # rejects connection
                break

if __name__ == '__main__':
    start_Server()
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


def acceptConn(theConnetion : socket):
    
    # Accepts a connection
    conn, addr = theConnetion.accept()
    with conn:
        print(f'[SERVER] Connected by {addr}')
    
        while True:
        
            # Start receiving data from client    
            data = conn.recv(1024)                
            if not data or data == "quit":
                break

            # TODO: Implement QUIT logic. 
        
            # Send back data to client
            conn.sendall(data)

def start_Server(host='127.0.0.1', port=65432):

    MAX_CONN = 5
    CURR_CONNS = 0
    
    listOfConns = []
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serverSock:
    
        # Binds socket 
        serverSock.bind((host, port))
        print(f'[SERVER] Started, listening on [{host} : {port}]')

        
        while(CURR_CONNS <= MAX_CONN):
            
            # Listens for connection
            serverSock.listen()
            
            if(CURR_CONNS == MAX_CONN):
                tempConn, tempAddr = serverSock.accept()
                with tempConn:
                    print(f'[Server Log] Client {tempAddr} attempted to connect, but server is full')
                    tempConn.sendall(b'[Server] No more spare connections, try again later.')
            else:
                listOfConns.append(threading.Thread(target=acceptConn(serverSock)))
                CURR_CONNS = CURR_CONNS + 1
                listOfConns[CURR_CONNS - 1].start()
                # listOfConns[CURR_CONNS - 1].join()

if __name__ == '__main__':
    start_Server()
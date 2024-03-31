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

def start_Client(host='127.0.0.1', port=65432):
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as clientSock:
        
        # Connect to server
        try:
            clientSock.connect((host, port))

            while True:
                # Ask client to send a message to server
                print('[CLIENT] Enter your message for the server: ')
                x = input()
                clientSock.sendall(x.encode('utf-8'))
                
                # Recieve ACK from server
                data = clientSock.recv(1024)
                
                if data:
                    print(f'[CLIENT] Message from Server: "{data.decode()}"')
                else:
                    print(f'[CLIENT] Connection Terminated by Client')
                    break
            
            clientSock.close()
        
        except Exception as e:
            print(f'[CLIENT] Something went wrong, see error: \n"{e}"')

if __name__ == '__main__':
    start_Client()
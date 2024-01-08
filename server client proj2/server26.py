"""EX 2.6 server implementation
   Author:
   Date:
"""

import socket
import protocol
from datetime import datetime
import random


def create_server_rsp(cmd):
    """Based on the command, create a proper response"""
    if cmd == "time":
        now_str = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        response = now_str
    elif cmd == "whoru":
        response = "jonser"
    elif cmd == "rand":
        response = str(random.randint(0, 10))
    return response


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", protocol.PORT))
    server_socket.listen()
    print("Server is up and running")
    (client_socket, client_address) = server_socket.accept()
    print("Client connected")

    while True:
        # Get message from socket and check if it is according to protocol
        valid_msg, cmd = protocol.get_msg(client_socket)
        if valid_msg:
            # 1. Print received message
            # 2. Check if the command is valid
            # 3. If valid command - create response
            print("client sent: " + cmd)
            if cmd == "time" or cmd == "whoru" or cmd == "rand":
               response = create_server_rsp(cmd)
            else:
                response = "Wrong command"
        else:
            response = "Wrong protocol"
            client_socket.recv(1024)  # Attempt to empty the socket from possible garbage
        # Handle EXIT command, no need to respond to the client
        if cmd == "exit":
               response = "bye bye"
               created_msg = protocol.create_msg(response)
               client_socket.send(created_msg.encode())   
               break
        # Send response to the client
        created_msg = protocol.create_msg(response)
        client_socket.send(created_msg.encode())
        print("messege sent :)")
    print("Closing\n")
    # Close sockets
    client_socket.close()

if __name__ == "__main__":
    main()

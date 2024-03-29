"""EX 2.6 client implementation
   Author:
   Date:
"""

import socket
import protocol


def main():
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.connect(("127.0.0.1", protocol.PORT))

    while True:
        user_input = input("\n\n\nEnter onr command command\n rand\n whoru\n time\n exit\n\n\n")
        # Check if user entered a valid command as defined in protocol
        valid_cmd = protocol.check_cmd(user_input)


        if valid_cmd:
            # If the command is valid:
            # 1. Add length field ("RAND" -> "04RAND")
            # 2. Send it to the server
            # 3. If command is EXIT, break from while loop
            # 4. Get server's response
            # 5. If server's response is valid, print it
           created_msg = protocol.create_msg(user_input)
           my_socket.send(created_msg.encode())
           
           (check,msg) = protocol.get_msg(my_socket)
           if user_input == "exit":
                break
           elif check == True:
                print(msg)
           else:
                print("Response not valid\n")
        else:
            print("Not a valid command")
    my_socket.recv(1024)
    print("Closing\n")
    # Close socket
    my_socket.close()


if __name__ == "__main__":
    main()

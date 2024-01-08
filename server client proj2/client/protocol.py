"""EX 2.6 protocol implementation
   Author:
   Date:
"""

LENGTH_FIELD_SIZE = 2
PORT = 8820


def check_cmd(data):
    """Check if the command is defined in the protocol (e.g RAND, NAME, TIME, EXIT)"""
    if data == "exit" or data == "time" or data == "whoru" or data == "rand":
     return True


def create_msg(data):
    """Create a valid protocol message, with length field"""
    use_length = str(len(data))
    zfill_length = use_length.zfill(2)
    data = zfill_length + data
    return data


def get_msg(my_socket):
    """Extract message from protocol, without the length field
       If length field does not include a number, returns False, "Error" """
    check = my_socket.recv(2).decode()
    if int(check) > 0 and int(check)< 100:   
      return True, my_socket.recv(int(check)).decode()
    else:
      return False

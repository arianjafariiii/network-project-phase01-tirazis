import socket


# Check if a host is online
def is_host_online(host, port):
    try:
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set a timeout for the connection attempt
        s.settimeout(5)

        # Try to connect to the host
        s.connect((host, port))
        s.close()  # Close the socket if connection succeeds
        return True
    except socket.error:
        return False


host_to_check = 'google.com'
port_to_check = 80

if is_host_online(host_to_check, port_to_check):
    print(f"The host {host_to_check} is online")
else:
    print(f"The host {host_to_check} is offline")

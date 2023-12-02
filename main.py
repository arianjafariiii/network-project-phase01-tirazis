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
        return f"The host {host} is online"
    except socket.error:
        return f"The host {host} is offline"

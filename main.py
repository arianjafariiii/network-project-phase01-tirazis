import socket
import json


# Check if a host is online
def is_host_online(host):
    port = 80
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


def state():
    # Get entries and separate them to use them in function
    host = input("Enter host : ")
    ports_s = input("Enter ports : ")
    ports_l = ports_s.split(' ')
    ports = [int(e) for e in ports_l]
    # Run for each port
    for por in ports:
        check_port(host, por)


def check_port(host, port):
    # Make an object of socket to connect
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)

    # Check is the host online or not and if yes get other information
    try:
        sock.connect((host, port))
        # Get service of the port
        try:
            service_name = socket.getservbyport(port, 'tcp')
        except OSError:
            service_name = "Unknown"
        print(f"{host} is online      --port: {port}     --service: {service_name}")

    except socket.error:
        print(f"{host} is offline")
        return True
    finally:
        sock.close()


def send_get_request(host, port, user_in):
    # Connect to the server
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    # Format
    message = user_in
    client.send(message.encode())
    response = client.recv(1024)
    print(f"Response for user {user_input[8:10]}: {response.decode()}")

def post_user_to_server(server_url, user_data):
    host, port = server_url.split(':')
    port = int(port)
    request = f"POST {user_data}"

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        client_socket.sendall(request.encode())

        response = client_socket.recv(1024).decode()
        print(response)









# Main

Host = 'localhost'
Port = 8081
server_url = "localhost:8081"


print(is_host_online(Host), '55555')
while True:

    user_input = input()
    if 'GET' in user_input:
        send_get_request('localhost', 8081, user_input)
    elif 'POST' in user_input:
        
        post_user_to_server(server_url,user_input )      



# Example usage:



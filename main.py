import socket

host = input("Enter host : ")
ports_s = input("Enter ports")

ports_l = ports_s.split(' ')
ports = [int(e) for e in ports_l]



def check_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    try:
        sock.connect((host, port))
        print(f"Port {port} is open")
        service_name = socket.getservbyport(port, 'tcp')
        print(service_name)
    except socket.error:
        print(f"Port {port} is closed")
    finally:
        sock.close()

for por in ports:
    check_port(host, por)

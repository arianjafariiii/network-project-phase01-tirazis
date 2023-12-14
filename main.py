import socket
def state():
    #Get entries and seperate them to use them in function
    host = input("Enter host : ")
    ports_s = input("Enter ports : ")
    ports_l = ports_s.split(' ')
    ports = [int(e) for e in ports_l]
    #Run for each port
    for por in ports:
        check_port(host, por)
    




def check_port(host, port):
        
    #Make an object of socket to cannect
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

#Check is the host online or not and if yes get other information
    try:
        sock.connect((host, port))
        #Get service of the port
        service_name = socket.getservbyport(port, 'tcp')
        print(f"{host} is online      --port: {port}     --service: {service_name}"  )
        
    except socket.error:
        print(f"{host} is offline")
        return True
    finally:
        sock.close()



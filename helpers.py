import socket
import ipaddress

# function to get the ip address
def get_ip_address():
    my_ip = socket.gethostbyname(socket.gethostname())
    return my_ip

# function to get the subnet mask
def get_subnet_mask():
    my_ip = socket.gethostbyname(socket.gethostname())
    ip = ipaddress.ip_address(my_ip)
    return str(ipaddress.ip_network(ip, strict=False).netmask)

# function to get the network address
def get_network_address():
    my_ip = socket.gethostbyname(socket.gethostname())
    ip = ipaddress.ip_address(my_ip)
    return str(ipaddress.ip_network(ip, strict=False).network_address)

# function to get the broadcast address
def get_broadcast_address():
    my_ip = socket.gethostbyname(socket.gethostname())
    ip = ipaddress.ip_address(my_ip)
    return str(ipaddress.ip_network(ip, strict=False).broadcast_address)

# function to get the network range
def get_network_range():
    my_ip = socket.gethostbyname(socket.gethostname())
    ip = ipaddress.ip_address(my_ip)
    return str(ipaddress.ip_network(ip, strict=False).hosts())

# function to get the network range list
def get_network_range_list():
    my_ip = socket.gethostbyname(socket.gethostname())
    ip = ipaddress.ip_address(my_ip)
    return list(ipaddress.ip_network(ip, strict=False).hosts())

# function to check if an ip belongs to my network
def belongs_to_my_network(ip):
    my_ip = socket.gethostbyname(socket.gethostname())
    ip = ipaddress.ip_address(ip)
    return ip in ipaddress.ip_network(my_ip, strict=False)
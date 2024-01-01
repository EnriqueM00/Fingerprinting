import socket
import ipaddress


def get_ip_address():
    """
    Obtiene la dirección IP de la máquina local.

    Returns:
        str: La dirección IP de la máquina local.
    """
    my_ip = socket.gethostbyname(socket.gethostname())
    return my_ip


def get_subnet_mask():
    """
    Obtiene la máscara de subred de la dirección IP del host local.

    Returns:
        str: La máscara de subred en formato de cadena.
    """
    my_ip = socket.gethostbyname(socket.gethostname())
    ip = ipaddress.ip_address(my_ip)
    return str(ipaddress.ip_network(ip, strict=False).netmask)


def get_network_address():
    """
    Obtiene la dirección de red a partir de la dirección IP del host.

    Returns:
        str: La dirección de red en formato de cadena.
    """
    my_ip = socket.gethostbyname(socket.gethostname())
    ip = ipaddress.ip_address(my_ip)
    return str(ipaddress.ip_network(ip, strict=False).network_address)


def get_broadcast_address():
    """
    Obtiene la dirección de difusión de la red.

    Returns:
        str: La dirección de difusión de la red.
    """
    my_ip = socket.gethostbyname(socket.gethostname())
    ip = ipaddress.ip_address(my_ip)
    return str(ipaddress.ip_network(ip, strict=False).broadcast_address)


def get_network_range():
    """
    Obtiene el rango de red al que pertenece la dirección IP del host actual.

    Returns:
        str: El rango de red en formato CIDR.
    """
    my_ip = socket.gethostbyname(socket.gethostname())
    ip = ipaddress.ip_address(my_ip)
    return str(ipaddress.ip_network(ip, strict=False).hosts())


def get_network_range_list():
    """
    Obtiene una lista de direcciones IP dentro de la red actual.

    Returns:
        list: Lista de direcciones IP dentro de la red actual.
    """
    my_ip = socket.gethostbyname(socket.gethostname())
    ip = ipaddress.ip_address(my_ip)
    return list(ipaddress.ip_network(ip, strict=False).hosts())


def belongs_to_my_network(ip):
    """
    Comprueba si una dirección IP pertenece a la misma red que la dirección IP local.

    Args:
        ip (str): La dirección IP que se va a comprobar.

    Returns:
        bool: True si la dirección IP pertenece a la misma red, False en caso contrario.
    """
    my_ip = socket.gethostbyname(socket.gethostname())
    ip = ipaddress.ip_address(ip)
    return ip in ipaddress.ip_network(my_ip, strict=False)
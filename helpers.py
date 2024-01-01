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

result = get_ip_address()
print(result)
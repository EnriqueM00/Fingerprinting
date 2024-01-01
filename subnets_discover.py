import ipaddress

def calculate_subnets(network, prefixlen_diff=16):
    """
    Calcula todas las posibles subredes de una red padre.

    Parámetros:
    network (str): La red padre en formato CIDR.
    prefixlen_diff (int): La diferencia entre la longitud del prefijo de la red padre y la de las subredes. Por defecto es 16.

    Devuelve:
    list: Una lista de subredes en formato CIDR.
    """

    parent_network = ipaddress.ip_network(network, strict=False)
    subnets = list(parent_network.subnets(prefixlen_diff=prefixlen_diff))

    print("Subredes calculadas:")
    for subnet in subnets:
        print(subnet)

    return [str(subnet) for subnet in subnets]

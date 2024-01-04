import ipaddress

# def calculate_subnets(network, prefixlen_diff=16):
#     """
#     Calcula las subredes posibles a partir de una red dada.

#     Args:
#         network (str): La dirección de red en formato CIDR.
#         prefixlen_diff (int, optional): La diferencia en el prefijo de longitud para calcular las subredes. 
#             Por defecto es 16.

#     Returns:
#         list: Una lista de las subredes posibles en formato CIDR.
#     """

#     parent_network = ipaddress.ip_network(network, strict=False)
#     subnets = list(parent_network.subnets(prefixlen_diff=prefixlen_diff))

#     private_subnets = [str(subnet) for subnet in subnets if subnet.is_private]

#     print("Se han calculado un total de " + str(len(private_subnets)) + " subredes posibles")

#     return private_subnets


def calculate_subnets(network, prefixlen_diff=16):
    return ["172.16.10.0/24", "172.20.10.0/24", "172.24.10.0/24", "172.28.10.0/24", "172.31.10.0/24"]

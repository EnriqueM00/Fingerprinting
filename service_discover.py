import socket
import nmap
import threading
import concurrent.futures

def scan_port(ip, port, open_ports):
    """
    Escanea un puerto específico en una dirección IP para verificar si está abierto.

    Parámetros:
    ip (str): La dirección IP a escanear.
    port (int): El número de puerto a escanear.
    open_ports (list): Una lista de puertos abiertos encontrados durante el escaneo.

    Retorna:
    None
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((ip, port))
    if result == 0:
        open_ports.append(port)
    sock.close()

def scan_ports(ip):
    """
    Escanea la dirección IP especificada en busca de puertos abiertos.

    Args:
        ip (str): La dirección IP a escanear.

    Returns:
        list: Una lista de puertos abiertos encontrados durante el escaneo.
    """
    open_ports = []
    ports_to_scan = range(1, 65535)

    with concurrent.futures.ThreadPoolExecutor(max_workers=1000) as executor:
        future_to_port = {executor.submit(scan_port, ip, port, open_ports): port for port in ports_to_scan}
        for future in concurrent.futures.as_completed(future_to_port):
            pass

    return open_ports
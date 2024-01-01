import socket
import nmap
import threading

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
    Escanea los puertos de una dirección IP dada y devuelve una lista de puertos abiertos.

    Args:
        ip (str): La dirección IP a escanear.

    Returns:
        list: Una lista de puertos abiertos.
    """
    open_ports = []
    threads = []

    for port in range(1, 65535):
        thread = threading.Thread(target=scan_port, args=(ip, port, open_ports))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    return open_ports
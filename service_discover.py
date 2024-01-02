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

scan_ports_max_workers = 1000 
# Número máximo de hilos a utilizar para escanear puertos
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

    with concurrent.futures.ThreadPoolExecutor(max_workers=scan_ports_max_workers) as executor:
        future_to_port = {executor.submit(scan_port, ip, port, open_ports): port for port in ports_to_scan}
        for future in concurrent.futures.as_completed(future_to_port):
            pass
    print("Puertos abiertos: " + str(open_ports))
    return open_ports


def scan_service(ip, port):
    """
    Escanea un servicio en una dirección IP y puerto específicos utilizando Nmap.

    Parámetros:
    - ip (str): La dirección IP del host a escanear.
    - port (int): El número de puerto del servicio a escanear.

    Retorna:
    - tuple: Una tupla que contiene el número de puerto y el nombre del servicio escaneado.
             Si no se encuentra el nombre del servicio, se devuelve el valor 'Desconocido'.
    """
    nm = nmap.PortScanner()
    res = nm.scan(ip, str(port))
    if 'scan' in res and ip in res['scan'] and 'tcp' in res['scan'][ip] and port in res['scan'][ip]['tcp'] and 'name' in res['scan'][ip]['tcp'][port]:
        return port, res['scan'][ip]['tcp'][port]['name']
    else:
        return port, 'Desconocido'

scan_services_max_workers = 100
# Número máximo de hilos a utilizar para escanear servicios
def scan_services(ip, ports):
    """
    Escanea la dirección IP especificada en busca de puertos abiertos y devuelve un diccionario de servicios que se ejecutan en esos puertos.

    Parámetros:
    ip (str): La dirección IP a escanear.
    ports (list): Una lista de puertos a escanear.
    """
    services = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=scan_services_max_workers) as executor:
        future_to_port = {executor.submit(scan_service, ip, port): port for port in ports}
        for future in concurrent.futures.as_completed(future_to_port):
            port, service = future.result()
            services[port] = service
    return services
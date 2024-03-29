import logging
from scapy.all import  ICMP, IP, sr, srp, Ether, ARP, conf
from helpers import *
from concurrent.futures import ThreadPoolExecutor
import concurrent.futures
import socket
import nmap

#Evitar que scapy imprima mensajes de warning en la consola 
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

# Configuracion global de el valor de verbosidad de scapy
# 0 = false
# 1 = true
conf.verb = 0

network_verbose = 0 #Nivel de verbosidad de la funcion 
network_timeout = 5 #Tiempo de espera para obtener la MAC de un dispositivo
def scan_ip(ip):
    """
    Realiza un escaneo de una dirección IP utilizando el protocolo ICMP.

    Args:
        ip (str): La dirección IP a escanear.

    Returns:
        dict: Un diccionario que contiene la dirección IP y la dirección MAC del dispositivo encontrado.
    """
    paquete = IP(dst=ip)/ICMP()
    result = sr(paquete, timeout=network_timeout, verbose=network_verbose)[0]

    for sent, received in result:
        if belongs_to_my_network(received.src):
            return {'ip': received.src, 'mac': obtain_mac(received.src)}
        else:
            return {'ip': received.src, 'mac': 'Desconocida'}

network_scan_max_workers = 100 # Número máximo de hilos a utilizar para escanear la red
def network_scan(subred):
    """
    Realiza un escaneo de red utilizando el protocolo ICMP para descubrir dispositivos activos en la subred especificada.

    Args:
        subred (str): La subred a escanear en formato CIDR (ejemplo: '192.168.0.0/24').

    Returns:
        list: Una lista de diccionarios que contienen la dirección IP y la dirección MAC de los dispositivos encontrados en la subred.
    """
    # Crea una lista de todas las direcciones IP en la subred
    network = ipaddress.ip_network(subred)
    ip_addresses = [str(ip) for ip in network.hosts()]

    devices = []

    # Crea un pool de hilos y realiza un escaneo de cada dirección IP en la subred
    with ThreadPoolExecutor(max_workers=network_scan_max_workers) as executor:
        future_to_ip = {executor.submit(scan_ip, ip): ip for ip in ip_addresses}
        for future in concurrent.futures.as_completed(future_to_ip):
            ip = future_to_ip[future]
            try:
                device = future.result()
                devices.append(device)
            except Exception as exc:
                print(f'La dirección IP {ip} generó una excepción: {exc}')

    if len(devices) == 0:
        return None
    else:
        return devices



mac_timeout = 5 #Tiempo de espera para obtener la MAC de un dispositivo
mac_retry = 2 #Numero de intentos para obtener la MAC de un dispositivo
mac_verbose = 0 #Nivel de verbosidad de la funcion srp
def obtain_mac(ip):
    """
    Obtiene la dirección MAC de un dispositivo dado su dirección IP.

    Parámetros:
    ip (str): La dirección IP del dispositivo.

    Retorna:
    str: La dirección MAC del dispositivo, o None si no se pudo obtener.
    """
    try:
        reply, _ = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip), timeout=mac_timeout, retry=mac_retry, verbose=mac_verbose)
        for _, r in reply:
            return r[Ether].src
    except Exception as e:
        print(f"Error al obtener la dirección MAC de {ip}: {e}")
    return None

def get_hostname(ip):
    """
    Obtiene el nombre del host de la dirección IP especificada.

    Args:
        ip (str): La dirección IP.

    Returns:
        str: El nombre del host, o None si no se pudo determinar.
    """
    try:
        host_name = socket.gethostbyaddr(ip)[0]
        return host_name
    except socket.herror:
        print("No se pudo determinar el nombre del host para la IP " + ip)
        return None
    
def get_os(ip):
    """
    Intenta determinar el sistema operativo del host en la dirección IP especificada.

    Args:
        ip (str): La dirección IP del host.

    Returns:
        str: El sistema operativo del host, o None si no se pudo determinar.
    """
    nm = nmap.PortScanner()
    try:
        res = nm.scan(ip, arguments='-O')
        if 'osmatch' in res['scan'][ip]:
            os = res['scan'][ip]['osmatch'][0]['name']
            return os
        else:
            print("No se pudo determinar el sistema operativo para la IP " + ip)
            return None
    except Exception as e:
        print("Error al escanear la IP " + ip + ": " + str(e))
        return None
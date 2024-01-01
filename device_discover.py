import logging
from scapy.all import  ICMP, IP, sr, srp, Ether, ARP, conf
from helpers import *

#Evitar que scapy imprima mensajes de warning en la consola 
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

# Configuracion global de el valor de verbosidad de scapy
# 0 = false
# 1 = true
conf.verb = 0

network_verbose = 0 #Nivel de verbosidad de la funcion 
network_timeout = 5 #Tiempo de espera para obtener la MAC de un dispositivo
def network_scan(subred):
    """
    Realiza un escaneo de red utilizando el protocolo ICMP para descubrir dispositivos activos en la subred especificada.

    Args:
        subred (str): La subred a escanear en formato CIDR (ejemplo: '192.168.0.0/24').

    Returns:
        list: Una lista de diccionarios que contienen la dirección IP y la dirección MAC de los dispositivos encontrados en la subred.
    """
    paquete = IP(dst=subred)/ICMP()
    result = sr(paquete, timeout=network_timeout, verbose=network_verbose)[0]

    devices = []

    for sent, received in result:
        if belongs_to_my_network(received.src):
            devices.append({'ip': received.src, 'mac': obtain_mac(received.src)})
        else:
            devices.append({'ip': received.src, 'mac': 'Desconocida'})

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
    str: La dirección MAC del dispositivo.
    """
    reply, not_reply = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip), timeout=mac_timeout, retry=mac_retry, verbose=mac_verbose)
    for s, r in reply:
        return r[Ether].src
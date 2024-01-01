from scapy.all import  ICMP, IP, sr, srp, Ether, ARP, conf
from helpers import *

# Configuracion global de el valor de verbosidad de scapy
# 0 = false
# 1 = true
conf.verb = 0

network_verbose = 0 #Nivel de verbosidad de la funcion 
network_timeout = 5 #Tiempo de espera para obtener la MAC de un dispositivo
def network_scan(subred):
    paquete = IP(dst=subred)/ICMP()
    result = sr(paquete, timeout=network_timeout, verbose=network_verbose)[0]

    devices = []

    for sent, received in result:
        if belongs_to_my_network(received.src):
            devices.append({'ip': received.src, 'mac': obtain_mac(received.src)})
        else:
            devices.append({'ip': received.src, 'mac': None})

    return devices



mac_timeout = 5 #Tiempo de espera para obtener la MAC de un dispositivo
mac_retry = 2 #Numero de intentos para obtener la MAC de un dispositivo
mac_verbose = 0 #Nivel de verbosidad de la funcion srp
def obtain_mac(ip):
    reply, not_reply = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip), timeout=mac_timeout, retry=mac_retry, verbose=mac_verbose)
    for s, r in reply:
        return r[Ether].src
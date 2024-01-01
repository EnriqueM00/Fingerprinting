from script_scan import *

from scapy.all import ARP, Ether, srp

def escanear_red(subred):
    arp = ARP(pdst=subred)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    paquete = ether/arp

    resultado = srp(paquete, timeout=3, verbose=0)[0]

    dispositivos = []

    for sent, received in resultado:
        dispositivos.append({'ip': received.psrc, 'mac': received.hwsrc})

    return dispositivos

# Ejemplo de uso
dispositivos = escanear_red("172.0.0.0/24")
for dispositivo in dispositivos:
    print("IP: {}, MAC: {}".format(dispositivo['ip'], dispositivo['mac']))
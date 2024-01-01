from scapy.all import ARP, Ether, srp


def network_scan(subred):
    arp = ARP(pdst=subred)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    paquete = ether/arp

    resultado = srp(paquete, timeout=3, verbose=0)[0]

    devices = []

    for sent, received in resultado:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})

    return devices
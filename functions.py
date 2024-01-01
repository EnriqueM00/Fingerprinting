from scapy.all import  ICMP, IP, sr, srp, Ether, ARP


def network_scan(subred):
    paquete = IP(dst=subred)/ICMP()
    resultado = sr(paquete, timeout=2, verbose=0)[0]

    dispositivos = []

    for sent, received in resultado:
        dispositivos.append({'ip': received.src, 'mac': obtener_mac(received.src)})

    return dispositivos

def obtener_mac(ip):
    respuestas, no_respuestas = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip), timeout=2, retry=10, verbose=0)
    for s, r in respuestas:
        return r[Ether].src
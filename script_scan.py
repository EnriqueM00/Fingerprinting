# from scapy.all import ARP, Ether, srp
# import nmap

# def mapports(ip, port):
#     nm = nmap.PortScanner()
#     res = nm.scan(ip, port, "-sV", True)
#     res = res['scan'][ip]

#     if res['tcp'][int(port)]['state'] == 'open':
#         return res['tcp'][int(port)]['name']
#     else:
#         return None


# def scan(ip):
#     arp = ARP(pdst=ip)  # Crear una solicitud ARP
#     ether = Ether(dst="ff:ff:ff:ff:ff:ff")  # Crear un paquete Ethernet
#     packet = ether/arp  # Apilar los dos paquetes

#     result = srp(packet, timeout=3, verbose=0)[0]

#     # Una lista de dispositivos encontrados, cada dispositivo es un diccionario
#     devices = []

#     for sent, received in result:
#         devices.append({'ip': received.psrc, 'mac': received.hwsrc})

#     return devices


# def main():
#     #Direciones a escanear
#     directions = ["172.16.10.0/24", "172.20.10.0/24", "172.24.10.0/24", "172.28.10.0/24", "172.31.10.0/24"]
#     devices = []
#     for direction in directions:
#         devices += scan(direction)

#     print("Dispositivos encontrados:")
#     print("IP" + " "*18+"MAC")
#     for device in devices:
#         print("{:16}    {}".format(device['ip'], device['mac']))

#         for port in range(1, 65.535):
#             result = mapports(device, str(port))
#             print(result)


# main()

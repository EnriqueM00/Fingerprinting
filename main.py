from script_scan import *

from scapy.all import ARP, Ether, srp

# Direciones a escanear
directions = ["172.16.10.0/24", "172.20.10.0/24", "172.24.10.0/24", "172.28.10.0/24", "172.31.10.0/24"]
devices = []
for direction in directions:
    devices += scan(direction)

    print("Dispositivos encontrados:")
    print("IP" + " "*18+"MAC")
    for device in devices:
        print("{:16}    {}".format(device['ip'], device['mac']))

        for port in range(1, 65.535):
            result = mapports(device, str(port))
            print(result)
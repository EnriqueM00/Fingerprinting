from functions import *



#Direciones a escanear
directions = ["172.16.10.0/24", "172.20.10.0/24", "172.24.10.0/24", "172.28.10.0/24", "172.31.10.0/24"]
devices = []
for direction in directions:
    devices += network_scan(direction)

    print("Dispositivos encontrados:")
    print("IP" + " "*18+"MAC")
    for device in devices:
        print("{:16}    {}".format(device['ip'], device['mac']))


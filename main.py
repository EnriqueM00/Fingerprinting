from device_discover import *
from service_discover import *



#Direciones a escanear
directions = ["172.16.10.0/24", "172.20.10.0/24", "172.24.10.0/24", "172.28.10.0/24", "172.31.10.0/24"]
devices = {}
for direction in directions:
    print("Escaneando red " + direction)
    print("Progreso: " + str(directions.index(direction)) + "/" + str(len(directions)) + " redes escaneadas")
    devices[direction] = network_scan(direction)

    print("Dispositivos encontrados en la red " + direction +" :")
    print("IP" + " "*18+"MAC")
    for device in devices[direction]:
        print("{:16}    {}".format(device['ip'], device['mac']))

    print("Escaneando servicios de la red " + direction)

    open_ports = scan_ports(direction)
    services = scan_services(direction, open_ports)
    print("Puertos abiertos y servicios:")
    for port, service in services.items():
        print(f"Puerto: {port}, Servicio: {service}")



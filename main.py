from device_discover import *
from service_discover import *
from write_report import *


#Direciones a escanear
directions = ["172.16.10.0/24", "172.20.10.0/24", "172.24.10.0/24", "172.28.10.0/24", "172.31.10.0/24"]
devices = {}
generate_txt_file("reporte.txt", "Reporte de escaneo de red")
for direction in directions:
    print("Escaneando red " + direction)
    add_line_to_txt_file("reporte.txt", "Red " + direction)
    print("Progreso: " + str(directions.index(direction)) + "/" + str(len(directions)) + " redes escaneadas")
    devices[direction] = network_scan(direction)

    print("Dispositivos encontrados en la red " + direction +" :")
    print("IP" + " "*18+"MAC")
    for device in devices[direction]:
        print("{:16}    {}".format(device['ip'], device['mac']))
        add_line_to_txt_file("reporte.txt", "{:16}    {}".format(device['ip'], device['mac']))
        print("Escaneando servicios de la ip " + device['ip'])
    
        ip = device['ip']
        open_ports = scan_ports(ip)
        services = scan_services(ip, open_ports)
        print("Puerto" + " "*10 + "Servicio")
        add_line_to_txt_file("reporte.txt", "Puerto" + " "*10 + "Servicio")
        for port, service in services.items():
            print("{:5}    {}".format(port, service))
            add_line_to_txt_file("reporte.txt", "{:5}    {}".format(port, service))



from device_discover import *
from service_discover import *
from write_report import *
from subnets_discover import *

#Direciones a escanear
directions = calculate_subnets("172.0.0.0/8")
devices = {}
generate_txt_file("reporte.txt", "Reporte de escaneo de red")
for direction in directions:
    print("Escaneando red " + direction)
    add_line_to_txt_file("reporte.txt", "Red " + direction)
    print("Progreso: " + str(directions.index(direction)) + "/" + str(len(directions)) + " redes escaneadas")
    result = network_scan(direction)
    if result != None:
        devices[direction] = result

        print("Dispositivos encontrados en la red " + direction +" :")
        print("IP" + " "*18+"MAC")
        for device in devices[direction]:
            print("{:16}                  {}".format(device['ip'], device['mac']))
            add_line_to_txt_file("reporte.txt", "IP: {} ".format(device['ip']))
            add_line_to_txt_file("reporte.txt", "MAC: {} ".format(device['mac']))
            print("Escaneando servicios de la ip " + device['ip'])
        
            ip = device['ip']
            open_ports = scan_ports(ip)
            services = scan_services(ip, open_ports)
            print("Puerto" + " "*10 + "Servicio")
            add_line_to_txt_file("reporte.txt", "Puerto" + " "*10 + "Servicio")
            for port, service in services.items():
                print("{:5}          {}".format(port, service))
                add_line_to_txt_file("reporte.txt", "{:5}          {}".format(port, service))
    else:
        print("No se encontraron dispositivos en la red " + direction)
        add_line_to_txt_file("reporte.txt", "No se encontraron dispositivos en la red " + direction)

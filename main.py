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
    add_line_to_txt_file("reporte.txt", "*"*40 )
    add_line_to_txt_file("reporte.txt", "Red " + direction)
    add_line_to_txt_file("reporte.txt", "*"*40 )
    print("Progreso: " + str(directions.index(direction)) + "/" + str(len(directions)) + " redes escaneadas")
    result = network_scan(direction)
    if result != None:
        devices[direction] = result

        print("Dispositivos encontrados en la red " + direction +" :")
        for device in devices[direction]:
            if device is not None:
                print("-"*60)
                add_line_to_txt_file("reporte.txt", "-"*40)
                print("IP: {} ".format(device['ip']))
                add_line_to_txt_file("reporte.txt", "IP: {} ".format(device['ip']))
                add_line_to_txt_file("reporte.txt", "MAC: {} ".format(device['mac']))
                host_name = get_hostname(ip)
                if host_name is not None:
                    print("Nombre del host: " + host_name)
                    add_line_to_txt_file("reporte.txt", "Nombre del host: " + host_name)
                os = get_os(ip)
                if os is not None:
                    print("Sistema operativo: " + os)
                    add_line_to_txt_file("reporte.txt", "Sistema operativo: " + os)

                print("Escaneando servicios de la ip " + device['ip'])
            
                ip = device['ip']
                open_ports = scan_ports(ip)
                if open_ports == "honeypot_detected":
                    print("Todos los puertos están abiertos. Esto podría ser un honeypot.")
                    add_line_to_txt_file("reporte.txt", "Todos los puertos están abiertos. Esto podría ser un honeypot.")
                elif len(open_ports) == 0:
                    print("No se encontraron puertos abiertos en la ip " + ip)
                    add_line_to_txt_file("reporte.txt", "No se encontraron puertos abiertos en la ip " + ip)
                else:
                    services = scan_services(ip, open_ports)
                    print("Puerto" + " "*10 + "Servicio")
                    add_line_to_txt_file("reporte.txt", "Puerto" + " "*10 + "Servicio")
                    for port, service in services.items():
                        print("{:5}          {}".format(port, service))
                        add_line_to_txt_file("reporte.txt", "{:5}          {}".format(port, service))

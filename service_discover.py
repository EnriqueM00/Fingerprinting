import socket
import nmap

def scan_ports(ip):
    open_ports = []
    for port in range(1, 65535):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        print("Escaneando ip " + ip + " puerto " + str(port))
        print(f"Escaneando puerto {port}")
        result = sock.connect_ex((ip, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

def scan_services(ip, ports):
    nm = nmap.PortScanner()
    services = {}
    for port in ports:
        res = nm.scan(ip, str(port))
        res = res['scan'][ip]['tcp'][port]['name']
        services[port] = res
    return services
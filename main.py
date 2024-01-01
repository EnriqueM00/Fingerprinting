from functions import *



devices = network_scan("172.0.0.0/24")
for device in devices:
    print("IP: {}, MAC: {}".format(device['ip'], devices['mac']))


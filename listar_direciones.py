import socket

def get_local_ips():
    ips = []
    hostname = socket.gethostname()
    ip_addresses = socket.getaddrinfo(hostname, None)
    
    for address in ip_addresses:
        ip = address[4][0]
        if ip not in ips:
            ips.append(ip)
    
    return ips

if __name__ == "__main__":
    local_ips = get_local_ips()
    for ip in local_ips:
        print(ip)
        
from scapy.all import ARP, Ether, srp
import socket

def get_local_ip():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    return local_ip

def get_subnet(ip):
    return '.'.join(ip.split('.')[:-1]) + '.0/24'

def scan_network(subnet):
    arp = ARP(pdst=subnet)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp

    result = srp(packet, timeout=2, verbose=0)[0]

    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})

    return devices

if __name__ == "__main__":
    local_ip = get_local_ip()
    subnet = get_subnet(local_ip)
    devices = scan_network(subnet)

    print("Dispositivos en la red:")
    for device in devices:
        print(f"IP: {device['ip']}, MAC: {device['mac']}")
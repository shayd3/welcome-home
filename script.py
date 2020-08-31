import nmap
import time

DEVICE_IP = '192.168.1.161'

while(True):
    # Initiate nmap, make nmap usable
    nm = nmap.PortScanner()

    # Perform scan - Scan local subnet - -n: Always resolve -PE: ICMP echo, -PA: TCP ACK to given ports
    nm.scan(hosts='192.168.1.0/24', arguments='-n -sP -PE -PA21,23,80,3389')

    # Parse scan results, get list of hosts
    hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]

    print(hosts_list)
    time.sleep(3)

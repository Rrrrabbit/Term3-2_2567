#!/usr/bin/python3  
from scapy.all import *  
import time
	  
ID     = 1000  
dst_ip = "10.9.0.5"
  
# Fragment No.1 (Fragment offset: 0)  
udp = UDP(sport=7070, dport=9090, chksum=0)  
udp.len = 8 + 72 + 80 + 80 + 68

ip = IP(dst=dst_ip, id=ID, frag=0, flags=1)   
payload = "A" * 71 + "\n"  
pkt1 = ip/udp/payload  
	  
# Fragment No.2 (Fragment offset: (8 + 72)/8 = 10)
ip = IP(dst=dst_ip, id=ID, frag=10, flags=1)   
ip.proto = 17 
payload  = "B" * 79 + "\n"  
pkt2 = ip/payload  

# Fragment No.3 (Fragment offset: (8 + 72 + 80)/8 = 20)
ip = IP(dst=dst_ip, id=ID, frag=20, flags=0)   
ip.proto = 17  
payload  = "C" * 79 + "\n"  
pkt3 = ip/payload

# Fragment No.4 (Fragment offset: (8 + 72 + 80 + 80)/8 = 30)
ip = IP(dst=dst_ip, id=ID, frag=30, flags=0)   
ip.proto = 17  
payload  = "D" * 67 + "\n"  
pkt4 = ip/payload

# Sending fragments
send(pkt1)
send(pkt2)
send(pkt3)
send(pkt4)

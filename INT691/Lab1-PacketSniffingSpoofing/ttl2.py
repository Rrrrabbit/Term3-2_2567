#!/usr/bin/env python3
from scapy.all import *

ip = IP()
ip.dst = sys.argv[1]
ttl = 1

while True:
  ip.ttl = ttl
  protocol = ICMP()
  packet = ip/protocol
  resp = sr1(packet, timeout=2, verbose=0)

  if resp is None:
    print("TTL =",ttl)
    print("No reply.")
  elif resp[ICMP].type == 0:
    print("TTL =",ttl)
    print("%d hops away: " % (ip.ttl), resp[IP].src)
    print("Arrived at destination ", resp[IP].src)
    break
  else:
    print("TTL =",ttl)
    print("%d hops away: " % (ip.ttl), resp[IP].src)
  ttl += 1

  if ttl > 30:
    break

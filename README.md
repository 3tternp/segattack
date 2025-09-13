# segattack
SegAttack: Layer 2 and Layer 3 Segmentation Attack Toolkit

SegAttack is a red team toolkit for authorized Layer 2 and Layer 3 segmentation attacks, inspired by Frogger2. It tests network isolation by exploiting protocols like DNS, DHCP, CDP, STP, DTP, ARP, and MAC. Designed for penetration testers and IT auditors, it aligns with standards like Beema Samiti IT guidelines (Nepal) for secure testing in controlled environments.

Features





DNS Spoofing: Redirects DNS queries to attacker-controlled IPs.



DHCP Flooding: Exhausts DHCP pools with fake Discover packets.



CDP Flooding: Overwhelms Cisco switches with fake CDP packets.



STP Manipulation: Claims root bridge to disrupt spanning tree topology.



DTP Flooding: Negotiates trunks for VLAN hopping.



ARP Poisoning: Performs MITM via ARP cache poisoning.



MAC Flooding: Overloads switch CAM tables to force hub-like behavior.



Modular Design: Python (Scapy) and Bash (hping3, arping) implementations.



Nepal Compliance: Avoids restricted APIs (e.g., social media ban, September 2025).

Installation

Prerequisites





OS: Kali Linux or similar.



Tools: sudo apt install python3-scapy hping3 arping netfilter-persistent iptables-persistent.



Python Dependencies: pip install -r requirements.txt.



Root Privileges: Required for packet crafting and iptables.

Setup

git clone https://github.com/3tternp/segattack.git

cd segattack

pip install -r requirements.txt

requirements.txt

scapy>=2.5.0
netfilterqueue>=0.6.0

Usage

CLI (Python)

# DNS Spoofing
sudo python3 segattack.py -i eth0 --attack dns --duration 120
# DHCP Flooding
sudo python3 segattack.py -i eth0 --attack dhcp --count 5000
# CDP Flooding
sudo python3 segattack.py -i eth0 --attack cdp --count 2000
# STP Manipulation
sudo python3 segattack.py -i eth0 --attack stp --duration 60
# DTP Flooding
sudo python3 segattack.py -i eth0 --attack dtp --count 1000
# ARP Poisoning
sudo python3 segattack.py -i eth0 --attack arp -t 192.168.1.100 --duration 300
# MAC Flooding
sudo python3 segattack.py -i eth0 --attack mac --count 5000

Bash Wrappers

# DHCP Flood
sudo ./bash_wrappers/dhcp_flood.sh eth0 30 2000
# ARP Poison
sudo ./bash_wrappers/arp_poison.sh eth0 192.168.1.100 192.168.1.1 300
# MAC Flood
sudo ./bash_wrappers/mac_flood.sh eth0 30 2000

Ethical Use

Authorized Use Only: SegAttack is for controlled red team engagements with explicit permission (e.g., ROE). Unauthorized use may violate laws (e.g., Nepal’s Electronic Transactions Act). Test in lab environments (e.g., GNS3 with Cisco switches).

Detection and Mitigation





Monitor: Use Wireshark to capture packets.



Mitigate: Enable DHCP snooping, ARP inspection, port security, MAC limiting, and STP protections.



Test: Verify VLAN hopping or traffic leakage post-attack.

Contributing

See CONTRIBUTING.md for guidelines. Ideas: add VLAN hopping detection, IPv6 support, or GUI.

License

MIT License. See LICENSE.

Acknowledgments

Inspired by Frogger2 and the cybersecurity community. Thanks to Nepal’s OWASP chapter for compliance feedback.

# segattack
# SegAttack: Your Toolkit for Network Segmentation Testing 🛡️

SegAttack is a specialized toolkit for **authorized red team engagements**. It's designed to test and validate network security by simulating **Layer 2 and Layer 3 segmentation attacks**. Inspired by the Frogger2 tool, SegAttack helps you identify and fix vulnerabilities in your network's isolation controls.

This tool is ideal for **penetration testers** and **IT auditors** who need to perform secure, controlled tests. It aligns with standards like the Beema Samiti IT guidelines in Nepal, ensuring responsible and compliant use in professional environments.

-----

## ⚡ What Can SegAttack Do?

SegAttack uses a variety of powerful techniques to test network resilience.

  * **DNS Spoofing:** Redirects DNS queries to an attacker-controlled IP address, allowing for malicious redirection of web traffic.
  * **DHCP Flooding:** Overwhelms the DHCP server with fake requests, potentially denying legitimate users access to the network.
  * **CDP Flooding:** Disrupts Cisco switches by flooding them with fake Cisco Discovery Protocol packets.
  * **STP Manipulation:** Attempts to become the root bridge of the network's Spanning Tree Protocol (STP), which can disrupt network topology.
  * **DTP Flooding:** Exploits the Dynamic Trunking Protocol (DTP) to negotiate trunk links, enabling VLAN hopping and bypassing segmentation.
  * **ARP Poisoning:** Poisons the ARP cache of devices on the network to perform a "man-in-the-middle" attack.
  * **MAC Flooding:** Overloads a switch's CAM table, forcing it to act like a hub and broadcast all traffic, potentially exposing sensitive data.

The toolkit is built with a **modular design** using both Python (Scapy) and Bash scripts (hping3, arping), giving you flexibility in how you execute your tests.

-----

## 🚀 Getting Started

### Installation

#### Prerequisites

  * **Operating System:** Kali Linux or a similar penetration testing distribution is recommended.
  * **Tools:** Install the necessary packages by running this command:
    ```bash
    sudo apt install python3-scapy hping3 arping netfilter-persistent iptables-persistent
    ```
  * **Python Dependencies:** Install the required Python libraries.
    ```bash
    pip install -r requirements.txt
    ```
  * **Permissions:** SegAttack requires **root privileges** to craft and send packets.

#### Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/3tternp/segattack.git
    ```
2.  **Navigate to the directory:**
    ```bash
    cd segattack
    ```
3.  **Install the Python dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    This will install `scapy>=2.5.0` and `netfilterqueue>=0.6.0`, which are essential for packet manipulation.

-----

## 🛠️ How to Use SegAttack

### Command Line Interface (Python)

All commands should be run with `sudo`.

  * **DNS Spoofing:** Redirects traffic for a specific duration.
    ```bash
    sudo python3 segattack.py -i eth0 --attack dns --duration 120
    ```
  * **DHCP Flooding:** Sends a specified number of DHCP Discover packets.
    ```bash
    sudo python3 segattack.py -i eth0 --attack dhcp --count 5000
    ```
  * **CDP Flooding:** Floods a Cisco switch with CDP packets.
    ```bash
    sudo python3 segattack.py -i eth0 --attack cdp --count 2000
    ```
  * **STP Manipulation:** Simulates a root bridge for a set time.
    ```bash
    sudo python3 segattack.py -i eth0 --attack stp --duration 60
    ```
  * **DTP Flooding:** Attempts to negotiate trunks with DTP packets.
    ```bash
    sudo python3 segattack.py -i eth0 --attack dtp --count 1000
    ```
  * **ARP Poisoning:** Poisons the ARP cache of a target IP.
    ```bash
    sudo python3 segattack.py -i eth0 --attack arp -t 192.168.1.100 --duration 300
    ```
  * **MAC Flooding:** Overloads the switch's CAM table.
    ```bash
    sudo python3 segattack.py -i eth0 --attack mac --count 5000
    ```

-----

### Bash Wrappers

For quick and easy use, you can also use the included Bash scripts.

  * **DHCP Flood:**
    ```bash
    sudo ./bash_wrappers/dhcp_flood.sh eth0 30 2000
    ```
    (Interface, Duration, Packet Count)
  * **ARP Poison:**
    ```bash
    sudo ./bash_wrappers/arp_poison.sh eth0 192.168.1.100 192.168.1.1 300
    ```
    (Interface, Target IP, Gateway IP, Duration)
  * **MAC Flood:**
    ```bash
    sudo ./bash_wrappers/mac_flood.sh eth0 30 2000
    ```
    (Interface, Duration, Packet Count)

-----

## ⚠️ Important: Ethical Use and Liability

**SegAttack is a powerful tool for authorized, controlled testing only.**

  * **Authorized Use:** You must have **explicit, written permission** before using this toolkit on any network.
  * **Legal Compliance:** Unauthorized use of SegAttack may violate local and international laws, such as Nepal's Electronic Transactions Act.
  * **Controlled Environments:** Always test in a secure lab environment, like a virtual network set up with GNS3 and Cisco switches, to prevent accidental damage or legal issues.

-----

## 🔬 Detection and Mitigation

After running your tests, it's crucial to understand how to detect and mitigate these attacks.

  * **Monitor:** Use packet analyzers like **Wireshark** to capture and inspect network traffic for malicious packets.
  * **Mitigate:** Harden your network with these security measures:
      * **DHCP Snooping**
      * **ARP Inspection**
      * **Port Security**
      * **MAC Limiting**
      * **STP Protections**
  * **Test:** Post-attack, verify if the attacks were successful by checking for VLAN hopping, traffic leakage, or other segmentation breaches.

-----

## 🙏 Contributing and License

We welcome contributions from the community\! Check out our **CONTRIBUTING.md** file for guidelines. Ideas for future features include IPv6 support, a graphical user interface (GUI), and automated VLAN hopping detection.

This project is released under the **MIT License**.

A big thank you to the **cybersecurity community** and the **OWASP Nepal chapter** for their inspiration and guidance in making this tool compliant and effective.

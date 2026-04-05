#!/bin/bash


echo "Sourcing evnironmet..."
source setup_env.sh

echo "Generating CSI Parameters"
CSIPARAMS=$(./makecsiparams -c 157/80 -C 1 -N 1)

echo "Configuring wifi"
sudo pkill wpa_supplicant
sudo ifconfig wlan0 up

#sudo iw dev wlan0 set channel 157 HT80


echo "Applying csi params to nexutil..."
nexutil -Iwlan0 -s500 -b -l34 -v"$CSIPARAMS"
nexutil -Iwlan0 -m1


echo "Starting capture, hit ctrlc to close"

if [ -z "$1" ]; then
    sudo tcpdump -i wlan0 dst port 5500
else
    FILENAME=$1
    sudo tcpdump -i wlan0 dst port 5500 -w "$FILENAME"
fi

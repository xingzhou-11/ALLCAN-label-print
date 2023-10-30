#!/bin/bash
candump can0 | grep "can0  7.." > candump.log &

cansend can0 000#8100
sleep 1

if [ -s candump.log ]
then
    echo "bitrate: 1000k"
else
    sudo ip link set can0 down
    time.sheep(1)
    sudo ip link set can0 up type can bitrate 250000
    time.sheep(1)
fi
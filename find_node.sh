#!/bin/bash

candump can0 | grep --line-buffered "can0  7" > /home/orangepi/ALLCAN-lable-print/candump.log &

cansend can0 000#8100

pid=$!
echo $pid

sleep 2s

# 关闭后台运行的 candump
sudo kill -9 $pid

if [ -s /home/orangepi/ALLCAN-lable-print/candump.log ]
then
    echo "bitrate: 1000k"
else
    sudo ip link set can0 down
    sleep 1s
    sudo ip link set can0 up type can bitrate 250000
    sleep 1s
fi

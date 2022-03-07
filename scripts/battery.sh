#! /bin/bash

battery=$(cat /sys/class/power_supply/BAT0/capacity)
if [[ ${battery} -le 98 ]];
	then notify-send -u critical -i ~/Downloads/low-battery.ico "Battery Low! $battery%" && xbacklight -set 25
fi

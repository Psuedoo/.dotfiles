#!/bin/sh

wallpaper=$(cat ~/.cache/wal/colors.json | jq '.wallpaper' | sed 's/"//g')
feh --bg-scale $wallpaper &

alacritty &
# wal -b 282738 -i ~/.config/Wallpaper/120_-_KnFPX73.jpg &&
picom --config ~/.config/picom/picom.conf &


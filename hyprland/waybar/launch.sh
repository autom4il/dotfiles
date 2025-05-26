#!/usr/bin/bash

killall waybar

if [[ $USER = "autom4il" ]]
then
    waybar -c ~/.config/waybar/config & -s ~/.config/waybar/style.css
else
    waybar &
fi

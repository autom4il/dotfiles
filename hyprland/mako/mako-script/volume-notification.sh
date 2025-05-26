#!/usr/bin/env bash

# Get the current volume
volume=$(amixer get Master | awk -F'[][]' 'END{ print $2 }')

mute=$(amixer set Master toggle | awk -F "[][]" 'END{print $6}')

if [[ "{$mute}" == "off" ]]
then
  message="Vol: muted"
else
  message="Vol: ${volume}"
fi

# Send the nofication using notify-send
notify-send -u low -h string:x-canonical-private-synchronous:volume "$message"

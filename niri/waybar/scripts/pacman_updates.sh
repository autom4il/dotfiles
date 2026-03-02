# Author: autom4il
# Date: 10 Feb 24
# Desc: Check pacman updates

if /usr/bin/ip link show enp1s0 |grep -q "state UP"
then
    check_updates=$(checkupdates |wc -l)
else
    check_updates="?"
fi

echo "$check_updates"

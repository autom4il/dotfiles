# Author: autom4il
# Date: 2023-12-30
# Desc: Preventing nested ranger instances

#!/usr/bin/env bash

ranger() {
    if [ -z "$RANGER_LEVEL" ]; then
        /usr/bin/ranger "$@"
    else
        exit
    fi
}

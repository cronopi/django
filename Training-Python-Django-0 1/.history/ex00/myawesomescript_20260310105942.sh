#!/bin/sh
curl -sL -I "$1" | grep -i '^location:' | tail -1 | cut -d' ' -f2

#!/bin/sh
curl -sL -w "%{url_effective}\n" -o /dev/null "$1"

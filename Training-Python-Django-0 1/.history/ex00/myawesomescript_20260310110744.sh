#!/bin/sh
curl L -w "%{url_effective}\n" -o /dev/null "$1"

#!/bin/bash

if [ $EUID -eq 0 ]; then
    echo "$(tput setaf 2)Script is running with root privileges.$(tput sgr0)"
    python shellcat.py
else
    echo "$(tput setaf 1)This script must be run with root privileges. Please restart it with sudo.
    sudo ./shellcat_start$(tput sgr0)"
fi

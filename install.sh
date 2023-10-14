#!/bin/bash

if [ $EUID -eq 0 ]; then
    echo "$(tput setaf 2)Script is running with root privileges.$(tput sgr0)"

    # Your code for root
    apt-get install mingw-w64
    pip install -r requirements.txt

    echo "$(tput setaf 2)[+] Success! Run ./shellstart to use shellcat!$(tput sgr0)"
else
    echo "$(tput setaf 1)This script must be run with root privileges. Please restart it with sudo.$(tput sgr0)"
fi

#!/bin/bash

#Please do the command "chmod +x Launch.sh" before launch the script

if test $(whoami) = 'root' ; then
    python3 AutomaticCRR.py
else
    echo Please run the script as a super user
    exit
fi



#!/bin/bash

if test $(whoami) = 'root' ; then
    python3 AutomaticCRR.py
else
    echo Please run the script as a super user
    exit
fi



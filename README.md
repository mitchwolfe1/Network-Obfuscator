# Network-Obfuscator
Emulates a service to listen on all ports. Defense concept against port scans.

Specify a range of ports for the script to listen on.

Usage: ```python portlistener.py [STARTPORT] [ENDPORT]```

Will listen until process is killed

## Bugs

Ghost Sockets still active after script is terminated

FIX: ```python portlistener.py stop```

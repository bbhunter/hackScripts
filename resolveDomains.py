#! /usr/bin/env python
import sys
import socket

for line in sys.stdin:
    line = line.strip()
    try:
        print line+":"+socket.gethostbyname(line)
    except:
        print line +" didn't resolve."

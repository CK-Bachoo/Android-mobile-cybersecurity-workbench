#!/bin/bash
pkill -f "watchdog.py" 2>/dev/null
nohup python3 watchdog.py > /dev/null 2>&1 &
echo $! > watchdog.pid

#!/bin/bash
pkill -f "watchdog.py" 2>/dev/null
rm -f watchdog.pid 2>/dev/null

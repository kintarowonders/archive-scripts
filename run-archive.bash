#!/bin/bash

cd /root/archive-scripts
python3 do-backup.py
python3 do-archive.py
python3 do-cleaner.py

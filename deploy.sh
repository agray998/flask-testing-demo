#!/bin/bash
sudo apt update
sudo apt install python3 python3-pip python3-venv -y
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
echo "killing existing processes"
sudo kill -9 $(sudo lsof -i :5000 | cut -d' ' -f2 | tail -n 5 | head -n 1)
python3 create.py
python3 -m gunicorn -D --workers 4 --bind 0.0.0.0:5000 app:app
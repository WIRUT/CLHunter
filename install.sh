#!/bin/bash -x

clear

echo "virtualenv venv"
wait
echo "pip install git+https://github.com/juliomalegria/python-craigslist"
wait
echo "pip install slackclient sqlalchemy python-dateutil"
wait
echo "Installation complete. To run CLHunter type: 'python lib/main.py'"
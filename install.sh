#!/bin/bash 

clear

echo "Creating virtual environment"
virtualenv venv
wait
source virtualenv_activate.sh
wait
# echo "Installing needed python packages"
# pip install git+https://github.com/juliomalegria/python-craigslist
# wait
# pip install slackclient sqlalchemy python-dateutil
# wait
# echo "\nInstallation complete. To run CLHunter type: 'python lib/main.py'"

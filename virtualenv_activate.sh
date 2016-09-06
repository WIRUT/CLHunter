#!/bin/sh
source venv/bin/activate
wait
echo "Installing needed python packages"
pip install git+https://github.com/juliomalegria/python-craigslist
wait
pip install slackclient sqlalchemy python-dateutil
wait
echo "Installation complete. To run, activate your virtual environment by " \
	 "running command: \n\n\t 'source venv/bin/activate' \n\n and then: \n\n\t"\
	"'python lib/main.py'"

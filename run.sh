#! /bin/sh

echo 'Starting the application'
cd /Users/colby/Code/leadparser

# check if venv exists
if [ ! -d "venv" ]; then
    echo 'Creating virtual environment'
    python3 -m venv venv
    source venv/bin/activate
    echo 'Installing python dependencies.'
    pip install -r requirements.txt

else
    echo 'Activating virtual environment.'
    source venv/bin/activate
fi

# check if node_modules exists
if [ ! -d "node_modules" ]; then
    echo 'Installing node dependencies.'
    npm install
fi

# set environment variables
export FLASK_APP=app.py
export FLASK_DEBUG=1

# run the application and open the browser
echo 'Application eady!'
open http://localhost:5000
flask run

read -p "Press any key to continue... " -n1 -s
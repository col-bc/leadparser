Write-Output "Starting the application"

# check if python3.10 is installed
$python = Get-Command python3.10 -ErrorAction SilentlyContinue
if ($python -eq $null) {
    Write-Output "Python 3.10 is required. Install it at https://www.python.org/downloads/"
    exit 1
}

# check if venv exists
If(-not(Test-Path -Path "venv")) {
    Write-Output "Virtual environment does not exist"
    Write-Output "Creating virtual environment"
    python -m venv venv
    Write-Output "Done."
    Write-Output "Installing python dependencies..."
    .\venv\Scripts\activate
    pip install -r requirements.txt
    Write-Output "Done."
}

# activate venv
. .\venv\Scripts\activate

# check if node_modules exists
If(-not(Test-Path -Path "node_modules")) {
    Write-Output "Installing node modules..."
    npm install
    Write-Output "Done."
}

# set environment variables
$env:FLASK_APP = "app.py"
$env:FLASK_DEBUG = "0"

# Open browser to http://localhost:5000/
Start-Process "http://localhost:5000/"

# run the application
echo 'Application ready!'
flask run

# wait for user input
Write-Output "Press any key to exit"
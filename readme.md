# Lead Parser for Red Dirt Equipment

This app extracts data from csv files containing lead data. It then formats the data and allows for the related objects to be created automatically in Pipedrive. The following csv templates are supported;
- [mahindrausa.com](https://mahindrausa.com/)
- [reddirtequipment.com](https://reddirtequipment.com/) (Dealer Spike)
- [kioti.com](https://kioti.com/)

## Prerequisites
This app uses python and requires version 3.10 or greater. View instructions on installing python [here](https://www.python.org/downloads/).

## Running the application
Open a terminal window to the root directory of this project.
```bash
$ cd ~/Code/leadparser
$ tree -L 1 ${pwd}
.
├── __init__.py
├── __pycache__
├── app.py
├── node_modules/
├── package-lock.json
├── package.json
├── readme.md
├── requirements.txt
├── run.sh
├── settings.json
├── static/
├── tailwind.config.js
├── templates/
├── utils/
└── venv/
```
Now simply execute the `run.sh` executable. The script will create a virtual environment (if one does not exist), install all the python dependencies in `requirements.txt` and then install the javascript dependencies required by `package-lock.json`. When the server is ready the script will open the app in your default web browser. By default, the app will be hosted at [`http://localhost:5000/`](http://localhost:5000/).
```sh
$ ./run.sh
Starting the application
Creating virtual environment
Installing dependencies
...
Application eady!
 * Serving Flask app 'app.py'
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```
Thanks it!

## Relevant Links
- [flowbite](https://flowbite.com) - UI Library
- [flask](https://flask.palletsprojects.com/en/2.2.x/) - Backend framework
- [Pipedrive](https://pipedrive.com)
- [Pipedrive Developers](https://developers.pipedrive.com/)
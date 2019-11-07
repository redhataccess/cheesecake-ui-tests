# cheescake-ui-tests
UI tests for Pantheon v2 using Selenium + Python.

## Pre-requisites
python3

## Setup
Install and create virtualenv (This step should be executed only when setting up the project for the first time)

* Install virtualenv
python3 -m pip install --user virtualenv

* Create virtualenv
python3 -m venv env

* Activate the virtual environment:
$ source env/bin/activate

* Install dependencies for setting up tests:
$ pip install -r requirements.txt

* Set Python Path to the current directory:
export PYTHONPATH = "<path to your current directory>"

* To Check if PYTHONPATH is set correctly to the current directory:
echo $PYTHONPATH
PYTHONPATH should not be blank and should be your current directory.

## Execute tests:
* Set the username and password fields in config.ini file
* User can choose to run the tests for different environments listed in config.ini file by passing the 'evt' and 'base_url'
parameter in the 'base.config_reader(<evt>, <base_url>)' method present inside webdriver.py file

* Go inside the suites directory and run the below command:
lcc run <test_file_name>
e.g. lcc run login_test

Deactivate virtualenv:
$ deactivate

Make the changes in the config file for actual values.
mv config.ini.sample config.ini
Make the appropriate changes to base URL in config.ini file.
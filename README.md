# cheescake-ui-tests
UI tests for Pantheon v2 using Selenium + Python.

## Pre-requisites
python3

## Setup
Install and create virtualenv (This step should be executed only when setting up the project for the first time)

* Install virtualenv

``` python3 -m pip install --user virtualenv ```

* Create virtualenv

``` python3 -m venv env ```

* Activate the virtual environment:

``` $ source env/bin/activate ```

* Install dependencies for setting up tests:

``` $ pip install -r requirements.txt ```

* Set Python Path to the current directory:

``` export PYTHONPATH = "<path to your current directory>" ```

* To Check if PYTHONPATH is set correctly to the current directory:

``` echo $PYTHONPATH ```

PYTHONPATH should not be blank and should be your current directory.

## Execute tests:
* Make the changes in the config file for actual values.

``` cp config.ini.sample config.ini ```

Make the appropriate changes to base URL,username and password fields in config.ini file.
You can reach out to any of the contributors for the actual values to be used.
By default, the tests will run in headless mode. If you choose to run otherwise, change the value to "no".


* To execute the tests:
``` lcc run ```

* To view the reports on console after you ran the tests:
``` lcc report ```

* To view the report in browser:
``` firefox report/report.html ```

* User can choose to run the tests for different environments listed in config.ini file by passing the 'env' and 'base_url'
parameter in 'base.config_reader(<env>, <base_url>)' method present inside browser_util.py file

* To run a single test:
``` lcc run <test_file_name> ```
e.g. lcc run login_test

Deactivate virtualenv:
``` $ deactivate ```


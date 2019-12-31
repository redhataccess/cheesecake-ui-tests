import lemoncheesecake.api as lcc
import git
import os
import shutil
import logging
import requests
import subprocess
import helpers.base as base
from helpers import constants
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from lemoncheesecake.matching import *
from pages import login_page


logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

test_repo_URL = base.config_reader('test_repo', 'test_repo_url')
test_repo_name = base.config_reader('test_repo', 'repo_name')
git_import_repo = base.config_reader(
    'git_import_test_repo',
    'git_import_repo_name')
url = base.config_reader('qa', 'base_url')
username = base.config_reader('login', 'username')
auth = base.config_reader('login', 'password')
headless = base.config_reader('test_mode', 'headless')


@lcc.fixture(scope="pre_run")
def setup_test_repo():
    logging.info("Cloning a test repo from gitlab..")
    project_dir_git = os.path.join(os.getcwd(), 'test-repo')

    if os.path.isdir(project_dir_git):
        shutil.rmtree(project_dir_git)

    os.mkdir(project_dir_git)

    repo = git.Repo.init(project_dir_git)
    origin = repo.create_remote('origin', test_repo_URL)
    origin.fetch()
    origin.pull(origin.refs[0].remote_head)

    logging.info("Installing the Pantheon uploader script..")
    try:
        subprocess.check_call(
            "curl -o pantheon.py https://raw.githubusercontent.com/redhataccess/pantheon/master/uploader/pantheon.py",
            shell=True)
    except subprocess.CalledProcessError as e:
        logging.error("Unable to install the uploader script")
        raise e

    os.chdir(project_dir_git)

    try:
        subprocess.check_call('python3 ../pantheon.py push', shell=True)
    except subprocess.CalledProcessError as e:
        logging.info(
            "Test setup did not complete successfully, error encountered during 'pantheon push'")
        raise e


@lcc.fixture(names=("driver", "driver_obj"), scope="session")
def setup(setup_test_repo):
    lcc.log_info("Initialising the webdriver object, opening the browser...")
    # Initialise the global webdriver, open the browser and maximise the
    # browser window
    if headless == "yes":
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        driver = webdriver.Chrome(
            ChromeDriverManager().install(),
            chrome_options=options)
        logging.info(
            "Chrome driver has been initialised successfully in headless mode")
    else:
        driver = webdriver.Chrome(ChromeDriverManager().install())
        logging.info("Chrome driver has been initialised successfully")

    driver.maximize_window()
    driver.implicitly_wait(15)
    driver.get(url)
    # login to Pantheon v2
    lcc.log_info("Log in to Pantheon v2 using credentials")
    login_page.login(driver)
    # the global driver object can be used globally in the tests.
    yield driver
    # This block of code is the teardown method which deletes the repository
    # created and closes the browser window.
    lcc.log_info("Deleting the test-repo from QA env...")
    path_to_repo = url + "content/repositories/" + test_repo_name
    lcc.log_info("Test repo node being deleted at: %s" % path_to_repo)
    body = {":operation": "delete"}
    response = requests.post(path_to_repo, data=body, auth=(username, auth))
    check_that("The test repo was deleted successfully",
               response.status_code, equal_to(200))
    path_to_git_repo = url + "content/repositories/" + git_import_repo
    lcc.log_info("Test repo node being deleted at: %s" % path_to_git_repo)
    response_git_delete = requests.post(
        path_to_git_repo, data=body, auth=(
            username, auth))
    check_that(
        "The git import test repo was deleted successfully from backend",
        response_git_delete.status_code,
        equal_to(200))
    lcc.log_info("Closing the browser window...")
    driver.close()
    driver.quit()


@lcc.fixture(scope="session")
def publish_module_api(driver):
    # preview_path = driver.current_url[59:]
    # preview_path[:-8]
    url_endpoint = url + constants.path_to_module_to_be_published
    print (url_endpoint)
    body = {":operation": "pant:release"}
    response = requests.post(url_endpoint, json=body, auth=('admin', 'admin'))
    print (response.text)

import lemoncheesecake.api as lcc
import git, os, shutil
import logging
import subprocess
import helpers.base as base
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

test_repo_URL = base.config_reader('test_repo', 'test_repo_url')
url = base.config_reader('qa', 'base_url')


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
        subprocess.check_call("curl -S https://raw.githubusercontent.com/redhataccess/pantheon/master/uploader/setup.sh | sh -",
                              shell=True)
    except subprocess.CalledProcessError as e:
        logging.error("Unable to install the uploader script")
        raise e

    os.chdir(project_dir_git)

    try:
        subprocess.check_call('pantheon push', shell=True)
    except subprocess.CalledProcessError as e:
        logging.info("Test setup did not complete successfully, error encountered during 'pantheon push'")
        raise e


@lcc.fixture(names=("driver", "driver_obj"), scope="session")
def setup(setup_test_repo):
    lcc.log_info("Initialising the webdriver object, opening the browser...")
    # Initialise the global webdriver, open the browser and maximise the browser window
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(15)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(url)
    yield driver
    lcc.log_info("Closing the browser window...")
    driver.close()
    driver.quit()

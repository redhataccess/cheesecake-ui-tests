import lemoncheesecake.api as lcc
import git
import os
import shutil, time, datetime
import logging
import requests
import subprocess
import helpers.base as base
from selenium import webdriver
from helpers import utilities
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# from webdriver_manager.firefox import GeckoDriverManager
# from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


from lemoncheesecake.matching import *
from pages import login_page
from helpers import constants


logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

test_repo_URL = base.config_reader('test_repo', 'test_repo_url')
test_repo_name = base.config_reader('test_repo', 'repo_name')
git_import_repo = base.config_reader('git_import_test_repo', 'git_import_repo_name')

# setting the appropriate URL value from env variable
env = os.environ['PANTHEON_ENV']
if env == "qa":
    url = base.config_reader('qa', 'base_url')
elif env == "dev":
    url = base.config_reader('dev', 'base_url')
elif env == "stage":
    url = base.config_reader('stage', 'base_url')
elif env == "prod":
    url = base.config_reader('prod', 'base_url')
else:
    raise Exception("Please set the env variable PANTHEON_ENV as dev/qa/stage specifically. "
                    "To run your tests against QA, run `$export PANTHEON_ENV=qa` before you run the tests")

logging.info("Tests are running against Pantheon instance: %s", url)
username = base.config_reader('login', 'username')
auth = base.config_reader('login', 'password')
headless = base.config_reader('test_mode', 'headless')
uploader_username = base.config_reader('uploader', 'username')
uploader_password = base.config_reader('uploader', 'password')
admin_username = base.config_reader('admin_login', 'username')
admin_auth = base.config_reader('admin_login', 'password')
proxy_url = base.config_reader('proxy', 'proxy_server')


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
    #origin.pull(origin.refs[0].remote_head)
    origin.pull('assemblies-2')

    logging.info("Installing the Pantheon uploader script..")
    # try:
    #     subprocess.check_call(
    #         "curl -o pantheon.py https://raw.githubusercontent.com/redhataccess/pantheon/master/uploader/pantheon.py",
    #         shell=True)
    # except subprocess.CalledProcessError as e:
    #     logging.error("Unable to install the uploader script")
    #     raise e

    os.chdir(project_dir_git)

    try:
        # subprocess.check_call(
        #     ('python3 ../pantheon.py --user={} --password={} --server={} push'.format(uploader_username,
        #                                                                               uploader_password,
        #                                                                               url)), shell=True)
        subprocess.check_call(
            ('pantheon --user={} --password={} --server={} push'.format(uploader_username, uploader_password,
                                                                        url)), shell=True)
        os.mkdir('screenshots')
        os.chdir('screenshots')
    except subprocess.CalledProcessError as e:
        logging.info(
            "Test setup did not complete successfully, error encountered during 'pantheon push'")
        raise e


# Creates products and add version to it using api endpoint
@lcc.fixture(scope="session")
def setup_test_products():
    print("Created product::", constants.product_name_uri)
    path_to_product_node = url + "content/products/" + constants.product_name_uri
    path_to_version = path_to_product_node + "/versions/{}".format(constants.product_version)
    lcc.log_info("Creating test product")
    lcc.log_info(
        "Test Product node being created at: %s" % path_to_product_node)

    create_product_payload = {"name": constants.product_name,
              "description": "AT test product description",
              "sling:resourceType": "pantheon/product",
              "jcr:primaryType": "pant:product",
              "locale": "en-US",
              "urlFragment": constants.product_name_uri}

    # Hit the api for create product
    response = requests.post(path_to_product_node, data=create_product_payload, auth=(username, auth))
    check_that("The Product was created successfully",
               response.status_code, any_of(equal_to(201), equal_to(200)))
    lcc.log_info("Creating version for the above product")
    time.sleep(5)

    lcc.log_info("Product version being created for the above product: %s" % path_to_version)

    create_version_payload = {"name": constants.product_version,
                              "sling:resourceType": "pantheon/productVersion",
                              "jcr:primaryType": "pant:productVersion",
                              "urlFragment": constants.product_version}


    # Hit the api for create version for the above product
    response = requests.post(path_to_version, data=create_version_payload, auth=(username, auth))
    check_that("The Product version was created successfully",
               response.status_code, any_of(equal_to(201), equal_to(200)))


def get_product_id():
    # Get ID of the product created
    path_to_product_node = url + "content/products/" + constants.product_name_uri
    path_to_version = path_to_product_node + "/versions/{}".format(constants.product_version)
    path = path_to_version+".json"
    response = requests.get(url=path, auth=(username, auth))
    product_uuid = response.json()["jcr:uuid"]
    return product_uuid


@lcc.fixture(names=("driver", "driver_obj"), scope="session")
def setup(setup_test_repo, setup_test_products):
    lcc.log_info("Initialising the webdriver object, opening the browser...")
    # Initialise the global webdriver, open the browser and maximise the
    # browser window
    if headless == "yes":
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--window-size=1920,1080')
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--proxy-server=%s' % proxy_url)
        # options.add_argument('--proxy-auto-detect')
        # driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
        driver = webdriver.Chrome(ChromeDriverManager(path=os.environ['PYTHONPATH']).install(), chrome_options=options)
        driver.maximize_window()
        logging.info("Webdriver has been initialised successfully in headless mode...")
    else:
        options = Options()
        options.add_argument('--proxy-server=%s' % proxy_url)
        #options.add_argument('--proxy-auto-detect')
        # caps = DesiredCapabilities.FIREFOX.copy()
        # caps["marionette"] = False
        # driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options, capabilities=caps)

        driver = webdriver.Chrome(ChromeDriverManager(path=os.environ['PYTHONPATH']).install(),chrome_options=options)
        logging.info("Webdriver has been initialised successfully")

    driver.maximize_window()
    driver.implicitly_wait(15)
    driver.get(url)
    lcc.log_info(driver.current_url)
    # login to Pantheon v2
    lcc.log_info("Log in to Pantheon v2 using credentials")
    login_page.login(driver)
    # the global driver object can be used globally in the tests.
    yield driver

    # This block of code is the teardown method which deletes the repository
    # created and closes the browser window.

    # # This block of code is the teardown method which deletes the repository uploaded for testing
    # lcc.log_info("Deleting the test-repo from QA env...")
    # path_to_repo = url + "bin/cpm/nodes/node.json/content/repositories/" + test_repo_name
    # lcc.log_info("Test repo node being deleted at: %s" % path_to_repo)
    # time.sleep(15)
    # response = requests.delete(path_to_repo, auth=(admin_username, admin_auth))
    # check_that("The test repo was deleted successfully",
    #            response.status_code, equal_to(200))
    # time.sleep(15)

    # Deleting the git repo uploaded via git import in the test suite.
    path_to_git_repo = url + "bin/cpm/nodes/node.json/content/repositories/" + git_import_repo
    lcc.log_info("Test repo node used for git import functionality being deleted at: %s" % path_to_git_repo)
    response_git_delete = requests.delete(path_to_git_repo, auth=(admin_username, admin_auth))
    print(str(response_git_delete.content))
    check_that(
        "The git import test repo was deleted successfully from backend", response_git_delete.status_code,
        equal_to(200))

    # This block of code is the teardown method which deletes the product created for testing
    path_to_new_product_node = url + "bin/cpm/nodes/node.json/content/products/" + constants.product_name_uri
    lcc.log_info("Test Product node being deleted at: %s" % path_to_new_product_node)
    response1 = requests.delete(path_to_new_product_node, auth=(admin_username, admin_auth))
    print(str(response1.content))
    check_that("Test product version created was deleted successfully",
               response1.status_code, equal_to(200))
    time.sleep(15)

    lcc.log_info("Closing the browser window...")
    driver.close()
    driver.quit()

    # lcc.log_info("Deleting the test-repo from QA env...")
    # path_to_repo = url + "content/repositories/" + test_repo_name
    # lcc.log_info("Test repo node being deleted at: %s" % path_to_repo)
    #
    # body = {":operation": "delete"}
    # response = requests.post(path_to_repo, data=body, auth=(admin_username, admin_auth))
    # check_that("The test repo was deleted successfully",
    #            response.status_code, equal_to(200))
    # time.sleep(10)
    #
    # path_to_git_repo = url + "content/repositories/" + git_import_repo
    # lcc.log_info("Test repo node used for git import functionality being deleted at: %s" % path_to_git_repo)
    # response_git_delete = requests.post(path_to_git_repo, data=body, auth=(admin_username, admin_auth))
    # check_that(
    #     "The git import test repo was deleted successfully from backend", response_git_delete.status_code, equal_to(200))
    # time.sleep(10)
    # # Deletes the products created using api endpoint
    #
    # lcc.log_info("Deleting test product created.. ")
    # body = {":operation": "delete"}
    # path_to_new_product_node = url + "content/products/" + constants.product_name_uri
    # lcc.log_info("Test Product node being deleted at: %s" % path_to_new_product_node)
    #
    # response1 = requests.post(path_to_new_product_node, data=body, auth=(admin_username, admin_auth))
    # check_that("Test product version created was deleted successfully",
    #            response1.status_code, equal_to(200))

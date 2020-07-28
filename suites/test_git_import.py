import sys
from helpers import base
import lemoncheesecake.api as lcc
from lemoncheesecake.matching import *
from pages import git_import_page
from helpers import utilities
from helpers import constants
from helpers import locators
import requests
from fixtures import fixture
from helpers.base_screenshot import Screenshot
from selenium.webdriver.common.by import By
from polling2 import poll

sys.path.append("..")

# SUITE = {
#     "description": "Git import for authenticated user",
#     "rank": "6"
# }
git_import_repo_URL = base.config_reader('git_import_test_repo', 'git_import_repo_url')
git_import_repo_Name = base.config_reader('git_import_test_repo', 'git_import_repo_name')
git_import_repo_branch = base.config_reader('git_import_test_repo', 'git_import_repo_branch')
number_of_modules = base.config_reader('git_import_test_repo', 'number_of_modules_imported')
module_title_prefix = constants.module_title_prefix


@lcc.suite("Suite: Git import functionality", rank="6")
class test_git_import(Screenshot):
    driver = lcc.inject_fixture("driver_obj")
    
    @lcc.test("Verify that warning message should be displayed when repository URL is empty")
    def git_import_for_empty_git_repo(self):
        utilities.click_element(
            self.driver, By.LINK_TEXT, locators.MENU_GIT_IMPORT_LINK_TEXT)
        git_import_page.import_git_repo(self.driver, None, None)
        check_that("Empty git repo url warning message",
                   utilities.get_text(self.driver, By.CSS_SELECTOR, locators.WARNING_ALERT_CSS),
                   contains_string(constants.repo_url_empty_warning_message))
    
    @lcc.test("Verify that error message should be displayed when repository url has invalid")
    def git_import_for_invalid_git_repo_url(self):
        git_import_page.import_git_repo(
            self.driver, constants.invalid_git_repo_url, git_import_repo_branch)
        check_that("Invalid git repo url error message",
                   utilities.get_text(self.driver, By.CSS_SELECTOR, locators.REPO_URL_INVALID_ERROR_CSS),
                   contains_string(constants.repo_url_invalid_error_message))
    
    @lcc.test("Verify that user should be able to upload modules successfully using git import")
    def git_import_for_sample_repo(self):
        git_import_page.import_git_repo(
            self.driver, git_import_repo_URL, git_import_repo_branch)
        utilities.verify_and_accept_confirmation_modal(
            self.driver, locators.GIT_IMPORT_REQUEST_SUBMITTED_TITLE,
            constants.git_import_submitted_modal_title, locators.GIT_IMPORT_REQUEST_SUBMITTED_YES)
        utilities.wait(30)
        utilities.page_reload(self.driver)
        search_url = fixture.url + 'pantheon/internal/modules.json?search=' + module_title_prefix
        lcc.log_info("Git import functionality verified using endpoint: %s" % search_url)
        lcc.log_info("Trying to poll the endpoint until we get the required number of search results as"
                     " per the test data ...")
        poll(lambda: requests.get(search_url).json()["size"] == 9, step=5, timeout=120)

        imported_modules_request = requests.get(search_url)
        imported_modules = imported_modules_request.json()
        lcc.log_info(str(imported_modules))
        total_modules = imported_modules["size"]

        lcc.log_info("Number of modules listed with the similar title name: %s" % str(total_modules))
        lcc.log_info("Capturing the number of modules uploaded from the repo: %s ..." % git_import_repo_Name)
        results = imported_modules["results"]
        imported_modules_array = []
        for result in results:
            if result["pant:transientSourceName"] == git_import_repo_Name:
                imported_modules_array.append(result["jcr:title"])
        lcc.log_info("Modules imported successfully via git import: %s with title prefix" % str(imported_modules_array))
        lcc.log_info("Number of modules imported successfully from repo: %s is %s" % (git_import_repo_URL,
                                                                                      str(len(imported_modules_array))))
        check_that("Count of modules uploaded using git import", len(imported_modules_array), equal_to(int(number_of_modules)))

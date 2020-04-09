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
sys.path.append("..")

SUITE = {
    "description": "Git import for authenticated user",
    "rank": "6"
}
git_import_repo_URL = base.config_reader('git_import_test_repo', 'git_import_repo_url')
git_import_repo_Name = base.config_reader('git_import_test_repo', 'git_import_repo_name')
git_import_repo_branch = base.config_reader('git_import_test_repo', 'git_import_repo_branch')
number_of_modules = base.config_reader('git_import_test_repo', 'number_of_modules_imported')
module_title_prefix = constants.module_title_prefix


@lcc.test("Verify that warning message should be displayed when repository URL is empty")
def git_import_for_empty_git_repo(driver):
    utilities.click_element_by_link_text(
        driver, locators.MENU_GIT_IMPORT_LINK_TEXT)
    git_import_page.import_git_repo(driver, None, None)
    check_that("Empty git repo url warning message", utilities.get_text_by_css(
        driver, locators.WARNING_ALERT_CSS), contains_string(constants.repo_url_empty_warning_message))


@lcc.test("Verify that error message should be displayed when repository url has invalid")
def git_import_for_invalid_git_repo_url(driver):
    git_import_page.import_git_repo(
        driver, constants.invalid_git_repo_url, git_import_repo_branch)
    check_that("Invalid git repo url error message", utilities.get_text_by_css(
        driver, locators.REPO_URL_INVALID_ERROR_CSS), contains_string(constants.repo_url_invalid_error_message))


@lcc.test("Verify that user should be able to upload module using git import")
def git_import(driver):
    git_import_page.import_git_repo(
        driver, git_import_repo_URL, git_import_repo_branch)
    utilities.verify_and_accept_confirmation_modal(
        driver, locators.GIT_IMPORT_REQUEST_SUBMITTED_TITLE,
        constants.git_import_submitted_modal_title, locators.GIT_IMPORT_REQUEST_SUBMITTED_YES)
    utilities.wait(30)
    utilities.page_reload(driver)
    search_url = fixture.url + 'modules.json?search=' + module_title_prefix
    lcc.log_info("Git import functionality verified using endpoint: %s" % search_url)
    imported_modules_request = requests.get(search_url)
    imported_modules = imported_modules_request.json()
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

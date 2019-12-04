import sys
from helpers import base
import lemoncheesecake.api as lcc
from lemoncheesecake.matching import *
from pages import git_import_page
from pages import search_page
from helpers import utilities
from helpers import constants
from helpers import locators
sys.path.append("..")

SUITE = {
    "description": "Git import for authenticated user",
    "rank": "2"
}
git_import_repo_URL = base.config_reader('git_import_test_repo', 'git_import_repo_url')
git_import_repo_Name = base.config_reader('git_import_test_repo', 'git_import_repo_name')

@lcc.test("Warning message should be displayed when repository URL is empty")
def git_import_for_empty_git_repo(driver):
    utilities.click_element_by_link_text(driver, locators.MENU_GIT_IMPORT_LINK_TEXT)
    git_import_page.import_git_repo(driver, None, None)
    check_that("Empty git repo url warning message",
               utilities.get_text_by_css(driver, locators.WARNING_ALERT_CSS),
               contains_string(constants.repo_url_empty_warning_message))

@lcc.test("Error message should be displayed when repository url has invalid")
def git_import_for_invalid_git_repo_url(driver):
    git_import_page.import_git_repo(driver, constants.invalid_git_repo_url, constants.git_import_branch)
    check_that("Invalid git repo url error message",
               utilities.get_text_by_css(driver, locators.REPO_URL_INVALID_ERROR_CSS),
               contains_string(constants.repo_url_invalid_error_message))


@lcc.test("User should be able to upload module using git import")
def git_import(driver):
    git_import_page.import_git_repo(driver, git_import_repo_URL, constants.git_import_branch)
    utilities.verify_and_accept_confirmation_modal(driver, locators.GIT_IMPORT_REQUEST_SUBMITTED_TITLE,
                                                   constants.git_import_submitted_modal_title,
                                                   locators.GIT_IMPORT_REQUEST_SUBMITTED_YES)
    utilities.wait(15)
    utilities.page_reload(driver)
    search_page.wait_for_module_to_load(driver, constants.git_import_last_module_uploaded)
    check_that("All modules are imported",
               search_page.count_of_modules_with_the_source_name(driver, git_import_repo_Name),
               equal_to(constants.git_import_repo_modules_count))



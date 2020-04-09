from helpers import locators
import sys
from helpers import utilities
sys.path.append("..")

# Enter git repo url and branch name and click on submit


def import_git_repo(driver, repo, branch):
    if (repo is not None):
        utilities.enter_text_by_css_selector(
            driver, locators.GIT_REPO_URL_TEXTBOX_CSS, repo)
        utilities.enter_text_by_css_selector(
            driver, locators.GIT_REPO_BRANCH_TEXTBOX_CSS, branch)
    utilities.click_element_by_css_selector(
        driver, locators.GIT_REPO_SUBMIT_BUTTON_CSS)

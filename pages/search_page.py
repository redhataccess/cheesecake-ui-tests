import sys
from helpers import locators
from helpers import utilities
from helpers import constants
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
sys.path.append("..")


# Wait until the module with given title is displayed
def wait_for_module_to_load(driver, title):
    WebDriverWait(driver, 20).until(
        ec.presence_of_element_located((By.LINK_TEXT, title)))

# Search for a module by title and click on it
def search_for_module_and_click(driver, title):
    utilities.enter_text_by_id(driver, locators.SEARCH_BOX_ID, title)
    utilities.click_element_by_css_selector(driver, locators.SEARCH_BUTTON_CSS)
    utilities.click_element_by_link_text(driver, title)

def get_list_of_recent_modules(driver):
    try:
        wait_for_module_to_load(
            driver, constants.git_import_last_module_uploaded)
    except TimeoutException as e:
        utilities.wait(15)
        wait_for_module_to_load(
            driver, constants.git_import_last_module_uploaded)
    titles_list = driver.find_elements_by_css_selector(locators.MODULE_TITLE_CSS)
    imported_titles = []
    for t in titles_list[:10]:
        imported_titles.append(t.text)
    return imported_titles



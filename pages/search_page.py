import sys
from helpers import locators
from helpers import utilities
import lemoncheesecake.api as lcc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import lemoncheesecake.api as lcc

sys.path.append("..")


# Wait until the module with given title is displayed
def wait_for_module_to_load(driver, title):
    utilities.wait_for_element(driver, By.LINK_TEXT, title)
    # WebDriverWait(driver, 20).until(
    #     ec.presence_of_element_located((By.LINK_TEXT, title)))


# Search for a module by title and click on it
def search_for_module_and_click(driver, title):
    try:
        utilities.enter_text(driver, By.ID, locators.SEARCH_BOX_ID, title)
        utilities.wait(3)
        utilities.click_element(driver, By.CSS_SELECTOR, locators.SEARCH_BUTTON_CSS)
        utilities.wait(3)
        utilities.click_element(driver, By.LINK_TEXT, title)
    except TimeoutException as e:
        lcc.log_info("It appears that the module was not found, please check your test data.")
        raise e

# this method will wait for the last known module to show up on the UI in the list of modules
# and then get you the list of top 10 modules showing up on the UI.
def get_list_of_recent_modules(driver, last_known_module_uploaded):
    try:
        wait_for_module_to_load(driver, last_known_module_uploaded)
    except TimeoutException as e:
        utilities.wait(15)
        wait_for_module_to_load(driver, last_known_module_uploaded)
    titles_list = driver.find_elements_by_css_selector(locators.MODULE_TITLE_CSS)
    imported_titles = []
    for t in titles_list[:10]:
        imported_titles.append(t.text)
    return imported_titles

# Filter the modules listed on the search page by module type
def filter_by_module_type(driver, module_type):
    utilities.wait(2)
    utilities.select_value_from_dropdown(driver, By.CSS_SELECTOR, locators.MODULE_TYPE_DROPDOWN_CSS, module_type)
    utilities.click_element(driver, By.CSS_SELECTOR, locators.SEARCH_BUTTON_CSS)
    utilities.wait(3)

# Returns a list of module types of the modules currently listed on the search page
def get_all_module_types_on_page(driver):
    list = driver.find_elements_by_css_selector(locators.MODULE_TYPE_LIST_CSS)
    type_array = []
    for i in list:
        type_array.append(i.text)
    return (type_array)




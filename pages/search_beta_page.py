from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import polling2

from helpers import utilities, locators
import lemoncheesecake.api as lcc
from lemoncheesecake.matching import *


def select_repo(driver, title):
    lcc.log_info("Selecting repo::{}".format(title))
    utilities.click_element(driver, By.LINK_TEXT, locators.MENU_SEARCH_PAGE_LINK_TEXT)
    utilities.wait(2)
    utilities.enter_text(driver, By.XPATH, locators.FILTER_BY_REPO_SEARCH_BAR_XPATH, title)
    polling2.poll(lambda: len(driver.find_elements(By.CLASS_NAME, locators.SELECT_REPO_CHECKBOX_CLASS_NAME))==1,
                  ignore_exceptions=[NoSuchElementException],
                  timeout=3,
                  step=0.1)
    # utilities.wait(7)
    utilities.click_element(driver, By.CLASS_NAME, locators.SELECT_REPO_CHECKBOX_CLASS_NAME)
    utilities.wait(3)

def search_module_and_click(driver, title):
    lcc.log_info("Searching for title::{}".format(title))
    try:
        wait_for_modules(driver)
        utilities.enter_text(driver, By.CSS_SELECTOR, locators.SEARCH_TITLE_CSS, title)
        # utilities.click_element(driver, By.CSS_SELECTOR, locators.TITLE_SEARCH_ICON_CSS)
        utilities.click_element(driver, By.LINK_TEXT, title)
    except TimeoutException as e:
        lcc.log_info("It appears that the module was not found, please check your test data.")
        raise e

def wait_for_modules(driver):
    utilities.wait_for_element(driver, By.CSS_SELECTOR, locators.MODULES_CSS)

def wait_for_assemblies(driver):
    utilities.wait_for_element(driver, By.CSS_SELECTOR, locators.ASSEMBLY_CSS)

# Filter the modules listed on the search page by module type
def filter_by_content_type(driver, module_type):
    module_type = module_type.upper()
    if module_type == "CONCEPT":
        locator = locators.CONCEPT_CHECKBOX_ID
    elif module_type == "PROCEDURE":
        locator = locators.PROCEDURE_CHECKBOX_ID
    elif module_type == "REFERENCE":
        locator = locators.REFERENCE_CHECKBOX_ID
    else:
        lcc.log_error("Invalid module type!!!")
    utilities.wait(2)
    utilities.click_element(driver, By. CSS_SELECTOR, locators.MODULE_TYPE_DROPDOWN_CSS)
    utilities.click_element(driver, By.ID, locator)
    # utilities.select_value_from_dropdown(driver, By.CSS_SELECTOR, locators.MODULE_TYPE_DROPDOWN_CSS, module_type)
    chips = get_filter_chip_list(driver)
    print(chips)
    print(module_type)
    assert_that("Filter chips listed", chips, has_item(module_type))
    utilities.wait(3)

def get_filter_chip_list(driver):
    list = utilities.find_elements_by_css_selector(driver, locators.FILTER_CHIP_LIST_CSS)
    list_text = []
    for i in list:
        list_text.append(i.text)
    return list_text

# def get_all_module_titles(driver):
#     modules_list = utilities.fi




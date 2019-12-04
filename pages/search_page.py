import helpers.base as base
from helpers import locators
import sys
from helpers import utilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
sys.path.append("..")

# Returns number of modules that have the given source repo name = {source_name}
def count_of_modules_with_the_source_name(driver, source_name):
    list = driver.find_elements_by_xpath(locators.MODULES_WITH_SOURCE_NAME.format(source_name))
    return len(list)

# Wait until the module with given title is displayed
def wait_for_module_to_load(driver, title):
    WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.LINK_TEXT, title)))
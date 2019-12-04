from helpers import utilities
from helpers import locators
from helpers import base
import sys
sys.path.append("..")


username = base.config_reader('login', 'username')
password = base.config_reader('login', 'password')


def login(driver):
    utilities.click_element_by_xpath(driver, locators.LOGIN_TAB_XPATH)
    utilities.enter_text_by_id(driver, locators.USER_NAME_ID, username)
    utilities.enter_text_by_id(driver, locators.PASSWORD_ID, password)
    utilities.click_element_by_class_name(
        driver, locators.LOGIN_BUTTON_CLASS_NAME)


def get_logged_in_username(driver):
    logged_in_user = utilities.find_element_by_partial_text(
        driver, locators.LOGGED_IN_USER_PARTIAL_TEXT).text
    return logged_in_user

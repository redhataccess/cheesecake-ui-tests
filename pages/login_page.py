import helpers.base as base
from helpers.locators import *
import sys
from helpers import utilities
sys.path.append("..")


username = base.config_reader('login', 'username')
password = base.config_reader('login', 'password')


def login(driver):
    utilities.click_element_by_xpath(driver, LOGIN_TAB_XPATH)
    utilities.enter_text_by_id(driver, USER_NAME_ID, username)
    utilities.enter_text_by_id(driver, PASSWORD_ID, password)
    utilities.click_element_by_class_name(driver, LOGIN_BUTTON_CLASS_NAME)


def get_logged_in_username(driver):
    logged_in_user = utilities.find_element_by_partial_text(driver, LOGGED_IN_USER_PARTIAL_TEXT).text
    return logged_in_user


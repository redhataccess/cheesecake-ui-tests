from helpers import utilities
from helpers import locators
from helpers import base
from selenium.webdriver.common.by import By
import sys
sys.path.append("..")


username = base.config_reader('login', 'username')
password = base.config_reader('login', 'password')


def login(driver):
    utilities.click_element(driver, By.XPATH, locators.LOGIN_TAB_XPATH)
    utilities.enter_text(driver, By.ID, locators.USER_NAME_ID, username)
    utilities.enter_text(driver, By.ID, locators.PASSWORD_ID, password)
    utilities.click_element(driver, By.CLASS_NAME, locators.LOGIN_BUTTON_CLASS_NAME)


def get_logged_in_username(driver):
    logged_in_user = utilities.get_text(
        driver, By.PARTIAL_LINK_TEXT, locators.LOGGED_IN_USER_PARTIAL_TEXT)
    return logged_in_user

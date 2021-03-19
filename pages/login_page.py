from helpers import utilities
from helpers import locators
from helpers import base
from fixtures import fixture
from selenium.webdriver.common.by import By
import sys
import lemoncheesecake.api as lcc
from lemoncheesecake.matching import *
sys.path.append("..")


username = base.config_reader('login', 'username')
password = base.config_reader('login', 'password')
sso_url = base.config_reader('qa' , 'sso_url')


def login(driver):
    # utilities.click_element(driver, By.LINK_TEXT, locators.LOGIN_LINK_TEXT)
    assert_that("Assert sso url", driver.current_url, contains_string(sso_url))
    utilities.enter_text(driver, By.ID, locators.USER_NAME_ID, username)
    utilities.click_element(driver, By.ID, locators.LOGIN_NEXT_BUTTON_ID)
    utilities.enter_text(driver, By.ID, locators.PASSWORD_ID, password)
    utilities.click_element(driver, By.ID, locators.LOGIN_BUTTON_ID)
    driver.get(fixture.url + "pantheon/#/")


def get_logged_in_username(driver):
    logged_in_user = utilities.get_text(
        driver, By.PARTIAL_LINK_TEXT, username)
    return logged_in_user

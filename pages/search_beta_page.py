from selenium.webdriver.common.by import By

from helpers import utilities, locators


def search_and_select_repo(driver, title):
    utilities.click_element(driver, By.XPATH, locators.MENU_SEARCH_BETA_XPATH)
    utilities.wait(1)
    utilities.enter_text(driver, By.XPATH, locators.FILTER_BY_REPO_SEARCH_BAR_XPATH, title)
    utilities.wait(1)
    utilities.click_element(driver, By.CLASS_NAME, locators.SELECT_REPO_CHECKBOX_CLASS_NAME)
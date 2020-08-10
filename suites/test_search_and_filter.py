import sys
import lemoncheesecake.api as lcc
from lemoncheesecake.matching import *
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException, NoSuchElementException

from helpers import utilities
from helpers import constants
from helpers import locators
from helpers.base_screenshot import Screenshot
import time
import requests
from fixtures import fixture
from selenium.webdriver.common.by import By

from pages import search_page

sys.path.append("..")


@lcc.suite("Suite: Tests for all the search and filter functionality", rank="8")
class test_search_and_filter(Screenshot):
    driver = lcc.inject_fixture("driver_obj")

    @lcc.test('Verify that search results are as expected')
    def search_for_module(self):
        utilities.click_element(self.driver, By.LINK_TEXT, "Search")
        utilities.wait(2)
        utilities.enter_text(self.driver, By.ID, locators.SEARCH_BOX_ID, constants.module_to_search)
        utilities.click_element(self.driver, By.CSS_SELECTOR, locators.SEARCH_BUTTON_CSS)
        utilities.wait(3)
        check_that("module is found on search page",
                   utilities.get_text(self.driver, By.XPATH, locators.SEARCH_MODULE_XPATH),
                   contains_string(constants.module_to_search))

    @lcc.test("Verify that warning should be displayed when module is not found")
    def search_for_random_text(self):
        utilities.find_elements_by_id(self.driver, locators.SEARCH_BOX_ID).clear()
        utilities.enter_text(self.driver, By.ID, locators.SEARCH_BOX_ID, constants.random_string_search)
        utilities.click_element(self.driver, By.CSS_SELECTOR, locators.SEARCH_BUTTON_CSS)
        utilities.wait(2)
        check_that("warning alert displayed",
                   utilities.get_text(self.driver, By.CSS_SELECTOR, locators.NO_MODULE_FOUND_CSS),
                   contains_string(constants.no_module_found))
        utilities.click_element(self.driver, By.XPATH, locators.CANCEL_BUTTON_XPATH)
        utilities.wait(2)

    @lcc.test("verify that the search results for asian characters such as '安装术语' should give accurate results.")
    def search_for_module_with_asian_chars(self):
        utilities.find_elements_by_id(self.driver, locators.SEARCH_BOX_ID).clear()
        utilities.enter_text(self.driver, By.ID, locators.SEARCH_BOX_ID, constants.asian_char_module)
        # module will be searchable once CCS-3754 is fixed
        # verifying warning alert as of now
        utilities.click_element(self.driver, By.CSS_SELECTOR, locators.SEARCH_BUTTON_CSS)
        utilities.wait(2)
        check_that("module with asian character should be found once CCS-3754 is fixed, checking for warning alert as of now..",
                   utilities.get_text(self.driver, By.CSS_SELECTOR, locators.NO_MODULE_FOUND_CSS),
                   contains_string(constants.no_module_found))
        utilities.click_element(self.driver, By.XPATH, locators.CANCEL_BUTTON_XPATH)
        utilities.wait(2)

    @lcc.test("Verify search results from body of the module")
    def search_for_body_of_module(self):
        utilities.find_elements_by_id(self.driver, locators.SEARCH_BOX_ID).clear()
        utilities.enter_text(self.driver, By.ID, locators.SEARCH_BOX_ID, constants.body_of_module_search)
        utilities.click_element(self.driver, By.CSS_SELECTOR, locators.SEARCH_BUTTON_CSS)
        utilities.wait(2)
        utilities.click_element(self.driver, By.XPATH, locators.SEARCH_MODULE_XPATH)
        utilities.wait(2)
        utilities.click_element(self.driver, By.CSS_SELECTOR, locators.MODULE_DISPLAY_PREVIEW_BUTTON_CSS)
        utilities.wait(2)
        utilities.switch_to_latest_tab(self.driver)
        body_of_module_on_preview = utilities.find_shadow_dom_element(self.driver,locators.SEARCH_BODY_ON_PREVIEW_CSS,
                                                                      locators.MODULE_BODY_ON_PREVIEW_CSS).text
        check_that("content of module is displayed", body_of_module_on_preview,
                   contains_string(constants.body_of_module_search))
        utilities.wait(2)
        self.driver.close()
        utilities.switch_to_first_tab(self.driver)

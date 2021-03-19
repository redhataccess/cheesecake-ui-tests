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
from suites.test_module_type import verify_filter_by_content_type

sys.path.append("..")


@lcc.suite("Suite: Tests for all the search and filter functionality", rank="7")
class test_search_and_filter(Screenshot):
    driver = lcc.inject_fixture("driver_obj")

    @lcc.test('Verify that search results are as expected')
    @lcc.disabled()
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
    @lcc.disabled()
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
    @lcc.disabled()
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
    @lcc.disabled()
    def search_for_body_of_module(self):
        try:
            utilities.find_elements_by_id(self.driver, locators.SEARCH_BOX_ID).clear()
            utilities.enter_text(self.driver, By.ID, locators.SEARCH_BOX_ID, constants.body_of_module_search)
            utilities.click_element(self.driver, By.CSS_SELECTOR, locators.SEARCH_BUTTON_CSS)
            utilities.wait(2)
            utilities.click_element(self.driver, By.XPATH, locators.SEARCH_MODULE_XPATH)
            utilities.wait(2)
            utilities.click_element(self.driver, By.CSS_SELECTOR, locators.MODULE_DISPLAY_PREVIEW_BUTTON_CSS)
            utilities.wait(2)
            utilities.switch_to_latest_tab(self.driver)
            body_of_module_on_preview = utilities.find_shadow_dom_element(self.driver,
                                                                          locators.SEARCH_BODY_ON_PREVIEW_CSS,
                                                                          locators.MODULE_BODY_CSS).text
            check_that("content of module is displayed", body_of_module_on_preview,
                       contains_string(constants.body_of_module_search))
            utilities.wait(2)
        except (TimeoutException, StaleElementReferenceException, NoSuchElementException) as e:
            lcc.log_error("Error finding element: %s" % e)
            lcc.log_error(e)
        finally:
            self.driver.close()
            utilities.switch_to_first_tab(self.driver)


    @lcc.test("Verify that product and version filter works as expected")
    @lcc.disabled()
    def select_product_and_version_filter(self):
        utilities.click_element(self.driver, By.LINK_TEXT, "Search")
        utilities.wait(2)
        utilities.select_value_from_dropdown(self.driver, By.CSS_SELECTOR, locators.SELECT_PRODUCT_NAME_CSS,
                                             constants.product_name)
        utilities.select_value_from_dropdown(self.driver, By.CSS_SELECTOR, locators.SELECT_PRODUCT_VERSION_CSS,
                                             constants.product_version)
        lcc.log_info("product and version selected and displayed on search page")
        utilities.find_element(self.driver, By.XPATH, locators.PRODUCT_FILTER_DISPLAY_XPATH).is_displayed()
        utilities.click_element(self.driver, By.CSS_SELECTOR, locators.SEARCH_BUTTON_CSS)
        utilities.wait(2)
        utilities.click_element(self.driver, By.XPATH, locators.SEARCH_MODULE_XPATH)
        utilities.wait(2)
        check_that("verify that 'filter by product and version' functionality filters results correctly",
                   utilities.get_text(self.driver, By.XPATH, locators.PRODUCT_VERSION_DISPLAY_PAGE_XPATH),
                   contains_string(constants.product_name + " " + constants.product_version))

    @lcc.test("Verify that 'Filter by content Type': Assembly functionality filters results correctly")
    @lcc.disabled()
    def select_content_type_filter(self):
        verify_filter_by_content_type(self.driver, "Assembly")
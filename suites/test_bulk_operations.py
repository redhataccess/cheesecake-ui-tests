import sys
import lemoncheesecake.api as lcc
from lemoncheesecake.matching import *
from helpers import utilities
from helpers import constants
from helpers import locators
from helpers.base_screenshot import Screenshot
from polling2 import poll
from pages import search_beta_page
from fixtures import fixture
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
sys.path.append("..")

url = fixture.url
username = fixture.username
auth = fixture.auth


@lcc.suite("Suite: Verify bulk edit metedata, bulk publish and bulk unpublish", rank=14)
class test_bulk_operations(Screenshot):
    driver = lcc.inject_fixture("driver_obj")

    @lcc.test('Verify user can bulk add metadata for modules')
    # @lcc.disabled()
    def modules_bulk_edit_metadata(self):
        utilities.click_element(self.driver, By.LINK_TEXT, locators.MENU_SEARCH_PAGE_LINK_TEXT)
        utilities.page_reload(self.driver)
        search_beta_page.select_repo(self.driver, fixture.repo_name)
        search_beta_page.search_titles(self.driver, constants.bulk_operations_modules)
        poll(lambda: len(utilities.find_elements_by_css_selector(self.driver, locators.MODULES_LIST_CSS))== 4,
             ignore_exceptions=[NoSuchElementException],
             timeout=5,
             step=0.5)
        utilities.click_element(self.driver, By.XPATH, locators.MODULES_SELECT_ALL_TITLE_XPATH)
        bulk_edit_metadata = utilities.find_element(self.driver, By.XPATH, locators.BULK_EDIT_METADATA_XPATH)
        bulk_publish = utilities.find_element(self.driver, By.CSS_SELECTOR, locators.BULK_PUBLISH_CSS)
        bulk_unpublish = utilities.find_element(self.driver, By.CSS_SELECTOR, locators.BULK_UNPUBLISH_CSS)
        check_that("Edit metadata button is enabled after selecting modules",
                   bulk_edit_metadata.get_attribute("aria-disabled"), equal_to("false"))
        check_that("Publish button is enabled after selecting modules",
                   bulk_publish.get_attribute("aria-disabled"), equal_to("false"))
        check_that("Unpublish button is enabled after selecting modules",
                   bulk_unpublish.get_attribute("aria-disabled"), equal_to("false"))
        bulk_edit_metadata.click()
        check_that("Edit metadata modal title",
                   utilities.get_text(self.driver, By.CSS_SELECTOR, locators.EDIT_METADATA_MODAL_TITLE),
                   equal_to("Edit Metadata"))
        check_that("Count of selected titles",
                   utilities.get_text(self.driver, By.ID, locators.SELECTED_MODULES_COUNT_ID), contains_string("4"))
        search_beta_page.add_bulk_metadata(self.driver)
        poll(lambda: utilities.get_text(self.driver, By.CSS_SELECTOR, locators.PROGRESS_SUCCESS_STATUS) == "100%",
             ignore_exceptions=[NoSuchElementException],
             timeout=20,
             step=1)
        utilities.wait(3)
        utilities.click_element(self.driver, By.XPATH, locators.VIEW_DETAILS_LINK)
        utilities.wait(3)
        modules_updated = utilities.find_elements_by_css_selector(self.driver, locators.UPDATED_TITLES_LIST_CSS)
        check_that("Count of successfully updated modules", len(modules_updated), equal_to(4))
        check_that("Skipped modules section text",
                   utilities.get_text(self.driver, By.CSS_SELECTOR, locators.SKIPPED_TITLE_LIST_CSS), equal_to("n/a"))
        check_that("Failed modules section text",
                   utilities.get_text(self.driver, By.CSS_SELECTOR, locators.FAILED_TITLES_LIST_CSS), equal_to("n/a"))
        utilities.click_element(self.driver, By.XPATH, locators.CLOSE_DETAILS_XPATH)
        utilities.click_element(self.driver, By.CSS_SELECTOR, locators.CLOSE_STATUS_ALERT)

    @lcc.test('Verify user can bulk publish modules')
    # @lcc.disabled()
    def modules_bulk_publish(self):
        poll(lambda: len(utilities.find_elements_by_css_selector(self.driver, locators.MODULES_LIST_CSS)) == 4,
             ignore_exceptions=[NoSuchElementException],
             timeout=5,
             step=0.5)
        utilities.wait(3)
        utilities.click_element(self.driver, By.XPATH, locators.MODULES_SELECT_ALL_TITLE_XPATH)
        utilities.wait(3)
        bulk_publish = utilities.find_element(self.driver, By.CSS_SELECTOR, locators.BULK_PUBLISH_CSS)
        bulk_publish.click()
        check_that("Confirmation modal title",
                   utilities.get_text(self.driver, By.CSS_SELECTOR, locators.MODAL_TITLE_CSS), equal_to("Publish"))
        check_that("Count of modules being published",
                   utilities.get_text(self.driver, By.CSS_SELECTOR, locators.TITLES_FOR_PUBLISH_CSS),
                   contains_string("4"))
        utilities.click_element(self.driver, By.CSS_SELECTOR, locators.CONFIRM_BUTTON_CSS)
        poll(lambda: utilities.get_text(self.driver, By.CSS_SELECTOR, locators.PROGRESS_SUCCESS_STATUS) == "100%",
             ignore_exceptions=[NoSuchElementException],
             timeout=20,
             step=1)
        utilities.click_element(self.driver, By.XPATH, locators.VIEW_DETAILS_LINK)
        modules_updated = utilities.find_elements_by_css_selector(self.driver, locators.UPDATED_TITLES_LIST_CSS)
        check_that("Count of successfully updated modules", len(modules_updated), less_than_or_equal_to(4))
        check_that("Skipped modules section text",
                   utilities.get_text(self.driver, By.CSS_SELECTOR, locators.SKIPPED_TITLE_LIST_CSS), equal_to("n/a"))
        check_that("Failed modules section text",
                   utilities.get_text(self.driver, By.CSS_SELECTOR, locators.FAILED_TITLES_LIST_CSS), equal_to("n/a"))
        utilities.click_element(self.driver, By.XPATH, locators.CLOSE_DETAILS_XPATH)
        utilities.click_element(self.driver, By.CSS_SELECTOR, locators.CLOSE_STATUS_ALERT)

    @lcc.test('Verify user can bulk unpublish modules')
    # @lcc.disabled()
    def modules_bulk_unpublish(self):
        poll(lambda: len(utilities.find_elements_by_css_selector(self.driver, locators.MODULES_LIST_CSS)) == 4,
             ignore_exceptions=[NoSuchElementException],
             timeout=5,
             step=0.5)
        utilities.wait(3)
        utilities.click_element(self.driver, By.XPATH, locators.MODULES_SELECT_ALL_TITLE_XPATH)
        utilities.wait(3)
        # Deselect first title
        utilities.click_element(self.driver, By.XPATH, locators.FIRST_MODULE_CHECKBOX_XPATH)
        utilities.wait(2)
        bulk_unpublish = utilities.find_element(self.driver, By.CSS_SELECTOR, locators.BULK_UNPUBLISH_CSS)
        bulk_unpublish.click()
        check_that("Confirmation modal title",
                   utilities.get_text(self.driver, By.CSS_SELECTOR, locators.MODAL_TITLE_CSS),
                   equal_to("Unpublish"))
        check_that("Count of modules being unpublished",
                   utilities.get_text(self.driver, By.CSS_SELECTOR, locators.TITLES_FOR_UNPUBLISH_CSS),
                   contains_string("3"))
        utilities.click_element(self.driver, By.CSS_SELECTOR, locators.CONFIRM_BUTTON_CSS)
        poll(lambda: utilities.get_text(self.driver, By.CSS_SELECTOR, locators.PROGRESS_SUCCESS_STATUS) == "100%",
             ignore_exceptions=[NoSuchElementException],
             timeout=20,
             step=1)
        utilities.click_element(self.driver, By.XPATH, locators.VIEW_DETAILS_LINK)
        modules_updated = utilities.find_elements_by_css_selector(self.driver, locators.UPDATED_TITLES_LIST_CSS)
        check_that("Count of successfully updated modules", len(modules_updated), equal_to(3))
        check_that("Failed modules section text",
                   utilities.get_text(self.driver, By.CSS_SELECTOR, locators.FAILED_TITLES_LIST_CSS), equal_to("n/a"))
        utilities.click_element(self.driver, By.XPATH, locators.CLOSE_DETAILS_XPATH)
        utilities.wait(2)
        utilities.click_element(self.driver, By.CSS_SELECTOR, locators.CLOSE_STATUS_ALERT)

    @lcc.test('Verify cannot edit metadata for published document')
    # @lcc.disabled()
    def published_title_add_metadata(self):
        utilities.click_element(self.driver, By.XPATH, locators.FIRST_MODULE_CHECKBOX_XPATH)
        utilities.wait(2)
        bulk_edit_metadata = utilities.find_element(self.driver, By.XPATH, locators.BULK_EDIT_METADATA_XPATH)
        bulk_edit_metadata.click()
        utilities.wait(2)
        search_beta_page.add_bulk_metadata(self.driver)
        utilities.wait(2)
        # lcc.log_info("This test is failing currenly to the bug CCS-4444")
        #commenting below check as scope of bug CCS-4444 is deferred , hence checking for skipped and updated modules status
        # check_that("Alert message displayed when trying to add metadata to published title",
        #     utilities.get_text(self.driver, By.CSS_SELECTOR, locators.ALERT_TITLE_CSS),
        #     equal_to(constants.error_message_on_edit_metadata))
        utilities.click_element(self.driver, By.XPATH, locators.VIEW_DETAILS_LINK)
        utilities.wait(3)
        modules_updated = utilities.find_elements_by_css_selector(self.driver, locators.UPDATED_TITLES_LIST_CSS)
        check_that("Count of successfully updated modules", len(modules_updated), equal_to(3))
        modules_skipped = utilities.find_elements_by_css_selector(self.driver, locators.SKIPPED_TITLES_LIST_CSS)
        check_that("Count of skipped modules", len(modules_skipped), equal_to(1))
        utilities.click_element(self.driver, By.XPATH, locators.CLOSE_DETAILS_XPATH)
        utilities.wait(15)
        lcc.log_info("End of tests, executing teardown")
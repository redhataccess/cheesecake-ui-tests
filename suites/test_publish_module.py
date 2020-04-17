import sys
from helpers import base
import lemoncheesecake.api as lcc
from lemoncheesecake.matching import *
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from pages import search_page
from helpers import utilities
from helpers import constants
from helpers import locators
from helpers.base_screenshot import Screenshot
sys.path.append("..")

# SUITE = {
#     "description": "Publish module test",
#     "rank": "4"
# }


@lcc.suite("Suite: Publish module test", rank="4")
class test_publish_module(Screenshot):
    driver = lcc.inject_fixture("driver_obj")

    @lcc.test("Verify that warning is displayed for publish module with no product metadata")
    def no_product_info_publish_module(self):
        utilities.click_element_by_link_text(self.driver, "Search")
        # Click on the title if it is displayed on the first page
        try:
            utilities.click_element_by_link_text(
                self.driver, constants.unpublished_module)
        # If the title is not found on the first page, search for the title and then click
        except (TimeoutException, StaleElementReferenceException) as e:
            lcc.log_info("An exception occurred while looking for the module, searching for the module now...")
            lcc.log_info(e)
            search_page.search_for_module_and_click(
                self.driver, constants.unpublished_module)
        utilities.click_element_by_css_selector(
            self.driver, locators.MODULE_DISPLAY_PUBLISH_BUTTON_CSS)
        check_that("Warning alert contains title", utilities.get_text_by_css(
            self.driver, locators.WARNING_ALERT_CSS), contains_string(constants.module_metadata_warning_title))
        check_that("Warning alert contains description", utilities.get_text_by_css(
            self.driver, locators.WARNING_ALERT_DESCRIPTION_CSS), contains_string(constants.module_metadata_warning))
        check_that("Button contains text", utilities.get_text_by_css(
            self.driver, locators.MODULE_DISPLAY_PUBLISH_BUTTON_CSS), contains_string("Publish"))

    @lcc.test("Verify that user is able to successfully publish module with product metadata added")
    @lcc.depends_on('test_edit_metadata.edit_metadata_successfully')
    def publish_module(self):
        utilities.click_element_by_link_text(self.driver, "Search")
        # Click on the title if it is displayed on the first page
        try:
            utilities.click_element_by_link_text(
                self.driver, constants.module_to_be_published)
        # If the title is not found on the first page, search for the title and then click
        except (TimeoutException, StaleElementReferenceException) as e:
            lcc.log_info("An exception occurred while looking for the module, searching for the module now...")
            lcc.log_info(e)
            search_page.search_for_module_and_click(
                self.driver, constants.module_to_be_published)
        utilities.wait(5)
        utilities.click_element_by_css_selector(
            self.driver, locators.MODULE_DISPLAY_PUBLISH_BUTTON_CSS)
        utilities.find_element_by_partial_text(self.driver, "View on Customer Portal")
        check_that("Button contains text", utilities.get_text_by_css(
            self.driver, locators.MODULE_DISPLAY_PUBLISH_BUTTON_CSS), contains_string("Unpublish"))
        check_that("Button contains text", utilities.get_text_by_css(
            self.driver, locators.MODULE_DISPLAY_PREVIEW_BUTTON_CSS), contains_string("View"))
        check_that("Copy permanent url link is displayed", utilities.get_text_by_css(
            self.driver, locators.COPY_URL_LINK_CSS), contains_string(constants.copy_url_link))
        check_that("View on portal link is displayed", utilities.get_text_by_css(
            self.driver, locators.VIEW_ON_PORTAL_LINK_CSS), contains_string(constants.view_on_portal_link))
        # adding checks if the module is displayed on the UI
        utilities.click_element_by_css_selector(self.driver, locators.VIEW_ON_PORTAL_LINK_CSS)
        utilities.switch_to_latest_tab(self.driver)
        check_that("View on Portal URL path", self.driver.current_url,
                   contains_string(constants.view_on_portal_page_url))

        try:
            module_element_display = utilities.find_element_by_css(self.driver,
                                                                   locators.MODULE_BODY_ON_PORTAL_CSS).is_displayed()
            check_that("Module content displayed on the Customer Portal", module_element_display, is_(True))
        except TimeoutException as e:
            raise e
        finally:
            utilities.switch_to_first_tab(self.driver)


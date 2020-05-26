import datetime
import sys
import time

import lemoncheesecake.api as lcc
from lemoncheesecake.matching import *
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException, NoSuchElementException

from helpers import constants
from helpers import locators
from helpers import utilities
from helpers.base_screenshot import Screenshot
from pages import search_page
from selenium.webdriver.common.by import By

sys.path.append("..")


# SUITE = {
#     "description": "Publish module test",
#     "rank": "4"
# }


@lcc.suite("Suite: Publish module test", rank="4")
class test_publish_module(Screenshot):
    driver = lcc.inject_fixture("driver_obj")
    uploaded_date_module_page = ""
    published_date_module_page = ""
    updated_date_view_page = ""
    published_date_view_page = ""

    @lcc.test("Verify that warning is displayed for publish module with no product metadata")
    def no_product_info_publish_module(self):
        utilities.click_element(self.driver, By.LINK_TEXT, "Search")
        # Click on the title if it is displayed on the first page
        try:
            utilities.click_element(
                self.driver, By.LINK_TEXT, constants.unpublished_module)
        # If the title is not found on the first page, search for the title and then click
        except (TimeoutException, StaleElementReferenceException) as e:
            lcc.log_info("An exception occurred while looking for the module, searching for the module now...")
            lcc.log_info(e)
            search_page.search_for_module_and_click(
                self.driver, constants.unpublished_module)
        utilities.click_element(self.driver, By.CSS_SELECTOR, locators.MODULE_DISPLAY_PUBLISH_BUTTON_CSS)
        check_that("Warning alert contains title",
                   utilities.get_text(self.driver, By.CSS_SELECTOR, locators.WARNING_ALERT_CSS),
                   contains_string(constants.module_metadata_warning_title))
        check_that("Warning alert contains description",
                   utilities.get_text(self.driver, By.CSS_SELECTOR, locators.WARNING_ALERT_DESCRIPTION_CSS),
                   contains_string(constants.module_metadata_warning))
        check_that("Button contains text",
                   utilities.get_text(self.driver, By.CSS_SELECTOR, locators.MODULE_DISPLAY_PUBLISH_BUTTON_CSS),
                   contains_string("Publish"))

    @lcc.test("Verify that user is able to successfully publish module with product metadata added")
    @lcc.depends_on('test_edit_metadata.edit_metadata_successfully')
    def publish_module(self):
        utilities.click_element(self.driver, By.LINK_TEXT, "Search")
        # Click on the title if it is displayed on the first page
        try:
            utilities.click_element(self.driver, By.LINK_TEXT, constants.module_to_be_published)
        # If the title is not found on the first page, search for the title and then click
        except (TimeoutException, StaleElementReferenceException) as e:
            lcc.log_info("An exception occurred while looking for the module, searching for the module now...")
            lcc.log_info(e)
            search_page.search_for_module_and_click(
                self.driver, constants.module_to_be_published)
        utilities.wait(5)
        # Assembly 2 module is being published here
        utilities.click_element(self.driver, By.CSS_SELECTOR, locators.MODULE_DISPLAY_PUBLISH_BUTTON_CSS)
        time.sleep(5)

        # get UPLOADED date in variable and covert into desired format- (DD Month YYYY)
        uploaded_date_module_page_txt = (utilities.get_text(
            self.driver, By.CSS_SELECTOR, locators.UPLOADED_DATE_MODULE_PAGE_CSS))
        lcc.log_info("captured uploaded date from module info page : " + uploaded_date_module_page_txt)
        test_publish_module.uploaded_date_module_page = datetime.datetime.strptime(
            uploaded_date_module_page_txt, "%a %b %d %Y %H:%M:%S %Z%z")
        test_publish_module.uploaded_date_module_page = datetime.datetime.strftime(
            test_publish_module.uploaded_date_module_page, "%d %B %Y")

        # get published date in variable and convert into desired format-(DD Month YYYY)
        published_date_module_page_txt = (utilities.get_text(
            self.driver, By.CSS_SELECTOR, locators.PUBLISHED_DATE_MODULE_PAGE_CSS)).rstrip('\n Version 1')
        lcc.log_info("captured published date from module info page : " + published_date_module_page_txt)
        test_publish_module.published_date_module_page = datetime.datetime.strptime(
            published_date_module_page_txt, "%a %b %d %Y %H:%M:%S %Z%z")
        test_publish_module.published_date_module_page = datetime.datetime.strftime(
            test_publish_module.published_date_module_page, "%d %B %Y")

        utilities.find_element(self.driver, By.PARTIAL_LINK_TEXT, "View on Customer Portal")
        check_that("Button contains text", utilities.get_text(
            self.driver, By.CSS_SELECTOR, locators.MODULE_DISPLAY_PUBLISH_BUTTON_CSS), contains_string("Unpublish"))
        check_that("Button contains text", utilities.get_text(
            self.driver, By.CSS_SELECTOR, locators.MODULE_DISPLAY_PREVIEW_BUTTON_CSS), contains_string("View"))
        check_that("Copy permanent url link is displayed", utilities.get_text(
            self.driver, By.CSS_SELECTOR, locators.COPY_URL_LINK_CSS), contains_string(constants.copy_url_link))
        check_that("View on portal link is displayed", utilities.get_text(
            self.driver, By.CSS_SELECTOR, locators.VIEW_ON_PORTAL_LINK_CSS), contains_string(constants.view_on_portal_link))
        # adding checks if the module is displayed on the UI
        utilities.click_element(self.driver, By.CSS_SELECTOR, locators.VIEW_ON_PORTAL_LINK_CSS)
        utilities.switch_to_latest_tab(self.driver)
        check_that("View on Portal URL path", self.driver.current_url,
                   contains_string(constants.view_on_portal_page_url))

        try:
            module_element_display = utilities.find_element(self.driver, By.CSS_SELECTOR,
                                                            locators.MODULE_BODY_ON_PORTAL_CSS).is_displayed()
            check_that("Module content displayed on the Customer Portal", module_element_display, is_(True))
        except TimeoutException as e:
            raise e
        finally:
            self.driver.close()
            utilities.switch_to_first_tab(self.driver)

    @lcc.test("Verify product info on view page")
    def product_info_on_view_page(self):
        utilities.click_element(self.driver, By.CSS_SELECTOR, locators.MODULE_DISPLAY_PREVIEW_BUTTON_CSS)
        time.sleep(3)
        utilities.switch_to_latest_tab(self.driver)
        # get updated and published date from view page and convert into desired format- (DD Month YYYY)
        test_publish_module.updated_date_view_page = (utilities.get_text(
            self.driver, By.CSS_SELECTOR, locators.UPDATED_DATE_ON_PORTAL_CSS)).strip("Updated ")
        test_publish_module.published_date_view_page = (utilities.get_text(
            self.driver, By.CSS_SELECTOR, locators.PUBLISHED_DATE_ON_PORTAL_CSS)).strip("Published ")

        # adding checks to verify product name,version,updated and published date on view page
        check_that("Product name reflected on view page", utilities.get_text(
            self.driver, By.CSS_SELECTOR, locators.PRODUCT_NAME_CSS), contains_string(constants.product_name.upper()))
        check_that("Product version reflected on view page", utilities.get_text(
            self.driver, By.CSS_SELECTOR, locators.PRODUCT_VERSION_CSS), contains_string(constants.product_version))
        check_that("updated date reflected on view page", test_publish_module.uploaded_date_module_page,
                   equal_to(test_publish_module.updated_date_view_page))
        check_that("published date reflected on view page", test_publish_module.published_date_module_page,
                   equal_to(test_publish_module.published_date_view_page))
        self.driver.close()
        utilities.switch_to_first_tab(self.driver)

    @lcc.test("Verify product info on customer portal")
    def product_info_on_customer_portal(self):
        utilities.click_element(self.driver, By.CSS_SELECTOR, locators.VIEW_ON_PORTAL_LINK_CSS)
        time.sleep(5)
        utilities.switch_to_latest_tab(self.driver)
        try:
            # Trying to look for element that contains the module body <article> </article>
            utilities.find_element(self.driver, By.ID, locators.MODULE_FOUND_ID)

            if utilities.get_text(self.driver, By.CSS_SELECTOR, locators.MODULE_NOT_FOUND_CSS) == constants.module_not_found:
                lcc.log_info("Module not found on customer portal ..")
            else:
                # adding checks to verify product name,version,updated and published date on customer portal
                check_that("Product name reflected on customer portal", utilities.get_text(
                    self.driver, By.CSS_SELECTOR, locators.PRODUCT_NAME_CSS), contains_string(constants.product_name.upper()))
                check_that("Product version reflected on customer portal", utilities.get_text(
                    self.driver, By.CSS_SELECTOR, locators.PRODUCT_VERSION_CSS), contains_string(constants.product_version))
                check_that("updated date reflected on customer portal", test_publish_module.uploaded_date_module_page,
                           equal_to(test_publish_module.updated_date_view_page))
                check_that("published date reflected on customer portal", test_publish_module.published_date_module_page,
                           equal_to(test_publish_module.published_date_view_page))
        except (NoSuchElementException, TimeoutException) as e:
            lcc.log_info("Some problem accessing the Customer Portal, please check.")
            raise e
        finally:
            self.driver.close()
            utilities.switch_to_first_tab(self.driver)

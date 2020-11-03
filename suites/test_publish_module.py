import datetime
import sys
import time

import lemoncheesecake.api as lcc
from lemoncheesecake.matching import *
from selenium.common.exceptions import *
from helpers import constants
from helpers import locators
from helpers import utilities
from helpers.base_screenshot import Screenshot
from datetime import datetime
from pages import search_page
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException, NoSuchElementException
from polling2 import poll

sys.path.append("..")


# SUITE = {
#     "description": "Publish module test",
#     "rank": "4"
# }

@lcc.suite("Suite: Publish module test", rank="5")
class test_publish_module(Screenshot):
    driver = lcc.inject_fixture("driver_obj")
    uploaded_date_module_page = ""
    published_date_module_page = ""
    updated_date_view_page = ""
    published_date_view_page = ""

    @lcc.test("Verify that warning is displayed for publish module with no product metadata")
    def no_product_info_publish_module(self):
        utilities.click_element(self.driver, By.LINK_TEXT, "Search")
        # # Click on the title if it is displayed on the first page
        utilities.wait(5)
        search_page.search_for_module_and_click(self.driver, constants.unpublished_module)
        utilities.wait(5)
        utilities.click_element(self.driver, By.CSS_SELECTOR, locators.MODULE_DISPLAY_PUBLISH_BUTTON_CSS)
        check_that("Button contains text",
                   utilities.get_text(self.driver, By.CSS_SELECTOR, locators.MODULE_DISPLAY_PUBLISH_BUTTON_CSS),
                   contains_string("Publish"))

    @lcc.test("Verify that user is able to successfully publish module with product metadata added")
    @lcc.depends_on('test_edit_metadata.edit_metadata_successfully')
    def publish_module(self):
        try:
            utilities.click_element(self.driver, By.LINK_TEXT, "Search")
            search_page.search_for_module_and_click(self.driver, constants.module_to_be_published)
            utilities.wait(10)
            utilities.click_element(self.driver, By.CSS_SELECTOR, locators.MODULE_DISPLAY_PUBLISH_BUTTON_CSS)
            utilities.wait(20)
            # The page needs a refresh because of an existing bug about the "View on Customer Portal not appearing"
            # self.driver.refresh()

            utilities.find_element(self.driver, By.PARTIAL_LINK_TEXT, "View on Customer Portal")
            check_that("Button contains text", utilities.get_text(
                self.driver, By.CSS_SELECTOR, locators.MODULE_DISPLAY_PUBLISH_BUTTON_CSS), contains_string("Unpublish"))
            check_that("Button contains text", utilities.get_text(
                self.driver, By.CSS_SELECTOR, locators.MODULE_DISPLAY_PREVIEW_BUTTON_CSS), contains_string("Preview"))
            check_that("Copy permanent url link is displayed", utilities.get_text(
                self.driver, By.CSS_SELECTOR, locators.COPY_URL_LINK_CSS), contains_string(constants.copy_url_link))
            check_that("View on portal link is displayed", utilities.get_text(
                self.driver, By.CSS_SELECTOR, locators.VIEW_ON_PORTAL_LINK_CSS),
                       contains_string(constants.view_on_portal_link))

            # get UPLOADED date in variable and covert into desired format- (DD Month YYYY)
            test_publish_module.uploaded_date_module_page = (utilities.get_text(
                self.driver, By.CSS_SELECTOR, locators.UPLOADED_DATE_MODULE_PAGE_CSS))
            lcc.log_info(
                "captured uploaded date from module info page : " + test_publish_module.uploaded_date_module_page)

            # get published date in variable and convert into desired format-(DD Month YYYY)
            test_publish_module.published_date_module_page = (utilities.get_text(
                self.driver, By.CSS_SELECTOR, locators.PUBLISHED_DATE_MODULE_PAGE_CSS)).rstrip('\n Version released')
            lcc.log_info(
                "captured published date from module info page : " + test_publish_module.published_date_module_page)

            # adding checks if the module is displayed on the UI
            utilities.click_element(self.driver, By.CSS_SELECTOR, locators.VIEW_ON_PORTAL_LINK_CSS)
            utilities.wait(5)
            utilities.switch_to_latest_tab(self.driver)
            utilities.wait(10)
            check_that("View on Portal URL path", self.driver.current_url,
                       contains_string(constants.view_on_portal_page_url))
            utilities.wait(6)
            # module_element_display = utilities.find_element(self.driver, By.CSS_SELECTOR,
            #                                                 locators.MODULE_BODY_ON_PORTAL_CSS).is_displayed()
            # check_that("Module content displayed on the Customer Portal", module_element_display, is_(True))
        except (TimeoutException, StaleElementReferenceException, NoSuchElementException) as e:
            lcc.log_error("Element could not be located!!!")
            lcc.log_error(e)
        finally:
            self.driver.close()
            utilities.switch_to_first_tab(self.driver)

    @lcc.test("Verify product info on view page")
    def product_info_on_view_page(self):
        utilities.click_element(self.driver, By.CSS_SELECTOR, locators.MODULE_DISPLAY_PREVIEW_BUTTON_CSS)
        utilities.switch_to_latest_tab(self.driver)
        utilities.wait(2)
        try:
            product_name = utilities.find_shadow_dom_element(self.driver, locators.PRODUCT_NAME_ON_PREVIEW_CSS,
                                                             locators.MODULE_BODY_ON_PREVIEW_CSS).text
            check_that("Product name reflected on view page", product_name,
                       contains_string(constants.product_name))
            product_version = utilities.find_shadow_dom_element(self.driver,
                                                                locators.PRODUCT_VERSION_ON_PREVIEW_CSS,
                                                                locators.MODULE_BODY_ON_PREVIEW_CSS).text
            check_that("Product version reflected on view page", product_version,
                       contains_string(constants.product_version))
            test_publish_module.updated_date_view_page = utilities.find_shadow_dom_element(self.driver,
                                                                                           locators.UPDATED_DATE_ON_PREVIEW_CSS,
                                                                                           locators.MODULE_BODY_ON_PREVIEW_CSS).text.strip(
                "Updated ")
            check_that("updated date reflected on view page", test_publish_module.updated_date_view_page,
                       contains_string(test_publish_module.uploaded_date_module_page))
            test_publish_module.published_date_view_page = utilities.find_shadow_dom_element(self.driver,
                                                                                             locators.PUBLISHED_DATE_ON_PREVIEW_CSS,
                                                                                             locators.MODULE_BODY_ON_PREVIEW_CSS).text.strip(
                "Published ")
            check_that("published date reflected on view page", test_publish_module.published_date_view_page,
                       contains_string(test_publish_module.published_date_module_page))
        except (TimeoutException, StaleElementReferenceException, NoSuchElementException) as e:
            lcc.log_error("Element could not be located!!!")
            lcc.log_error(e)
        finally:
            self.driver.close()
            utilities.switch_to_first_tab(self.driver)

    @lcc.test("Verify product info on customer portal")
    def product_info_on_customer_portal(self):
        time.sleep(5)
        utilities.click_element(self.driver, By.PARTIAL_LINK_TEXT, "View on Customer Portal")
        time.sleep(5)
        utilities.switch_to_latest_tab(self.driver)
        lcc.log_info("Find the CP preview in the attachment below for debugging purposes")
        self.driver.save_screenshot("cp_preview_.png")
        lcc.save_attachment_file("cp_preview_.png")
        utilities.wait(6)
        try:
            product_name = utilities.find_shadow_dom_element(self.driver, locators.PRODUCT_NAME_ON_PREVIEW_CSS,
                                                             locators.MODULE_BODY_ON_PORTAL_CSS).text
            product_version = utilities.find_shadow_dom_element(self.driver, locators.PRODUCT_VERSION_ON_PREVIEW_CSS,
                                                                locators.MODULE_BODY_ON_PORTAL_CSS).text
            check_that("Product name reflected on customer portal", product_name,
                       contains_string(constants.product_name))
            check_that("Product version reflected on customer portal", product_version,
                       contains_string(constants.product_version))
            check_that("updated date reflected on customer portal", test_publish_module.updated_date_view_page,
                       equal_to(test_publish_module.uploaded_date_module_page))
            check_that("published date reflected on customer portal", test_publish_module.published_date_view_page,
                       equal_to(test_publish_module.published_date_module_page))
        except (TimeoutException, StaleElementReferenceException, NoSuchElementException) as e:
            lcc.log_error("Some problem accessing the Customer Portal, please check.")
            lcc.log_error(e)
        finally:
            self.driver.close()
            utilities.switch_to_first_tab(self.driver)

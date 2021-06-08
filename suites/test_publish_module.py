import datetime
import sys
import time
import requests

import lemoncheesecake.api as lcc
from lemoncheesecake.matching import *
from selenium.common.exceptions import *

from fixtures.fixture import admin_username, admin_auth
from helpers import constants, base
from helpers import locators
from helpers import utilities
from fixtures import fixture
from helpers.base_screenshot import Screenshot
from datetime import datetime
from pages import search_page
from pages import search_beta_page
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException, NoSuchElementException
from polling2 import poll

sys.path.append("..")
username = base.config_reader('login', 'username')
auth = base.config_reader('login', 'password')
api_auth = base.config_reader('login', 'api_password')


# SUITE = {
#     "description": "Publish module test",
#     "rank": "4"
# }

@lcc.suite("Suite: Publish module test", rank=5)
class test_publish_module(Screenshot):
    driver = lcc.inject_fixture("driver_obj")
    first_pub_date_details_page = ""
    last_pub_date_details_page = ""

    # updated_date_view_page = ""
    # published_date_view_page = ""

    @lcc.test("Verify that warning is displayed for publish module with no product metadata")
    def no_product_info_publish_module(self):
        utilities.click_element(self.driver, By.LINK_TEXT, "Search")
        utilities.page_reload(self.driver)
        # # Click on the title if it is displayed on the first page
        utilities.wait(5)
        # search_page.search_for_module_and_click(self.driver, constants.unpublished_module)
        search_beta_page.select_repo(self.driver, fixture.repo_name)
        search_beta_page.search_module_and_click(self.driver, constants.unpublished_module)
        utilities.wait(5)
        tooltip_icon = utilities.find_element(self.driver, By.CSS_SELECTOR, locators.NO_URL_TOOLTIP_ICON)
        check_that("No url tooltip icon is displayed", tooltip_icon.is_displayed(), is_true())
        utilities.click_element(self.driver, By.ID, locators.MODULE_DISPLAY_PUBLISH_BUTTON_ID)
        check_that("Button contains text",
                   utilities.get_text(self.driver, By.ID, locators.MODULE_DISPLAY_PUBLISH_BUTTON_ID),
                   contains_string("Publish"))

    @lcc.test("Verify that user is able to successfully publish module with product metadata added")
    @lcc.depends_on('test_edit_metadata.edit_metadata_successfully')
    def publish_module(self):
        utilities.click_element(self.driver, By.LINK_TEXT, "Search")
        utilities.page_reload(self.driver)
        # search_page.search_for_module_and_click(self.driver, constants.module_to_be_published)
        search_beta_page.select_repo(self.driver, fixture.repo_name)
        search_beta_page.search_module_and_click(self.driver, constants.module_to_be_published)
        utilities.wait(10)

        pre_live_url = utilities.find_element(self.driver, By.LINK_TEXT, "Pre-live Customer Portal URL")
        print(pre_live_url.get_attribute('href'))
        check_that("Pre-live URL link is displayed", pre_live_url.is_displayed(), is_true())
        copy_pre_live_url = utilities.find_element(self.driver, By.LINK_TEXT, "Copy pre-live URL")
        check_that("Copy Pre-live URL is displayed", copy_pre_live_url.is_displayed(), is_true())

        utilities.click_element(self.driver, By.ID, locators.MODULE_DISPLAY_PUBLISH_BUTTON_ID)
        utilities.wait(20)
        print("Clicked publish")
        # The page needs a refresh because of an existing bug about the "View on Customer Portal not appearing"
        self.driver.refresh()
        utilities.find_element(self.driver, By.PARTIAL_LINK_TEXT, "View on Customer Portal")
        check_that("Button contains text", utilities.get_text(
            self.driver, By.ID, locators.MODULE_DISPLAY_UNPUBLISH_BUTTON_ID), contains_string("Unpublish"))
        check_that("Button contains text", utilities.get_text(
            self.driver, By.CSS_SELECTOR, locators.MODULE_DISPLAY_PREVIEW_BUTTON_CSS), contains_string("Preview"))
        check_that("Copy permanent url link is displayed", utilities.get_text(
            self.driver, By.CSS_SELECTOR, locators.COPY_URL_LINK_CSS), contains_string(constants.copy_url_link))
        check_that("View on portal link is displayed", utilities.get_text(
            self.driver, By.CSS_SELECTOR, locators.VIEW_ON_PORTAL_LINK_CSS),
                   contains_string(constants.view_on_portal_link))

        # get UPLOADED date in variable and covert into desired format- (DD Month YYYY)
        self.first_pub_date_details_page = (utilities.get_text(
            self.driver, By.CSS_SELECTOR, locators.FIRST_PUB_DATE_MODULE_PAGE_CSS))
        lcc.log_info(
            "captured 1st published date from module info page : " + self.first_pub_date_details_page)

        # get published date in variable and convert into desired format-(DD Month YYYY)
        self.last_pub_date_details_page = (utilities.get_text(
            self.driver, By.CSS_SELECTOR, locators.LAST_PUB_DATE_MODULE_PAGE_CSS))
        lcc.log_info(
            "captured last published date from module info page : " + test_publish_module.last_pub_date_details_page)

        # adding checks if the module is displayed on the UI
        utilities.click_element(self.driver, By.CSS_SELECTOR, locators.VIEW_ON_PORTAL_LINK_CSS)
        utilities.wait(5)
        try:
            utilities.switch_to_latest_tab(self.driver)
            utilities.wait(10)
            check_that("View on Portal URL path", self.driver.current_url,
                       contains_string(constants.view_on_portal_page_url))
        except (TimeoutException, StaleElementReferenceException, NoSuchElementException) as e:
            lcc.log_error("Element could not be located!!!")
            lcc.log_error(e)
        finally:
            if (len(self.driver.window_handles) > 1):
                self.driver.close()
                utilities.switch_to_first_tab(self.driver)

    @lcc.test("Verify product info on view page")
    def product_info_on_view_page(self):
        utilities.click_element(self.driver, By.CSS_SELECTOR, locators.MODULE_DISPLAY_PREVIEW_BUTTON_CSS)
        try:
            utilities.switch_to_latest_tab(self.driver)
            utilities.wait(2)
            product_name = utilities.find_shadow_dom_element(self.driver, locators.PRODUCT_NAME_ON_PREVIEW_CSS,
                                                             locators.MODULE_BODY_CONTENT_CSS).text
            check_that("Product name reflected on view page", product_name,
                       contains_string(constants.product_name))
            product_version = utilities.find_shadow_dom_element(self.driver,
                                                                locators.PRODUCT_VERSION_ON_PREVIEW_CSS,
                                                                locators.MODULE_BODY_CONTENT_CSS).text
            check_that("Product version reflected on view page", product_version,
                       contains_string(constants.product_version))
            updated_date_view_page = utilities.find_shadow_dom_element(self.driver,
                                                                       locators.UPDATED_DATE_ON_PREVIEW_CSS,
                                                                       locators.MODULE_BODY_CONTENT_CSS).text.strip(
                "Updated ")
            check_that("updated date reflected on view page", updated_date_view_page,
                       contains_string(self.first_pub_date_details_page))
            published_date_view_page = utilities.find_shadow_dom_element(self.driver,
                                                                         locators.PUBLISHED_DATE_ON_PREVIEW_CSS,
                                                                         locators.MODULE_BODY_CONTENT_CSS).text.strip(
                "Published ")
            check_that("published date reflected on view page", published_date_view_page,
                       contains_string(self.last_pub_date_details_page))
            legal_notice = utilities.find_shadow_dom_element(self.driver, locators.LEGAL_NOTICE_ON_PREVIEW_CSS,
                                                             locators.MODULE_BODY_CONTENT_CSS)
            check_that("legal notice is displayed at the bottom of preview page", legal_notice.text,
                       contains_string("Legal Notices for Trademarks"))
            legal_notice_href = legal_notice.get_attribute("href")
            check_that("verify legal notice link", legal_notice_href, contains_string(constants.legal_notice_link))

        except (TimeoutException, StaleElementReferenceException, NoSuchElementException) as e:
            lcc.log_error("Element could not be located!!!")
            lcc.log_error(e)
        finally:
            if (len(self.driver.window_handles) > 1):
                self.driver.close()
                utilities.switch_to_first_tab(self.driver)

    @lcc.test("Verify info on customer portal")
    def product_info_on_customer_portal(self):
        utilities.wait(5)
        utilities.page_reload(self.driver)
        utilities.click_element(self.driver, By.PARTIAL_LINK_TEXT, "View on Customer Portal")
        try:
            utilities.wait(5)
            utilities.switch_to_latest_tab(self.driver)
            utilities.wait(6)
            updated_date_on_portal = utilities.find_shadow_dom_element(self.driver, locators.UPDATED_DATE_ON_PORTAL_CSS,
                                                                       locators.MODULE_BODY_ON_PORTAL_CSS).get_attribute(
                "textContent")
            check_that("updated date reflected on view page", updated_date_on_portal,
                       contains_string(self.first_pub_date_details_page))
            published_date_on_portal = utilities.find_shadow_dom_element(self.driver,
                                                                         locators.PUBLISHED_DATE_ON_PORTAL_CSS,
                                                                         locators.MODULE_BODY_ON_PORTAL_CSS).get_attribute(
                "textContent")
            check_that("published date reflected on view page", published_date_on_portal,
                       contains_string(self.last_pub_date_details_page))
        except (TimeoutException, StaleElementReferenceException, NoSuchElementException) as e:
            lcc.log_error("Some problem accessing the Customer Portal, please check.")
            lcc.log_error(e)
        finally:
            if (len(self.driver.window_handles) > 1):
                self.driver.close()
                utilities.switch_to_first_tab(self.driver)

    def teardown_suite(self):
        response = unpublish_module(self, constants.module_to_unpublish, constants.variant)
        check_that("Unpublish request status code", response.status_code, equal_to(200))
        lcc.log_info("Module published for above test is unpublished successfully..")


def unpublish_module(self, module_path, variant):
    unpublish_url = fixture.url + module_path
    lcc.log_info("Unpublishing the module: %s" % unpublish_url)
    payload = {
        ":operation": "pant:unpublish",
        "locale": "en_US",
        "variant": variant
    }
    response = requests.post(unpublish_url, data=payload, auth=(admin_username, admin_auth),
                             headers={'Accept': 'application/json'})
    return response

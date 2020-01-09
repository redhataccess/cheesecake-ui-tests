import sys
from helpers import base
import lemoncheesecake.api as lcc
from lemoncheesecake.matching import *
from selenium.common.exceptions import TimeoutException
from pages import search_page
from helpers import utilities
from helpers import constants
from helpers import locators
sys.path.append("..")

SUITE = {
    "description": "Publish module test",
    "rank": "4"
}


@lcc.test("Verify that warning is displayed for publish module with no product metadata")
def no_product_info_publish_module(driver):
    utilities.click_element_by_link_text(driver, "Search")
    # Click on the title if it is displayed on the first page
    try:
        utilities.click_element_by_link_text(
            driver, constants.unpublished_module)
    # If the title is not found on the first page, search for the title and then click
    except TimeoutException as e:
        search_page.search_for_module_and_click(
            driver, constants.unpublished_module)
    utilities.click_element_by_css_selector(
        driver, locators.MODULE_DISPLAY_PUBLISH_BUTTON_CSS)
    check_that("Warning alert contains title", utilities.get_text_by_css(
        driver, locators.WARNING_ALERT_CSS), contains_string(constants.module_metadata_warning_title))
    check_that("Warning alert contains description", utilities.get_text_by_css(
        driver, locators.WARNING_ALERT_DESCRIPTION_CSS), contains_string(constants.module_metadata_warning))
    check_that("Button contains text", utilities.get_text_by_css(
        driver, locators.MODULE_DISPLAY_PUBLISH_BUTTON_CSS), contains_string("Publish"))


@lcc.test("Verify that user is able to successfully publish module with product metadata added")
def publish_module(driver):
    utilities.click_element_by_link_text(driver, "Search")
    # Click on the title if it is displayed on the first page
    try:
        utilities.click_element_by_link_text(
            driver, constants.module_to_be_published)
    # If the title is not found on the first page, search for the title and then click
    except TimeoutException as e:
        search_page.search_for_module_and_click(
            driver, constants.module_to_be_published)
    utilities.wait(5)
    utilities.click_element_by_css_selector(
        driver, locators.MODULE_DISPLAY_PUBLISH_BUTTON_CSS)
    utilities.find_element_by_partial_text(driver, "View on Customer Portal")
    check_that("Button contains text", utilities.get_text_by_css(
        driver, locators.MODULE_DISPLAY_PUBLISH_BUTTON_CSS), contains_string("Unpublish"))
    check_that("Button contains text", utilities.get_text_by_css(
        driver, locators.MODULE_DISPLAY_PREVIEW_BUTTON_CSS), contains_string("View"))
    check_that("Copy permanent url link is displayed", utilities.get_text_by_css(
        driver, locators.COPY_URL_LINK_CSS), contains_string(constants.copy_url_link))
    check_that("View on portal link is displayed", utilities.get_text_by_css(
        driver, locators.VIEW_ON_PORTAL_LINK_CSS), contains_string(constants.view_on_portal_link))

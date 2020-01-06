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
    "description": "View module test",
    "rank": "5"
}


@lcc.test("Authenticated user view unpublished module")
def authenticated_user_view_unpublished_module(driver):
    utilities.click_element_by_link_text(driver, "Search")
    # Click on the title if it is displayed on the first page
    try:
        utilities.click_element_by_link_text(
            driver, constants.unpublished_module)
    # If the title is not found on the first page, search for the title and then click
    except TimeoutException as e:
        search_page.search_for_module_and_click(
            driver, constants.unpublished_module)
    check_that("Button contains text", utilities.get_text_by_css(
        driver, locators.MODULE_DISPLAY_PUBLISH_BUTTON_CSS), contains_string("Publish"))
    check_that("Button contains text", utilities.get_text_by_css(
        driver, locators.MODULE_DISPLAY_PREVIEW_BUTTON_CSS), contains_string("Preview"))
    check_that("Publish status", utilities.get_text_by_xpath(
        driver, locators.MODULE_DISPLAY_PUBLISH_STATUS_XPATH), contains_string("Not published"))
    check_that("Module display page title", utilities.get_text_by_css(
        driver, locators.MODULE_DISPLAY_TITLE_CSS), contains_string(constants.unpublished_module))


@lcc.test("Authenticated user view published module")
def authenticated_user_view_published_module(driver):
    utilities.click_element_by_link_text(driver, "Search")
    # Click on the title if it is displayed on the first page
    try:
        utilities.click_element_by_link_text(
            driver, constants.module_to_be_published)
    # If the title is not found on the first page, search for the title and then click
    except TimeoutException as e:
        search_page.search_for_module_and_click(
            driver, constants.module_to_be_published)
    utilities.find_element_by_css(
        driver, locators.MODULE_DISPLAY_PUBLISH_BUTTON_CSS)
    check_that("Button contains text", utilities.get_text_by_css(
        driver, locators.MODULE_DISPLAY_PUBLISH_BUTTON_CSS), contains_string("Unpublish"))

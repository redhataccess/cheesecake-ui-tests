import sys
import re
from helpers import base
import lemoncheesecake.api as lcc
from lemoncheesecake.matching import *
from selenium.common.exceptions import TimeoutException
from pages import search_page
from helpers import utilities
from helpers import constants
from helpers import locators
from fixtures import fixture
sys.path.append("..")

SUITE = {
    "description": "View module test",
    "rank": "5"
}

url = fixture.url


@lcc.test("Verify that for authenticated user an unpublished module displays all expected fields")
@lcc.depends_on('test_publish_module.publish_module')
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
    check_that("URL", driver.current_url, contains_string(
        url+constants.module_display_page_path_unpublished))
    check_that("Button", utilities.get_text_by_css(
        driver, locators.MODULE_DISPLAY_PUBLISH_BUTTON_CSS), contains_string("Publish"))
    check_that("Button", utilities.get_text_by_css(
        driver, locators.MODULE_DISPLAY_PREVIEW_BUTTON_CSS), contains_string("Preview"))
    check_that("Publish status", utilities.get_text_by_xpath(
        driver, locators.MODULE_DISPLAY_PUBLISH_STATUS_XPATH), contains_string("Not published"))
    check_that("Module display page title", utilities.get_text_by_css(
        driver, locators.MODULE_DISPLAY_TITLE_CSS), contains_string(constants.unpublished_module))


@lcc.test("Verify that for authenticated user a published module displays all expected fields")
@lcc.depends_on('test_publish_module.publish_module')
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
    check_that("URL", driver.current_url,
               contains_string(url + constants.module_display_page_path_published))
    check_that("Button", utilities.get_text_by_css(
        driver, locators.MODULE_DISPLAY_PUBLISH_BUTTON_CSS), contains_string("Unpublish"))


@lcc.test("Verify that view on portal link navigates to correct page and verify its content")
@lcc.depends_on('test_publish_module.publish_module')
def view_on_portal_link_test(driver):
    utilities.click_element_by_css_selector(
        driver, locators.VIEW_ON_PORTAL_LINK_CSS)
    utilities.switch_to_latest_tab(driver)
    check_that("View on Portal URL path", driver.current_url,
               contains_string(constants.view_on_portal_page_url))
    module_id_regex = re.compile(
        r'^[a-zA-Z0-9]{8}-[a-zA-Z0-9]{4}-[a-zA-Z0-9]{4}-[a-zA-Z0-9]{4}-[a-zA-Z0-9]{12}$')
    current__module_id = driver.current_url.split("/topics/en-us/")[1]
    check_that("View on Portal URL id",
               current__module_id, match_pattern(module_id_regex))
    try:
        check_that("Module content displayed on the Customer Portal", utilities.find_element_by_css(
        driver, locators.MODULE_BODY_ON_PORTAL_CSS).is_displayed(), is_(True))
    except TimeoutException as e:
        raise e
    finally:
        utilities.switch_to_first_tab(driver)

import sys
import lemoncheesecake.api as lcc
from lemoncheesecake.matching import *
from selenium.common.exceptions import TimeoutException
from pages import display_module_page
from pages import search_page
from helpers import utilities
from helpers import constants
from helpers import locators
sys.path.append("..")

SUITE = {
    "description": "Edit metadata for a module",
    "rank": "3"
}

@lcc.test("Warning should be displayed on Edit Metadata modal when no data is entered")
def edit_metadata_blank_data(driver):
    utilities.click_element_by_link_text(driver, "Search")
    # Click on the title if it is displayed on the first page
    try:
        utilities.click_element_by_link_text(driver, constants.module_to_be_published)
    # If the title is not found on the first page, search for the title and then click
    except TimeoutException as e:
        search_page.search_for_module_and_click(driver, constants.module_to_be_published)
    utilities.click_element_by_css_selector(driver, locators.EDIT_METADATA_DROPDOWN_CSS)
    utilities.click_element_by_css_selector(driver, locators.EDIT_METADATA_BUTTON_CSS)
    check_that("Edit metadata modal title", utilities.get_text_by_css(driver, locators.EDIT_METADATA_MODAL_TITLE_CSS),
               contains_string(constants.edit_metadata_modal_title))
    utilities.click_element_by_css_selector(driver, locators.EDIT_METADATA_SAVE_CSS)
    check_that("Warning displayed", utilities.get_text_by_css(driver, locators.WARNING_ALERT_CSS),
               contains_string(constants.edit_metadata_modal_warning))
    utilities.click_element_by_css_selector(driver, locators.CLOSE_WARNING_ALERT_CSS)

@lcc.test("Warning should be displayed on Edit Metadata modal when URL fragment field is blank")
def edit_metadata_empty_url_fragment(driver):
    display_module_page.reset_edit_metadata_from(driver)
    utilities.select_value_from_dropdown(driver, locators.PRODUCT_NAME_DROPDOWN_CSS, constants.product_name)
    utilities.select_value_from_dropdown(driver, locators.PRODUCT_VERSION_DROPDOWN_CSS, constants.product_version)
    utilities.select_value_from_dropdown(driver, locators.PRODUCT_USECASE_DROPDOWN_CSS, constants.use_case)
    # utilities.enter_text_by_css_selector(driver, locators.PRODUCT_URLFRAGMENT_CSS, constants.url_fragment)
    utilities.click_element_by_css_selector(driver, locators.EDIT_METADATA_SAVE_CSS)
    check_that("Warning displayed", utilities.get_text_by_css(driver, locators.WARNING_ALERT_CSS),
               contains_string(constants.edit_metadata_modal_warning))
    utilities.click_element_by_css_selector(driver, locators.CLOSE_WARNING_ALERT_CSS)

@lcc.test("Warning should be displayed on Edit Metadata modal when Product name field is blank")
def edit_metadata_empty_productname(driver):
    display_module_page.reset_edit_metadata_from(driver)
    # utilities.select_value_from_dropdown(driver, locators.PRODUCT_NAME_DROPDOWN_CSS, constants.product_name)
    # utilities.select_value_from_dropdown(driver, locators.PRODUCT_VERSION_DROPDOWN_CSS, constants.product_version)
    utilities.select_value_from_dropdown(driver, locators.PRODUCT_USECASE_DROPDOWN_CSS, constants.use_case)
    utilities.enter_text_by_css_selector(driver, locators.PRODUCT_URLFRAGMENT_CSS, constants.url_fragment)
    utilities.click_element_by_css_selector(driver, locators.EDIT_METADATA_SAVE_CSS)
    check_that("Warning displayed", utilities.get_text_by_css(driver, locators.WARNING_ALERT_CSS),
               contains_string(constants.edit_metadata_modal_warning))
    utilities.click_element_by_css_selector(driver, locators.CLOSE_WARNING_ALERT_CSS)

@lcc.test("Warning should be displayed on Edit Metadata modal when Product version field is blank")
def edit_metadata_empty_version(driver):
    display_module_page.reset_edit_metadata_from(driver)
    utilities.select_value_from_dropdown(driver, locators.PRODUCT_NAME_DROPDOWN_CSS, constants.product_name)
    # utilities.select_value_from_dropdown(driver, locators.PRODUCT_VERSION_DROPDOWN_CSS, constants.product_version)
    utilities.select_value_from_dropdown(driver, locators.PRODUCT_USECASE_DROPDOWN_CSS, constants.use_case)
    utilities.enter_text_by_css_selector(driver, locators.PRODUCT_URLFRAGMENT_CSS, constants.url_fragment)
    utilities.click_element_by_css_selector(driver, locators.EDIT_METADATA_SAVE_CSS)
    check_that("Warning displayed", utilities.get_text_by_css(driver, locators.WARNING_ALERT_CSS),
               contains_string(constants.edit_metadata_modal_warning))
    utilities.click_element_by_css_selector(driver, locators.CLOSE_WARNING_ALERT_CSS)

@lcc.test("Warning should be displayed on Edit Metadata modal when Usecase field is blank")
def edit_metadata_empty_usecase(driver):
    display_module_page.reset_edit_metadata_from(driver)
    utilities.select_value_from_dropdown(driver, locators.PRODUCT_NAME_DROPDOWN_CSS, constants.product_name)
    utilities.select_value_from_dropdown(driver, locators.PRODUCT_VERSION_DROPDOWN_CSS, constants.product_version)
    # utilities.select_value_from_dropdown(driver, locators.PRODUCT_USECASE_DROPDOWN_CSS, constants.use_case)
    utilities.enter_text_by_css_selector(driver, locators.PRODUCT_URLFRAGMENT_CSS, constants.url_fragment)
    utilities.click_element_by_css_selector(driver, locators.EDIT_METADATA_SAVE_CSS)
    check_that("Warning displayed", utilities.get_text_by_css(driver, locators.WARNING_ALERT_CSS),
               contains_string(constants.edit_metadata_modal_warning))
    utilities.click_element_by_css_selector(driver, locators.CLOSE_WARNING_ALERT_CSS)

@lcc.test("User should be able to add product metadata successfully")
def edit_metadata_successfully(driver):
    display_module_page.reset_edit_metadata_from(driver)
    utilities.select_value_from_dropdown(driver, locators.PRODUCT_NAME_DROPDOWN_CSS, constants.product_name)
    utilities.select_value_from_dropdown(driver, locators.PRODUCT_VERSION_DROPDOWN_CSS, constants.product_version)
    utilities.select_value_from_dropdown(driver, locators.PRODUCT_USECASE_DROPDOWN_CSS, constants.use_case)
    utilities.enter_text_by_css_selector(driver, locators.PRODUCT_URLFRAGMENT_CSS, constants.url_fragment)
    utilities.click_element_by_css_selector(driver, locators.EDIT_METADATA_SAVE_CSS)
    check_that("Success message displayed",
               utilities.get_text_by_css(driver, locators.UPDATE_SUCCESS_MESSAGE_CSS),
               contains_string(constants.success_message))
    check_that("Product name reflected on displayed module page", utilities.get_text_by_css(driver, locators.PRODUCT_INFO_CSS),
               contains_string(constants.product_name))
    check_that("Product version reflected on displayed module page",
               utilities.get_text_by_css(driver, locators.PRODUCT_INFO_CSS), contains_string(constants.product_version))
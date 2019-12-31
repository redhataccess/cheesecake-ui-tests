import sys
import lemoncheesecake.api as lcc
from lemoncheesecake.matching import *
from helpers import utilities
from helpers import constants
from helpers import locators
sys.path.append("..")

SUITE = {
    "description": "Create a new product",
    "rank": "6"
}

product_name = constants.new_product_name + utilities.generate_random_string(4)


@lcc.test('Verify that Warning is displayed when no product name is being entered')
def create_product_blank_name(driver):
    utilities.click_element_by_link_text(driver, locators.MENU_PRODUCTS_LINK_TEXT)
    utilities.click_element_by_link_text(driver, locators.MENU_NEW_PRODUCT_LINK_TEXT)
    utilities.enter_text_by_id(driver, locators.PRODUCT_NAME_TEXTBOX_ID, "")
    utilities.click_element_by_class_name(driver, locators.SAVE_PRODUCT_BUTTON_CLASS_NAME)
    check_that("Warning is displayed", utilities.get_text_by_css(driver, locators.WARNING_ALERT_CSS),
               contains_string(constants.blank_product_name_warning))
    utilities.click_element_by_css_selector(driver, locators.CLOSE_WARNING_ALERT_CSS)


@lcc.test("Verify that the product is created successfully and listed in the Products list")
def create_product(driver):
    utilities.click_element_by_link_text(driver, locators.MENU_NEW_PRODUCT_LINK_TEXT)

    lcc.log_info("Product name input: %s " % product_name)
    utilities.enter_text_by_id(driver, locators.PRODUCT_NAME_TEXTBOX_ID, product_name)
    utilities.enter_text_by_id(driver, locators.PRODUCT_DESCRIPTION_TEXTBOX_ID, constants.new_product_description)
    utilities.click_element_by_class_name(driver, locators.SAVE_PRODUCT_BUTTON_CLASS_NAME)
    products = utilities.find_elements_by_id(driver, locators.PRODUCT_NAMES_LI_ID)
    products_list = []
    for product in products:
        products_list.append(product.text)
    check_that("Product created is listed successfully", products_list, has_item(product_name), quiet=False)


@lcc.test("Verify that user is unable to create duplicate product names, Warning is displayed")
def duplicate_product_name(driver):
    utilities.click_element_by_link_text(driver, locators.MENU_NEW_PRODUCT_LINK_TEXT)
    lcc.log_info("Product name input: %s " % product_name)
    utilities.enter_text_by_id(driver, locators.PRODUCT_NAME_TEXTBOX_ID, product_name)
    utilities.enter_text_by_id(driver, locators.PRODUCT_DESCRIPTION_TEXTBOX_ID, constants.new_product_description)
    utilities.click_element_by_class_name(driver, locators.SAVE_PRODUCT_BUTTON_CLASS_NAME)
    check_that("Duplicate Product warning is displayed", utilities.get_text_by_css(driver, locators.WARNING_ALERT_CSS),
               contains_string(constants.duplicate_product_name_warning))
    utilities.click_element_by_css_selector(driver, locators.CLOSE_WARNING_ALERT_CSS)

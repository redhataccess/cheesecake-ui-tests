import sys
import lemoncheesecake.api as lcc
from lemoncheesecake.matching import *
from helpers import utilities
from helpers import constants
from helpers import locators
import helpers.base as base
import time
import requests
sys.path.append("..")

SUITE = {
    "description": "Create a new product and versions",
    "rank": "2"
}

product_name = constants.new_product_name + utilities.generate_random_string(4)
url = base.config_reader('qa', 'base_url')
username = base.config_reader('login', 'username')
auth = base.config_reader('login', 'password')


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
    lcc.log_info(str(len(products)))
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


@lcc.test("Verify that user is able to create versions of the above product")
def create_product_versions(driver):
    utilities.click_element_by_link_text(driver, locators.MENU_PRODUCT_LISTING_LINK_TEXT)
    # User clicks on 'Product details' button for the product created above.
    lcc.log_info("Product name to add versions for: %s " % product_name)
    time.sleep(10)
    products = utilities.find_elements_by_class_name(driver, locators.PRODUCT_NAMES_LIST_CLASS_NAME)
    lcc.log_info("Number of products found in the list %s" % str(len(products)))
    for product in products:
        if product_name in product.text:
            lcc.log_info("Adding versions to %s" % product.text)
            product.find_element_by_class_name("pf-c-options-menu").click()
            lcc.log_info("Clicking on the dropdown to add product details")
            product.find_element_by_class_name(locators.PRODUCT_DETAILS_BUTTON_CLASS_NAME).click()
            break

    # User adds versions to the 'Add Product versions' and verifies if the versions were added successfully.
    driver.find_element_by_id(locators.NEW_PRODUCT_VERSION_TEXTBOX_ID).send_keys(constants.product_version_1)
    driver.find_element_by_xpath(locators.PRODUCT_VERSION_SAVE_BUTTON_XPATH).click()
    driver.find_element_by_id(locators.NEW_PRODUCT_VERSION_TEXTBOX_ID).clear()
    time.sleep(5)
    driver.find_element_by_id(locators.NEW_PRODUCT_VERSION_TEXTBOX_ID).send_keys(constants.product_version_2)
    driver.find_element_by_xpath(locators.PRODUCT_VERSION_SAVE_BUTTON_XPATH).click()
    driver.find_element_by_id(locators.NEW_PRODUCT_VERSION_TEXTBOX_ID).clear()
    time.sleep(5)
    driver.find_element_by_id(locators.NEW_PRODUCT_VERSION_TEXTBOX_ID).send_keys(constants.product_version_3)
    driver.find_element_by_xpath(locators.PRODUCT_VERSION_SAVE_BUTTON_XPATH).click()
    driver.find_element_by_id(locators.NEW_PRODUCT_VERSION_TEXTBOX_ID).clear()
    time.sleep(10)
    versions_ul = driver.find_element_by_class_name(locators.PRODUCT_VERSIONS_UL_CLASS_NAME)
    versions_list = versions_ul.find_elements_by_tag_name(locators.PRODUCT_VERSIONS_LI_TAG_NAME)
    versions = []
    for version in versions_list:
        versions.append(version.text)
    lcc.log_info("Versions added: %s" % str(versions))
    check_that("Product version entered is added successfully ", versions, has_item(constants.product_version_1))
    check_that("Product version entered is added successfully ", versions, has_item(constants.product_version_2))
    check_that("Product version entered is added successfully ", versions, has_item(constants.product_version_3))


def teardown_suite():
    lcc.log_info("Deleting the product created above...")
    product_name_node = product_name.replace(" ", "_").lower()
    path_to_product_node = url + "content/products/" + product_name_node
    lcc.log_info("Test Product node being deleted at: %s" % path_to_product_node)
    body = {":operation": "delete"}
    response = requests.post(path_to_product_node, data=body, auth=(username, auth))
    check_that("The Product created was deleted successfully",
               response.status_code, equal_to(200))

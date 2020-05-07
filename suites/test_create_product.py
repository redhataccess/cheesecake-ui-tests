import sys
import lemoncheesecake.api as lcc
from lemoncheesecake.matching import *
from helpers import utilities
from helpers import constants
from helpers import locators
from helpers.base_screenshot import Screenshot
import time
import requests
from fixtures import fixture
from selenium.webdriver.common.by import By
sys.path.append("..")

# SUITE = {
#     "description": "Create a new product and versions",
#     "rank": "2"
# }

product_name = constants.new_product_name + utilities.generate_random_string(4)
url = fixture.url
username = fixture.username
auth = fixture.auth


@lcc.suite("Suite: Create a new product and versions", rank="2")
class test_create_product(Screenshot):
    driver = lcc.inject_fixture("driver_obj")

    @lcc.test('Verify that Warning is displayed when no product name is being entered')
    def create_product_blank_name(self):
        utilities.click_element(self.driver, By.LINK_TEXT, locators.MENU_PRODUCTS_LINK_TEXT)
        utilities.click_element(self.driver, By.LINK_TEXT, locators.MENU_NEW_PRODUCT_LINK_TEXT)
        utilities.enter_text(self.driver, By.ID, locators.PRODUCT_NAME_TEXTBOX_ID, "")
        utilities.click_element(self.driver, By.CLASS_NAME, locators.SAVE_PRODUCT_BUTTON_CLASS_NAME)
        check_that("Warning is displayed", utilities.get_text(self.driver, By.CSS_SELECTOR, locators.WARNING_ALERT_CSS),
                   contains_string(constants.blank_product_name_warning))
        utilities.click_element(self.driver, By.CSS_SELECTOR, locators.CLOSE_WARNING_ALERT_CSS)

    @lcc.test("Verify that the product is created successfully and listed in the Products list")
    def create_product(self):
        utilities.click_element(self.driver, By.LINK_TEXT, locators.MENU_NEW_PRODUCT_LINK_TEXT)

        lcc.log_info("Product name input: %s " % product_name)
        utilities.enter_text(self.driver, By.ID, locators.PRODUCT_NAME_TEXTBOX_ID, product_name)
        utilities.enter_text(self.driver, By.ID, locators.PRODUCT_DESCRIPTION_TEXTBOX_ID, constants.new_product_description)
        utilities.click_element(self.driver, By.CLASS_NAME, locators.SAVE_PRODUCT_BUTTON_CLASS_NAME)
        products = utilities.find_elements_by_id(self.driver, locators.PRODUCT_NAMES_LI_ID)
        lcc.log_info(str(len(products)))
        products_list = []
        for product in products:
            products_list.append(product.text)
        check_that("Product created is listed successfully", products_list, has_item(product_name), quiet=False)

    @lcc.test("Verify that user is unable to create duplicate product names, Warning is displayed")
    def duplicate_product_name(self):
        utilities.click_element(self.driver, By.LINK_TEXT, locators.MENU_NEW_PRODUCT_LINK_TEXT)
        lcc.log_info("Product name input: %s " % product_name)
        utilities.enter_text(self.driver, By.ID, locators.PRODUCT_NAME_TEXTBOX_ID, product_name)
        utilities.enter_text(self.driver, By.ID, locators.PRODUCT_DESCRIPTION_TEXTBOX_ID, constants.new_product_description)
        utilities.click_element(self.driver, By.CLASS_NAME, locators.SAVE_PRODUCT_BUTTON_CLASS_NAME)
        check_that("Duplicate Product warning is displayed",
                   utilities.get_text(self.driver, By.CSS_SELECTOR, locators.WARNING_ALERT_CSS),
                   contains_string(constants.duplicate_product_name_warning))
        utilities.click_element(self.driver, By.CSS_SELECTOR, locators.CLOSE_WARNING_ALERT_CSS)

    @lcc.test("Verify that user is able to create versions of the above product")
    def create_product_versions(self):
        utilities.click_element(self.driver, By.LINK_TEXT, locators.MENU_PRODUCT_LISTING_LINK_TEXT)
        # User clicks on 'Product details' button for the product created above.
        lcc.log_info("Product name to add versions for: %s " % product_name)
        utilities.wait(10)
        products = utilities.find_elements_by_class_name(self.driver, locators.PRODUCT_NAMES_LIST_CLASS_NAME)
        lcc.log_info("Number of products found in the list %s" % str(len(products)))
        for product in products:
            if product_name in product.text:
                lcc.log_info("Adding versions to %s" % product.text)
                product.find_element_by_class_name("pf-c-options-menu").click()
                lcc.log_info("Clicking on the dropdown to add product details")
                product.find_element_by_class_name(locators.PRODUCT_DETAILS_BUTTON_CLASS_NAME).click()
                break

        # User adds versions to the 'Add Product versions' and verifies if the versions were added successfully.
        utilities.enter_text(self.driver, By.ID, locators.NEW_PRODUCT_VERSION_TEXTBOX_ID, constants.product_version_1)
        utilities.click_element(self.driver, By.XPATH, locators.PRODUCT_VERSION_SAVE_BUTTON_XPATH)
        utilities.find_element(self.driver, By.ID, locators.NEW_PRODUCT_VERSION_TEXTBOX_ID).clear()
        utilities.wait(5)
        utilities.enter_text(self.driver, By.ID, locators.NEW_PRODUCT_VERSION_TEXTBOX_ID, constants.product_version_2)
        utilities.click_element(self.driver, By.XPATH, locators.PRODUCT_VERSION_SAVE_BUTTON_XPATH)
        utilities.find_element(self.driver, By.ID,locators.NEW_PRODUCT_VERSION_TEXTBOX_ID).clear()
        utilities.wait(5)
        utilities.enter_text(self.driver, By.ID, locators.NEW_PRODUCT_VERSION_TEXTBOX_ID, constants.product_version_3)
        utilities.click_element(self.driver, By.XPATH, locators.PRODUCT_VERSION_SAVE_BUTTON_XPATH)
        utilities.find_element(self.driver, By.ID, locators.NEW_PRODUCT_VERSION_TEXTBOX_ID).clear()
        utilities.wait(10)
        versions_ul = utilities.find_element(self.driver, By.CLASS_NAME, locators.PRODUCT_VERSIONS_UL_CLASS_NAME)
        versions_list = versions_ul.find_elements_by_tag_name(locators.PRODUCT_VERSIONS_LI_TAG_NAME)
        versions = []
        for version in versions_list:
            versions.append(version.text)
        lcc.log_info("Versions added: %s" % str(versions))
        check_that("Product version entered is added successfully ", versions, has_item(constants.product_version_1))
        check_that("Product version entered is added successfully ", versions, has_item(constants.product_version_2))
        check_that("Product version entered is added successfully ", versions, has_item(constants.product_version_3))

    def teardown_suite(self):
        lcc.log_info("Deleting the product created above...")
        product_name_node = product_name.replace(" ", "_").lower()
        path_to_product_node = url + "content/products/" + product_name_node
        lcc.log_info("Test Product node being deleted at: %s" % path_to_product_node)
        body = {":operation": "delete"}
        response = requests.post(path_to_product_node, data=body, auth=(fixture.admin_username, fixture.admin_auth))
        check_that("The Product created was deleted successfully",
                   response.status_code, equal_to(200))

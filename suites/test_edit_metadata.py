import sys
import lemoncheesecake.api as lcc
from lemoncheesecake.matching import *
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException, NoSuchElementException
from pages import search_page
from pages import display_module_page
from pages import search_beta_page
from helpers import utilities
from helpers import constants
from helpers import locators
from helpers.base_screenshot import Screenshot
from selenium.webdriver.common.by import By
from fixtures import fixture
sys.path.append("..")

# SUITE = {
#     "description": "Edit metadata for a module",
#     "rank": "3"
# }

# Test flow for the suite:
# 1. With all the fields on edit metadata modal blank click on submit
# 2. Populate all the fields on edit metadata modal except url fragment and click on submit
# 3. Populate all the fields on edit metadata modal except product name and click on submit
# 4. Populate all the fields on edit metadata modal except product version and click on submit
# 5. Populate all the fields on edit metadata modal except usecase and click on submit
# 6. Populate all the fields on edit metadata with valid data and click on submit


@lcc.suite("Suite: Edit metadata for a module", rank="4")
class test_edit_metadata(Screenshot):
    driver = lcc.inject_fixture("driver_obj")

    @lcc.test("Verify that warning should be displayed on Edit Metadata modal when no data is entered")
    def edit_metadata_blank_data(self):
        utilities.click_element(self.driver, By.LINK_TEXT, "Search")
        # # Click on the title if it is displayed on the first page
        utilities.wait(5)
        # search_page.search_for_module_and_click(self.driver, constants.module_to_be_published)
        search_beta_page.select_repo(self.driver, fixture.repo_name)
        search_beta_page.search_module_and_click(self.driver, constants.module_to_be_published)
        self.driver.refresh()
        utilities.click_element(self.driver, By.XPATH, locators.ADD_METADATA_BUTTON_XPATH)
        check_that("Edit metadata modal title",
                   utilities.get_text(self.driver, By.CSS_SELECTOR, locators.EDIT_METADATA_MODAL_TITLE_CSS),
                   contains_string(constants.edit_metadata_modal_title))
        utilities.click_element(self.driver, By.CSS_SELECTOR, locators.EDIT_METADATA_SAVE_CSS)
        check_that("Warning displayed", utilities.get_text(self.driver, By.CSS_SELECTOR, locators.WARNING_ALERT_CSS),
                   contains_string(constants.edit_metadata_modal_warning))
        utilities.wait(2)

    @lcc.test("Verify that warning should be displayed on Edit Metadata modal when Product name field is blank")
    def edit_metadata_empty_productname(self):
        display_module_page.reset_edit_metadata_from(self.driver)
        display_module_page.fill_edit_metadata_form(self.driver, constants.default_product_name,
                                                    constants.default_product_version, constants.use_case,
                                                    constants.url_fragment)
        check_that("Warning displayed", utilities.get_text(self.driver, By.CSS_SELECTOR, locators.WARNING_ALERT_CSS),
                   contains_string(constants.edit_metadata_modal_warning))
        utilities.wait(2)

    @lcc.test("Verify that warning should be displayed on Edit Metadata modal when Product version field is blank")
    def edit_metadata_empty_version(self):
        display_module_page.reset_edit_metadata_from(self.driver)
        display_module_page.fill_edit_metadata_form(self.driver, constants.product_name, constants.default_product_version,
                                                    constants.use_case, constants.url_fragment)
        check_that("Warning displayed", utilities.get_text(self.driver, By.CSS_SELECTOR, locators.WARNING_ALERT_CSS),
                   contains_string(constants.edit_metadata_modal_warning))
        utilities.wait(2)

    @lcc.test("Verify that warning should be displayed on Edit Metadata modal when Usecase field is blank")
    def edit_metadata_empty_usecase(self):
        display_module_page.reset_edit_metadata_from(self.driver)
        display_module_page.fill_edit_metadata_form(self.driver, constants.product_name, constants.product_version,
                                                    constants.default_use_case, constants.url_fragment)
        check_that("Warning displayed", utilities.get_text(self.driver, By.CSS_SELECTOR, locators.WARNING_ALERT_CSS),
                   contains_string(constants.edit_metadata_modal_warning))
        utilities.wait(2)

    @lcc.test("Verify that user should be able to add product metadata successfully")
    def edit_metadata_successfully(self):
        display_module_page.reset_edit_metadata_from(self.driver)
        display_module_page.fill_edit_metadata_form(self.driver, constants.product_name, constants.product_version,
                                                    constants.use_case, constants.url_fragment)
        check_that("Success message displayed",
                   utilities.get_text(self.driver, By.CSS_SELECTOR, locators.UPDATE_SUCCESS_MESSAGE_CSS),
                   contains_string(constants.success_message))
        check_that("Product name reflected on displayed module page",
                   utilities.get_text(self.driver, By.CSS_SELECTOR, locators.PRODUCT_INFO_CSS),
                   contains_string(constants.product_name))
        check_that("Product version reflected on displayed module page",
                   utilities.get_text(self.driver, By.CSS_SELECTOR, locators.PRODUCT_INFO_CSS),
                   contains_string(constants.product_version))

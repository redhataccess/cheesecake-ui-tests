import sys
import lemoncheesecake.api as lcc
from lemoncheesecake.matching import *
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from pages import search_page
from pages import display_module_page
from helpers import utilities
from helpers import constants
from helpers import locators
from helpers.base_screenshot import Screenshot
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

@lcc.suite("Suite: Edit metadata for a module", rank="3")
class test_edit_metadata(Screenshot):
    driver = lcc.inject_fixture("driver_obj")

    @lcc.test("Verify that warning should be displayed on Edit Metadata modal when no data is entered")
    def edit_metadata_blank_data(self):
        utilities.click_element_by_link_text(self.driver, "Search")
        # Click on the title if it is displayed on the first page
        utilities.wait(5)
        try:
            utilities.click_element_by_link_text(
                self.driver, constants.module_to_be_published)
        # If the title is not found on the first page, search for the title and then click
        except (TimeoutException, StaleElementReferenceException) as e:
            lcc.log_info("An exception occurred while looking for the module, searching for the module now...")
            search_page.search_for_module_and_click(self.driver, constants.module_to_be_published)
        utilities.click_element_by_css_selector(self.driver, locators.EDIT_METADATA_DROPDOWN_CSS)
        utilities.click_element_by_css_selector(self.driver, locators.EDIT_METADATA_BUTTON_CSS)
        check_that("Edit metadata modal title", utilities.get_text_by_css(self.driver, locators.EDIT_METADATA_MODAL_TITLE_CSS),
                   contains_string(constants.edit_metadata_modal_title))
        utilities.click_element_by_css_selector(self.driver, locators.EDIT_METADATA_SAVE_CSS)
        check_that("Warning displayed", utilities.get_text_by_css(self.driver, locators.WARNING_ALERT_CSS),
                   contains_string(constants.edit_metadata_modal_warning))
        utilities.wait(2)

    @lcc.test("Verify that warning should be displayed on Edit Metadata modal when URL fragment field is blank")
    def edit_metadata_empty_url_fragment(self):
        display_module_page.reset_edit_metadata_from(self.driver)
        display_module_page.fill_edit_metadata_form(self.driver, constants.product_name, constants.product_version,
                                                    constants.use_case, "")
        check_that("Warning displayed", utilities.get_text_by_css(self.driver, locators.WARNING_ALERT_CSS),
                   contains_string(constants.edit_metadata_modal_warning))
        utilities.wait(2)

    @lcc.test("Verify that warning should be displayed on Edit Metadata modal when Product name field is blank")
    def edit_metadata_empty_productname(self):
        display_module_page.reset_edit_metadata_from(self.driver)
        display_module_page.fill_edit_metadata_form(self.driver, constants.default_product_name,
                                                    constants.default_product_version, constants.use_case,
                                                    constants.url_fragment)
        check_that("Warning displayed", utilities.get_text_by_css(self.driver, locators.WARNING_ALERT_CSS),
                   contains_string(constants.edit_metadata_modal_warning))
        utilities.wait(2)

    @lcc.test("Verify that warning should be displayed on Edit Metadata modal when Product version field is blank")
    def edit_metadata_empty_version(self):
        display_module_page.reset_edit_metadata_from(self.driver)
        display_module_page.fill_edit_metadata_form(self.driver, constants.product_name, constants.default_product_version,
                                                    constants.use_case, constants.url_fragment)
        check_that("Warning displayed", utilities.get_text_by_css(self.driver, locators.WARNING_ALERT_CSS),
                   contains_string(constants.edit_metadata_modal_warning))
        utilities.wait(2)

    @lcc.test("Verify that warning should be displayed on Edit Metadata modal when Usecase field is blank")
    def edit_metadata_empty_usecase(self):
        display_module_page.reset_edit_metadata_from(self.driver)
        display_module_page.fill_edit_metadata_form(self.driver, constants.product_name, constants.product_version,
                                                    constants.default_use_case, constants.url_fragment)
        check_that("Warning displayed", utilities.get_text_by_css(self.driver, locators.WARNING_ALERT_CSS),
                   contains_string(constants.edit_metadata_modal_warning))
        utilities.wait(2)

    @lcc.test("Verify that user should be able to add product metadata successfully")
    def edit_metadata_successfully(self):
        display_module_page.reset_edit_metadata_from(self.driver)
        display_module_page.fill_edit_metadata_form(self.driver, constants.product_name, constants.product_version,
                                                    constants.use_case, constants.url_fragment)
        check_that("Success message displayed",
                   utilities.get_text_by_css(self.driver, locators.UPDATE_SUCCESS_MESSAGE_CSS),
                   contains_string(constants.success_message))
        check_that("Product name reflected on displayed module page", utilities.get_text_by_css(self.driver, locators.PRODUCT_INFO_CSS),
                   contains_string(constants.product_name))
        check_that("Product version reflected on displayed module page",
                   utilities.get_text_by_css(self.driver, locators.PRODUCT_INFO_CSS), contains_string(constants.product_version))

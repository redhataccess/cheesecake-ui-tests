import sys
from helpers.base_screenshot import Screenshot
import requests
import lemoncheesecake.api as lcc
from lemoncheesecake.matching import *
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from pages import search_page
from pages import display_module_page
from helpers import utilities
from helpers import constants
from helpers import locators
from fixtures import fixture
sys.path.append("..")

# SUITE = {
#     "description": "Verify module type test",
#     "rank": "7"
# }

#   Carryout the following tests:
#      - Filter modules by the module type and verify all the modules with the expected module type are listed
#      - Verify module type saved in the backend is correct using the api endpoint
#      - Verify module type shown on the module display page is as expected
#      - Verify module type persists after publishing the module
#      - Verify that file containing invalid module type, the module type data does not get added

url = fixture.url


@lcc.suite("Suite: Module type test- Checks module type data for modules", rank="7")
class test_module_type(Screenshot):
    driver = lcc.inject_fixture("driver_obj")

    @lcc.test("Concept :: Verify filter by module type")
    def verify_filter_by_module_type_concept(self):
        lcc.log_info("================= Module type :: Concept =================")
        verify_filter_by_module_type(self.driver, "Concept")

    @lcc.test("Concept :: Verify module type form backend when module type is mentioned in filename")
    @lcc.depends_on("test_module_type.verify_filter_by_module_type_concept")
    def verify_module_type_from_backend_module_type_in_filename_con(self):
        lcc.log_info("Verifying module type for modules with type mentioned in the filename")
        # verify_module_type_data(self.driver, module_type, constants.con_module_title)
        open_module_display_page(self.driver, constants.con_module_title)
        verify_module_type_from_backend(self.driver, "Concept")

    @lcc.test("Concept :: Verify module type on UI when module type is mentioned in file name")
    @lcc.depends_on("test_module_type.verify_module_type_from_backend_module_type_in_filename_con")
    def verify_module_type_from_ui_module_type_in_filename_con(self):
        verify_module_type_from_UI(self.driver, "Concept")

    @lcc.test("Concept :: Verify module type after publishing when module type mentioned in filename")
    @lcc.depends_on("test_module_type.verify_module_type_from_backend_module_type_in_filename_con")
    def verify_module_type_after_publising_con(self):
        verify_module_type_after_publishing(self.driver, "Concept")


    @lcc.test("Concept :: Verify module type form backend when module type is mentioned inside adoc file")
    def verify_module_type_from_backend_module_type_inside_file_con(self):
        lcc.log_info("Verifying module type for modules with type mentioned inside the adoc file")
        utilities.click_element_by_link_text(self.driver, locators.MENU_SEARCH_PAGE_LINK_TEXT)
        search_page.filter_by_module_type(self.driver, "Concept")
        open_module_display_page(self.driver, constants.con_module_title1)
        verify_module_type_from_backend(self.driver, "Concept")

    @lcc.test("Procedure :: Verify filter by module type")
    def verify_filter_by_module_type_procedure(self):
        lcc.log_info("================= Module type :: Procedure =================")
        verify_filter_by_module_type(self.driver, "Procedure")

    @lcc.test("Procedure :: Verify module type form backend when module type is mentioned in filename")
    @lcc.depends_on("test_module_type.verify_filter_by_module_type_procedure")
    def verify_module_type_from_backend_module_type_in_filename_proc(self):
        lcc.log_info("Verifying module type for modules with type mentioned in the filename")
        # verify_module_type_data(self.driver, module_type, constants.con_module_title)
        open_module_display_page(self.driver, constants.proc_module_title)
        verify_module_type_from_backend(self.driver, "Procedure")

    @lcc.test("Procedure :: Verify module type on UI when module type is mentioned in file name")
    @lcc.depends_on("test_module_type.verify_module_type_from_backend_module_type_in_filename_proc")
    def verify_module_type_from_ui_module_type_in_filename_proc(self):
        verify_module_type_from_UI(self.driver, "Procedure")

    @lcc.test("Procedure :: Verify module type after publishing when module type mentioned in filename")
    @lcc.depends_on("test_module_type.verify_module_type_from_backend_module_type_in_filename_proc")
    def verify_module_type_after_publising_proc(self):
        verify_module_type_after_publishing(self.driver, "Procedure")

    @lcc.test("Procedure :: Verify module type form backend when module type is mentioned inside adoc file")
    def verify_module_type_from_backend_module_type_inside_file_proc(self):
        lcc.log_info("Verifying module type for modules with type mentioned inside the adoc file")
        utilities.click_element_by_link_text(self.driver, locators.MENU_SEARCH_PAGE_LINK_TEXT)
        search_page.filter_by_module_type(self.driver, "Procedure")
        open_module_display_page(self.driver, constants.proc_module_title1)
        verify_module_type_from_backend(self.driver, "Procedure")

    @lcc.test("Reference :: Verify filter by module type: Reference")
    def verify_filter_by_module_type_reference(self):
        lcc.log_info("================= Module type :: Reference =================")
        verify_filter_by_module_type(self.driver, "Reference")

    @lcc.test("Reference :: Verify module type form backend when module type is mentioned in filename")
    @lcc.depends_on("test_module_type.verify_filter_by_module_type_reference")
    def verify_module_type_from_backend_module_type_in_filename_ref(self):
        lcc.log_info("Verifying module type for modules with type mentioned in the filename")
        # verify_module_type_data(self.driver, module_type, constants.con_module_title)
        open_module_display_page(self.driver, constants.ref_module_title)
        verify_module_type_from_backend(self.driver, "Reference")

    @lcc.test("Reference :: Verify module type on UI when module type is mentioned in file name")
    @lcc.depends_on("test_module_type.verify_module_type_from_backend_module_type_in_filename_ref")
    def verify_module_type_from_ui_module_type_in_filename_ref(self):
        verify_module_type_from_UI(self.driver, "Reference")

    @lcc.test("Reference :: Verify module type after publishing when module type mentioned in filename")
    @lcc.depends_on("test_module_type.verify_module_type_from_backend_module_type_in_filename_ref")
    def verify_module_type_after_publising_ref(self):
        verify_module_type_after_publishing(self.driver, "Reference")

    @lcc.test("Reference :: Verify module type form backend when module type is mentioned inside adoc file")
    def verify_module_type_from_backend_module_type_inside_file_ref(self):
        lcc.log_info("Verifying module type for modules with type mentioned inside the adoc file")
        utilities.click_element_by_link_text(self.driver, locators.MENU_SEARCH_PAGE_LINK_TEXT)
        search_page.filter_by_module_type(self.driver, "Reference")
        open_module_display_page(self.driver, constants.ref_module_title1)
        verify_module_type_from_backend(self.driver, "Reference")

    @lcc.test("Verify module with invalid type defined")
    def verify_no_module_type(self):
        utilities.click_element_by_link_text(self.driver, locators.MENU_SEARCH_PAGE_LINK_TEXT)
        try:
            search_page.search_for_module_and_click(self.driver, constants.no_module_type_title)
        except (TimeoutException, StaleElementReferenceException) as e:
            lcc.log_error("Module not listed on listed in the results after applying module type filter.")
            utilities.wait(2)
            search_page.search_for_module_and_click(self.driver, constants.no_module_type_title)
        lcc.log_info("Verifying no module type is displayed for modules with invalid type mentioned inside the asciidoc file")
        # Once landed on the module display page, get path to adoc from the module display page url
        path_to_adoc_file = display_module_page.get_path_to_adoc(self.driver)
        path = path_to_adoc_file + constants.path_for_module_type
        response = requests.get(url + path)
        # module_type_from_backend = utilities.get_module_type_from_backend(url + path)
        check_that("Module type node in backend", response.status_code, equal_to(404))
        module_type_on_display_page = utilities.get_text_by_css(self.driver, locators.VIEW_MODULE_TYPE_CSS)
        check_that("Module type displayed on UI ", module_type_on_display_page.upper(), equal_to("-"))

# Helper methods for actual tests

# This method will click on given title to open the module display page for it
def open_module_display_page(driver, title):
    try:
        utilities.click_element_by_link_text(driver, title)
    # If the title is not found on the first page, search for the title and then click
    except (TimeoutException, StaleElementReferenceException) as e:
        lcc.log_error("Module not listed on listed in the results after applying module type filter.")
        lcc.log_info("Searching for the module title now...")
        search_page.search_for_module_and_click(driver, title)

# This method will verify the module type from the backend for the module user is currently landed on
def verify_module_type_from_backend(driver, module_type):
    # Once landed on the module display page, get path to adoc from the module display page url
    path_to_adoc_file = display_module_page.get_path_to_adoc(driver)
    path = path_to_adoc_file + constants.path_for_module_type
    response = requests.get(url + path)
    check_that("Module type saved in the backend", response.text.upper(),
               equal_to(module_type.upper()))

# This method will verify the module type shown for the module, user is currently landed on
def verify_module_type_from_UI(driver, module_type):
    module_type_on_display_page = utilities.get_text_by_css(driver, locators.VIEW_MODULE_TYPE_CSS)
    check_that("Module type displayed on UI ", module_type_on_display_page.upper(),
               equal_to(module_type.upper()))

# This method will verify if module type persists after publishing
def verify_module_type_after_publishing(driver, module_type):
    lcc.log_info("Verifying if module type persists after publishing")
    display_module_page.add_metadata_and_publish(driver)
    module_type_on_display_page_again = utilities.get_text_by_css(driver, locators.VIEW_MODULE_TYPE_CSS)
    lcc.log_warning("This is expected to fail until CCS-3552 is fixed!!!")
    check_that("Module type displayed on UI after publishing", module_type_on_display_page_again.upper(),
               equal_to(module_type.upper()))

# This method navigates to the search page, filters the modules by given module type
# and verifies that module type of all the modules listed after the filter is applied = given module type
def verify_filter_by_module_type(driver, module_type):
    utilities.click_element_by_link_text(driver, locators.MENU_SEARCH_PAGE_LINK_TEXT)
    lcc.log_info("Verifying filter by module type")
    search_page.filter_by_module_type(driver, module_type)
    module_type_list = search_page.get_all_module_types_on_page(driver)
    all_of(check_that("Module type", module_type.upper(), is_in(module_type_list)),
           check_that("All elements in the module type column are same", len(set(module_type_list))==1, is_true()))


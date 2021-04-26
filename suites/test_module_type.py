import sys
from helpers.base_screenshot import Screenshot
import requests
import lemoncheesecake.api as lcc
from lemoncheesecake.matching import *
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from pages import search_page, search_beta_page
from pages import display_module_page
from helpers import utilities
from helpers import constants
from helpers import locators
from fixtures import fixture
from selenium.webdriver.common.by import By
sys.path.append("..")

# SUITE = {
#     "description": "Verify module type test",
#     "rank": "7"
# }

#   Carryout the following tests:
#      - Filter modules by the module type and verify all the modules with the expected module type are listed
#      - Verify module type saved in the backend is correct using the api endpoint
#       Failing due to CCS-3734
#      - Verify module type shown on the module details page is as expected
#       Failing due to CCS-3552
#      - Verify module type persists after publishing the module
#      - Verify that file containing invalid module type, the module type data does not get added

url = fixture.url


@lcc.suite("Suite: Tests for Module type(CONCEPT, PROCEDURE, REFERENCE) by filter and filename", rank="8")
class test_module_type(Screenshot):
    driver = lcc.inject_fixture("driver_obj")

    @lcc.test("Verify that 'Filter by Module Type': CONCEPT functionality filters results correctly")
    def verify_filter_by_content_type_concept(self):
        verify_filter_by_content_type(self.driver, "Concept")

    @lcc.test("Verify module type: CONCEPT is shown correctly when added as filename 'con_file.adoc' verified using the api")
    @lcc.depends_on("test_module_type.verify_filter_by_content_type_concept")
    def verify_module_type_from_backend_module_type_in_filename_con(self):
        open_module_display_page(self.driver, constants.con_module_title)
        verify_module_type_from_backend(self.driver, "Concept")

    @lcc.test("Verify module type: CONCEPT appears as in on UI when module type is added as filename 'con_file.adoc'")
    @lcc.depends_on("test_module_type.verify_module_type_from_backend_module_type_in_filename_con")
    def verify_module_type_from_ui_module_type_in_filename_con(self):
        verify_module_type_from_UI(self.driver, "Concept")

    @lcc.test("Verify module type: CONCEPT does not disappear from the UI after the module is published.")
    @lcc.depends_on("test_module_type.verify_module_type_from_backend_module_type_in_filename_con")
    def verify_module_type_after_publising_con(self):
        verify_module_type_after_publishing(self.driver, "Concept")

    @lcc.test(
        "Verify module type: CONCEPT shows correctly when mentioned inside asccidoc file as ':pantheon-module-type: CONCEPT'")
    def verify_module_type_from_backend_module_type_inside_file_con(self):
        utilities.click_element(self.driver, By.LINK_TEXT, locators.MENU_SEARCH_PAGE_LINK_TEXT)
        search_beta_page.select_repo(self.driver, fixture.repo_name)
        search_beta_page.filter_by_content_type(self.driver, "Concept")
        # search_page.filter_by_module_type(self.driver, "Concept")
        open_module_display_page(self.driver, constants.con_module_title1)
        verify_module_type_from_backend(self.driver, "Concept")

    @lcc.test("Verify that 'Filter by Module Type': PROCEDURE functionality filters results correctly")
    def verify_filter_by_content_type_procedure(self):
        verify_filter_by_content_type(self.driver, "Procedure")

    @lcc.test(
        "Verify module type: PROCEDURE is shown correctly when added as filename 'proc_file.adoc' verified using the api")
    @lcc.depends_on("test_module_type.verify_filter_by_content_type_procedure")
    def verify_module_type_from_backend_module_type_in_filename_proc(self):
        open_module_display_page(self.driver, constants.proc_module_title)
        verify_module_type_from_backend(self.driver, "Procedure")

    @lcc.test(
        "Verify module type: PROCEDURE appears as in on UI when module type is added as filename 'proc_file.adoc'")
    @lcc.depends_on("test_module_type.verify_module_type_from_backend_module_type_in_filename_proc")
    def verify_module_type_from_ui_module_type_in_filename_proc(self):
        verify_module_type_from_UI(self.driver, "Procedure")

    @lcc.test("Verify module type: PROCEDURE does not disappear from the UI after the module is published.")
    @lcc.depends_on("test_module_type.verify_module_type_from_backend_module_type_in_filename_proc")
    def verify_module_type_after_publising_proc(self):
        verify_module_type_after_publishing(self.driver, "Procedure")

    @lcc.test(
        "Verify module type: PROCEDURE shows correctly when mentioned inside asccidoc file as ':pantheon-module-type: PROCEDURE'")
    def verify_module_type_from_backend_module_type_inside_file_proc(self):
        utilities.click_element(self.driver, By.LINK_TEXT, locators.MENU_SEARCH_PAGE_LINK_TEXT)
        # search_page.filter_by_module_type(self.driver, "Procedure")
        search_beta_page.select_repo(self.driver, fixture.repo_name)
        search_beta_page.filter_by_content_type(self.driver, "Procedure")
        open_module_display_page(self.driver, constants.proc_module_title1)
        verify_module_type_from_backend(self.driver, "Procedure")

    @lcc.test("Verify that 'Filter by Module Type': REFERENCE functionality filters results correctly")
    def verify_filter_by_content_type_reference(self):
        verify_filter_by_content_type(self.driver, "Reference")

    @lcc.test(
        "Verify module type: REFERENCE is shown correctly when added as filename 'ref_file.adoc' verified using the api")
    @lcc.depends_on("test_module_type.verify_filter_by_content_type_reference")
    def verify_module_type_from_backend_module_type_in_filename_ref(self):
        open_module_display_page(self.driver, constants.ref_module_title)
        verify_module_type_from_backend(self.driver, "Reference")

    @lcc.test("Verify module type: REFERENCE appears as in on UI when module type is added as filename 'ref_file.adoc'")
    @lcc.depends_on("test_module_type.verify_module_type_from_backend_module_type_in_filename_ref")
    def verify_module_type_from_ui_module_type_in_filename_ref(self):
        verify_module_type_from_UI(self.driver, "Reference")

    @lcc.test("Verify module type: REFERENCE does not disappear from the UI after the module is published.")
    @lcc.depends_on("test_module_type.verify_module_type_from_backend_module_type_in_filename_ref")
    def verify_module_type_after_publising_ref(self):
        verify_module_type_after_publishing(self.driver, "Reference")

    @lcc.test(
        "Verify module type: REFERENCE shows correctly when mentioned inside asccidoc file as ':pantheon-module-type: REFERENCE'")
    def verify_module_type_from_backend_module_type_inside_file_ref(self):
        utilities.click_element(self.driver, By.LINK_TEXT, locators.MENU_SEARCH_PAGE_LINK_TEXT)
        # search_page.filter_by_module_type(self.driver, "Reference")
        search_beta_page.select_repo(self.driver, fixture.repo_name)
        search_beta_page.filter_by_content_type(self.driver, "Reference")
        open_module_display_page(self.driver, constants.ref_module_title1)
        verify_module_type_from_backend(self.driver, "Reference")

    @lcc.test("Verify module with invalid type defined")
    def verify_no_module_type(self):
        utilities.click_element(self.driver, By.LINK_TEXT, locators.MENU_SEARCH_PAGE_LINK_TEXT)
        utilities.page_reload(self.driver)
        # try:
        #     search_page.search_for_module_and_click(self.driver, constants.no_module_type_title)
        # except (TimeoutException, StaleElementReferenceException) as e:
        #     lcc.log_error("Module not listed on listed in the results after applying module type filter.")
        #     utilities.wait(2)
        #     search_page.search_for_module_and_click(self.driver, constants.no_module_type_title)
        search_beta_page.select_repo(self.driver, fixture.repo_name)
        search_beta_page.search_module_and_click(self.driver, constants.no_module_type_title)
        lcc.log_info("Verifying no module type is displayed for modules with invalid type mentioned inside "
                     "the asciidoc file")
        # Once landed on the module display page, get path to adoc from the module display page url
        path_to_adoc_file = display_module_page.get_path_to_adoc(self.driver)
        path = path_to_adoc_file + constants.path_for_module_type
        response = requests.get(url=url + path, auth=(fixture.username, fixture.api_auth))
        check_that("Module type node in backend", response.status_code, equal_to(404))

# Helper methods for actual tests


# This method will click on given title to open the module display page for it
def open_module_display_page(driver, title):
    print("Inside open module display page")
    try:
        print("Title::"+title)
        utilities.click_element(driver, By.LINK_TEXT, title)
        utilities.wait(5)
    except Exception as e:
        print("In except...")
        # If the title is not found on the first page, search for the title and then click
        lcc.log_info(e)
        lcc.log_info("Module not listed on listed in the results after applying module type filter.")
        lcc.log_info("Searching for the module title now...")
        search_beta_page.search_module_and_click(driver, title)


# This method will verify the module type from the backend for the module user is currently landed on
def verify_module_type_from_backend(driver, module_type):
    # Once landed on the module display page, get path to adoc from the module display page url
    path_to_adoc_file = display_module_page.get_path_to_adoc(driver)
    path = path_to_adoc_file + constants.path_for_module_type
    req = url+path.strip()
    response = requests.get(url=req, auth=(fixture.username, fixture.api_auth))
    lcc.log_info("Verifying the response at endpoint: %s " % req)
    check_that("Module type saved in the backend", response.text.upper(),
               contains_string(module_type.upper()))


# This method will verify the module type shown for the module, user is currently landed on
def verify_module_type_from_UI(driver, module_type):
    module_type_on_display_page = utilities.get_text(driver, By.CSS_SELECTOR, locators.VIEW_MODULE_TYPE_CSS)
    lcc.log_info("Verifying that the module type is displayed on the UI as: %s " % module_type)
    check_that("Module type displayed on UI ", module_type_on_display_page.upper(),
               equal_to(module_type.upper()))


# This method will verify if module type persists after publishing
def verify_module_type_after_publishing(driver, module_type):
    lcc.log_info("Verifying if module type persists after publishing")
    display_module_page.add_metadata_and_publish(driver)
    module_type_on_display_page_again = utilities.get_text(driver, By.CSS_SELECTOR, locators.VIEW_MODULE_TYPE_CSS)
    check_that("Module type displayed on UI after publishing", module_type_on_display_page_again.upper(),
               equal_to(module_type.upper()))


# This method navigates to the search page, filters the modules by given module type
# and verifies that module type of all the modules listed after the filter is applied = given module type
def verify_filter_by_content_type(driver, module_type):
    utilities.click_element(driver, By.LINK_TEXT, locators.MENU_SEARCH_PAGE_LINK_TEXT)
    utilities.page_reload(driver)
    search_beta_page.select_repo(driver, fixture.repo_name)
    lcc.log_info("Verifying filter by module type: %s " % module_type)
    search_beta_page.filter_by_content_type(driver, module_type)
    module_type_title_list = utilities.find_elements_by_css_selector(driver, locators.ALL_MODULE_TITLES)
    module_type_list = []
    for i in module_type_title_list:
        module_type_list.append(i.text)
    for i in module_type_list:
        check_that("Module type for all titles", i, contains_string(module_type))
    utilities.wait(10)
    # all_of(check_that("Module type", module_type.upper(), is_in(module_type_list)),
    #        check_that("All elements in the module type column are same", len(set(module_type_list))==1, is_true()))


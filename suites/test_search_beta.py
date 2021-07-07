import sys
from selenium.webdriver.common.by import By
import lemoncheesecake.api as lcc
from lemoncheesecake.matching import *
from helpers import utilities, locators, constants
from helpers.base_screenshot import Screenshot
from pages import search_beta_page, display_module_page
from helpers import base
from suites.test_publish_module import unpublish_module


@lcc.suite("Suite: Tests for Search Beta", rank=11)
class test_search_beta(Screenshot):
    driver = lcc.inject_fixture("driver_obj")

    repo_name = base.config_reader('test_repo', 'repo_name')
    module_prefix = base.config_reader('test_repo', 'module_prefix')
    assembly_prefix = base.config_reader('test_repo', 'assembly_prefix')

    @lcc.test("Verify that main filter toggle, filter by Repository toggle view works as expected; "
              "warning error msg is displayed when no repo is selected ")
    def no_repo_selected(self):
        utilities.wait(2)
        utilities.click_element(self.driver, By.LINK_TEXT, locators.MENU_SEARCH_PAGE_LINK_TEXT)
        utilities.page_reload(self.driver)
        utilities.wait(1)
        # clicking on filter funnel icon twice to close and re-open the filter by repo pannel
        utilities.click_element(self.driver, By.ID, locators.TOGGLE_ID)
        utilities.wait(1)
        utilities.click_element(self.driver, By.ID, locators.TOGGLE_ID)
        utilities.wait(1)
        check_that("Filter by repo section is displayed", utilities.find_element(self.driver, By.CLASS_NAME,
                                        locators.FILTER_BY_REPO_SECTION_CLASS_NAME).is_displayed(),is_true())
        check_that("No results found warning message", utilities.get_text(self.driver, By.CSS_SELECTOR,
                                                                          locators.NO_MODULE_RESULTS_FOUND_CSS),
                   contains_string(constants.no_results_found))
        utilities.click_element(self.driver, By.XPATH, locators.FILTER_BY_REPO_TOGGLE_XPATH)
        utilities.wait(1)
        utilities.click_element(self.driver, By.XPATH, locators.FILTER_BY_REPO_TOGGLE_XPATH)
        utilities.wait(1)
        check_that("Repository list is displayed after expanding Filter by Repo",
                   utilities.find_element(self.driver, By.XPATH,
                                          locators.REPO_LIST_XPATH).is_displayed(), is_true())

    @lcc.test("Verify that user is able to see results when he uses Filter by Repository search bar")
    def search_for_repo(self):
        utilities.enter_text(self.driver, By.XPATH, locators.FILTER_BY_REPO_SEARCH_BAR_XPATH, self.repo_name)
        utilities.wait(1)
        repo_list = utilities.find_elements_by_css_selector(self.driver, locators.REPOSITORY_CHECKBOX_CSS)
        repo_list_count = len(repo_list)
        for i in range(repo_list_count):
            if repo_list[i].text == self.repo_name:
                check_that("Entered repo name is displayed on search results",
                           repo_list[i].text, equal_to(self.repo_name))
        utilities.click_element(self.driver, By.CLASS_NAME, locators.CANCEL_BUTTON_ON_REPO_SEARCH_BAR_CLASS_NAME)
        utilities.wait(1)

    @lcc.test("Verify user is able to select a repo; Module and Assemblies section has content displayed and toggles.")
    def select_repo_filter(self):
        search_beta_page.select_repo(self.driver, self.repo_name)
        utilities.wait(1)
        utilities.find_element(self.driver, By.CSS_SELECTOR, locators.REPOSITORY_CHECKBOX_CSS).is_selected()
        check_that("Repository name displayed correctly on right side panel", utilities.get_text(
            self.driver, By.XPATH, locators.REPOSITORY_NAME_XPATH), equal_to(self.repo_name))
        check_that("Modules section has data displayed for selected repo", utilities.find_element(
            self.driver, By.CSS_SELECTOR, locators.MODULES_CSS).is_displayed(), is_true())
        check_that("Assemblies section has data displayed for selected repo", utilities.find_element(
            self.driver, By.CSS_SELECTOR, locators.ASSEMBLY_CSS).is_displayed(), is_true())

        utilities.click_element(self.driver, By.XPATH, locators.MODULES_TOGGLE_BUTTON_XPATH)
        utilities.wait(1)
        check_that("Modules section is collapsible", utilities.find_element(
            self.driver, By.XPATH, locators.MODULE_ASSEMBLY_TOGGLE_XPATH).is_displayed(), is_true())
        utilities.click_element(self.driver, By.XPATH, locators.MODULES_TOGGLE_BUTTON_XPATH)
        utilities.wait(1)
        utilities.click_element(self.driver, By.XPATH, locators.ASSEMBLY_TOGGLE_BUTTON_XPATH)
        utilities.wait(1)
        check_that("Assemblies section is collapsible", utilities.find_element(
            self.driver, By.XPATH, locators.MODULE_ASSEMBLY_TOGGLE_XPATH).is_displayed(), is_true())
        utilities.wait(1)
        utilities.click_element(self.driver, By.XPATH, locators.ASSEMBLY_TOGGLE_BUTTON_XPATH)

    @lcc.test("Verify that modules and assemblies are listed for selected repo")
    def modules_assemblies_list(self):
        utilities.wait(1)
        module_title_list = utilities.find_elements_by_css_selector(self.driver, locators.MODULE_TITLES_CSS)
        modules_count = len(module_title_list)
        modules = modules_count - 1
        lcc.log_info("Modules displayed: %s " % str(modules))
        for i in range(1, modules_count):
            check_that("Modules listed for selected repo", module_title_list[i].text,
                       contains_string(self.module_prefix))
        assembly_title_list = utilities.find_elements_by_css_selector(self.driver, locators.ASSEMBLY_TITLES_CSS)
        assembly_count = len(assembly_title_list)
        assemblies = assembly_count - 1
        lcc.log_info("Assemblies displayed: %s" % str(assemblies))
        for i in range(1, assembly_count):
            check_that("Assemblies listed for selected repo", assembly_title_list[i].text,
                       contains_string(self.assembly_prefix))
        lcc.log_info("Find the Search beta page preview in the attachment below:")
        self.driver.save_screenshot("search_beta_repo_selected.png")
        lcc.save_attachment_file("search_beta_repo_selected.png")

    @lcc.test("Verify Status and Content Type filter on search page")
    def filters_on_search_page(self):
        utilities.click_element(self.driver, By.CLASS_NAME, locators.STATUS_FILTER_CLASS_NAME)
        utilities.click_element(self.driver, By.CLASS_NAME, locators.DRAFT_STATUS_CLASS_NAME)
        check_that("Draft Status filter chip is displayed on search page",
                   utilities.find_element(self.driver, By.CLASS_NAME,
                                          locators.STATUS_TOOLBAR_CHIP_CLASS_NAME).is_displayed(), is_true())
        last_published_date_list = utilities.find_elements_by_XPATH(self.driver, locators.LAST_PUBLISHED_DATE_XPATH)
        published_date_list = []
        for i in last_published_date_list:
            published_date_list.append(i.text)
        for i in published_date_list:
            check_that("Published date for all titles should be '-' when draft status filter is selected", i,
                       contains_string("-"))
        utilities.click_element(self.driver, By.CSS_SELECTOR, locators.CLEAR_ALL_FILTER_CSS)
        utilities.wait(1)
        search_beta_page.search_module_and_click(self.driver, constants.publish_module)
        utilities.wait(1)
        display_module_page.add_metadata_and_publish(self.driver)
        utilities.wait(2)
        utilities.click_element(self.driver, By.LINK_TEXT, "Search")
        search_beta_page.select_repo(self.driver, self.repo_name)
        utilities.wait(2)
        utilities.click_element(self.driver, By.CLASS_NAME, locators.STATUS_FILTER_CLASS_NAME)
        utilities.click_element(self.driver, By.CLASS_NAME, locators.PUBLISHED_STATUS_CLASS_NAME)
        utilities.wait(2)
        check_that("Published module is filtered", utilities.get_text(self.driver, By.CSS_SELECTOR,
                                                                      locators.FIRST_MODULE_LISTED_CSS), contains_string(constants.publish_module))
        check_that("Green check is displayed for published module", utilities.find_element(self.driver, By.CLASS_NAME,
                                                        locators.GREEN_CHECK_CLASS_NAME).is_displayed(), is_true())
        utilities.wait(3)
        utilities.click_element(self.driver, By.CSS_SELECTOR, locators.CLEAR_ALL_FILTER_CSS)
        utilities.wait(1)
        utilities.click_element(self.driver, By.CLASS_NAME, locators.CONTENT_TYPE_CLASS_NAME)
        utilities.click_element(self.driver, By.CLASS_NAME, locators.CONCEPT_CONTENT_TYPE_FILTER_CLASS_NAME)
        check_that("Content Type filter chip is displayed on search page",
                   utilities.find_element(self.driver, By.CLASS_NAME,
                                          locators.STATUS_TOOLBAR_CHIP_CLASS_NAME).is_displayed(), is_true())
        utilities.wait(3)
        check_that("'Concept' content type filter is selected", utilities.get_text(self.driver, By.CSS_SELECTOR,
                                                                                   locators.FIRST_MODULE_LISTED_CSS), contains_string("Concept"))
        utilities.wait(1)
        utilities.click_element(self.driver, By.CLASS_NAME, locators.CONCEPT_CONTENT_TYPE_FILTER_CLASS_NAME)
        utilities.click_element(self.driver, By.CLASS_NAME, locators.PROCEDURE_CONTENT_TYPE_FILTER_CLASS_NAME)
        utilities.wait(3)
        check_that("'Procedure' content type filter is selected", utilities.get_text(self.driver, By.CSS_SELECTOR,
                                                                                     locators.FIRST_MODULE_LISTED_CSS), contains_string("Procedure"))
        utilities.wait(1)
        utilities.click_element(self.driver, By.CLASS_NAME, locators.PROCEDURE_CONTENT_TYPE_FILTER_CLASS_NAME)
        utilities.click_element(self.driver, By.CLASS_NAME, locators.REFERENCE_CONTENT_TYPE_FILTER_CLASS_NAME)
        utilities.wait(3)
        check_that("'Reference' content type filter is selected", utilities.get_text(self.driver, By.CSS_SELECTOR,
                                                                                     locators.FIRST_MODULE_LISTED_CSS), contains_string("Reference"))
        utilities.wait(2)

    def teardown_suite(self):
        response = unpublish_module(self, constants.search_module_unpublish, constants.variant)
        check_that("Unpublish request status code", response.status_code, equal_to(200))
        lcc.log_info("module published for above test is unpublished successfully..")
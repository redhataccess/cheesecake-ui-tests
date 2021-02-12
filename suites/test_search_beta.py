import sys
from selenium.webdriver.common.by import By
import lemoncheesecake.api as lcc
from lemoncheesecake.matching import *
from helpers import utilities, locators, constants
from helpers.base_screenshot import Screenshot
from pages import search_beta_page
from helpers import base


@lcc.suite("Suite: Tests for Search Beta", rank="10")
class test_search_beta(Screenshot):
    driver = lcc.inject_fixture("driver_obj")

    repo_name = base.config_reader('test_repo', 'repo_name')
    module_prefix = base.config_reader('test_repo', 'module_prefix')
    assembly_prefix = base.config_reader('test_repo', 'assembly_prefix')

    @lcc.test("Verify that main filter toggle, filter by Repository toggle view works as expected; "
              "warning error msg is displayed when no repo is selected ")
    def no_repo_selected(self):
        utilities.wait(2)
        utilities.click_element(self.driver, By.XPATH, locators.MENU_SEARCH_BETA_XPATH)
        utilities.wait(1)
        # clicking on filter funnel icon twice to close and re-open the filter by repo pannel
        utilities.click_element(self.driver, By.ID, locators.TOGGLE_ID)
        utilities.wait(1)
        utilities.click_element(self.driver, By.ID, locators.TOGGLE_ID)
        utilities.wait(1)
        check_that("Filter by repo section is displayed", utilities.find_element(self.driver, By.CLASS_NAME,
                          locators.FILTER_BY_REPO_SECTION_CLASS_NAME).is_displayed(), is_true())
        check_that("No results found warning message", utilities.get_text(self.driver, By.CSS_SELECTOR,
                                                                          locators.NO_RESULTS_FOUND_CSS),
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
            if repo_list[i].text == self.repo_name :
                check_that("Entered repo name is displayed on search results",
                           repo_list[i].text, equal_to(self.repo_name))
        utilities.click_element(self.driver, By.CLASS_NAME, locators.CANCEL_BUTTON_ON_REPO_SEARCH_BAR_CLASS_NAME)
        utilities.wait(1)

    @lcc.test("Verify user is able to select a repo; Module and Assemblies section has content displayed and toggles.")
    def select_repo_filter(self):
        search_beta_page.search_and_select_repo(self.driver, self.repo_name)
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

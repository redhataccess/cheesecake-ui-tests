import sys
import subprocess
import os
import lemoncheesecake.api as lcc
from lemoncheesecake.matching import *
from helpers import utilities
from helpers import constants
from helpers import locators
from helpers.base_screenshot import Screenshot
from polling2 import poll
from pages import search_beta_page, display_module_page
from fixtures import fixture
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from helpers import locators
import requests
sys.path.append("..")

url = fixture.url
username = fixture.username
auth = fixture.api_auth


@lcc.suite("Suite: Verify xref validation works as expected", rank=10)
class test_xref_validation(Screenshot):
    driver = lcc.inject_fixture("driver_obj")
    xref_target = []

    @lcc.test('Verify xref validation for module')
    def xref_validations_module(self):
        utilities.click_element(self.driver, By.LINK_TEXT, locators.MENU_SEARCH_PAGE_LINK_TEXT)
        # utilities.page_reload(self.driver)
        search_beta_page.select_repo(self.driver, fixture.repo_name)
        search_beta_page.search_titles(self.driver, constants.partial_title)
        # Verify the number of xref validation icons displayed after filtering search results
        result_count = len(utilities.find_elements_by_XPATH(self.driver, locators.XREF_VALIDATION_ICON_XPATH))
        check_that("Expected titles show the xref validation icon on search page", result_count,
                   greater_than_or_equal_to(3))
        # Number of modules returned in the search results
        modules_list = utilities.find_elements_by_css_selector(self.driver, locators.MODULE_SEARCH_RESULTS_CSS)
        j=1
        # Iterate throught the list of modules returned
        while j<=len(modules_list):
            print("================",j,"====================")
            utilities.click_element(self.driver, By.CSS_SELECTOR, locators.NTH_MODULE_LISTED_CSS.format(j))
            utilities.wait(10)
            # Verify check validation tree is displayed on UI
            check_that("Xref validation tree is displayed on document details page",
                       utilities.find_element(self.driver, By.ID, locators.XREF_VALIDATION_TREE_ID).is_displayed(),
                       is_true())
            validation_count = int(utilities.get_text(self.driver, By.CSS_SELECTOR, locators.XREF_VALIDATION_COUNT_CSS))
            print(validation_count)
            adoc_path = display_module_page.get_path_to_adoc(self.driver)
            req = fixture.url + adoc_path + '.10.json'
            print(req)
            # Get data from validation node in the JCR tree
            response = requests.get(url=req, auth=(username, auth))
            validation_xref = response.json()['en_US']['variants'][constants.variant]['draft']['validations']['xref']
            print(validation_xref)
            # xref node contains validation nodes along with created, createdBy and primaryType fields.
            # Hence, subracting 3 from the count
            count = len(validation_xref)-3
            print(count)
            check_that("Count of validation nodes on UI and API matches", validation_count, equal_to(count))
            # Separate the filename and the path wrt to repo name
            path_in_repo, file = os.path.split(adoc_path.split("/entities/")[1])
            print(path_in_repo)
            cwd = os.getcwd()
            print("cwd::", cwd)
            # If user is not inside the repo directory the navigate to the repo directory
            if not (cwd.endswith(path_in_repo)):
                path = "../" + path_in_repo
                os.chdir(path)
                cwd = os.getcwd()
                print("cwd::", cwd)
            print("File-", file)
            # Read contents of the adoc file
            content = utilities.read_file(file)
            print(content)
            i=1
            while (i<=count):
                # For each xref validation node for every module check all the fields within the node
                check_that("Validation message", validation_xref[str(i)]['pant:message'],
                           equal_to(constants.xref_validation_msg))
                check_that("Validation type", validation_xref[str(i)]['pant:validationType'], equal_to("xref"))
                check_that("Xref target", validation_xref[str(i)]['pant:xrefTarget'], is_not_none())
                check_that("Validation status", validation_xref[str(i)]["pant:status"], equal_to("error"))
                target_path = validation_xref[str(i)]['pant:xrefTarget']
                print("target path::", target_path)
                self.xref_target.append(target_path)
                # Verify that the xref validation target actually is a part of the file adoc content
                check_that("File content", content, contains_string(target_path))
                i=i+1
            # Navigate back to search page and filter out the xref validation titles from the repo to perform tests
            # on the next module in list
            utilities.click_element(self.driver, By.LINK_TEXT, locators.MENU_SEARCH_PAGE_LINK_TEXT)
            utilities.page_reload(self.driver)
            search_beta_page.select_repo(self.driver, fixture.repo_name)
            search_beta_page.search_titles(self.driver, constants.partial_title)
            j=j+1

    @lcc.test('Verify xref validation for assembly')
    def xref_validation_assembly(self):
        # Go to search page, select the repo and filter out the titles
        utilities.click_element(self.driver, By.LINK_TEXT, locators.MENU_SEARCH_PAGE_LINK_TEXT)
        utilities.page_reload(self.driver)
        search_beta_page.select_repo(self.driver, fixture.repo_name)
        search_beta_page.search_titles(self.driver, constants.partial_title)
        # Verify that expected number of xref validation icons are displayed
        check_that("Expected titles show the xref validation icon on search page",
                   len(utilities.find_elements_by_XPATH(self.driver, locators.XREF_VALIDATION_ICON_XPATH)),
                   greater_than_or_equal_to(3))
        utilities.click_element(self.driver, By.CSS_SELECTOR, locators.FIRST_LISTED_ASSEMBLY_CSS)
        utilities.wait(10)
        # Verify that xref validation is displayed on the UI
        check_that("Xref validation tree is displayed on document details page",
                   utilities.find_element(self.driver, By.ID, locators.XREF_VALIDATION_TREE_ID).is_displayed(),
                   is_true())
        # Get the number of xref validation displayed on the UI
        validation_count = int(utilities.get_text(self.driver, By.CSS_SELECTOR, locators.XREF_VALIDATION_COUNT_CSS))
        print(validation_count)
        adoc_path = display_module_page.get_path_to_adoc(self.driver)
        req = fixture.url + adoc_path + '.10.json'
        print(req)
        response = requests.get(url=req, auth=(username, auth))
        print(response.json())
        # Get xref validation data from the JCR tree
        validation_xref = response.json()['en_US']['variants'][constants.variant]['draft']['validations']['xref']
        print(validation_xref)
        # xref node contains validation nodes along with created, createdBy and primaryType fields.
        # Hence, subracting 3 from the count
        count = len(validation_xref)-3
        print(count)
        # Verify count of xref validation nodes on UI and JCR tree matches
        check_that("Count of validation nodes on UI and API matches", validation_count, equal_to(count))
        # Separate the filename and the path wrt to repo name
        path_in_repo, file = os.path.split(adoc_path.split("/entities/")[1])
        print(path_in_repo)
        cwd = os.getcwd()
        print("cwd::", cwd)
        # Get path of the file wrt current working directory
        relative_path = cwd.split("test-repo/")
        print(relative_path)
        # # If user is not already inside the repo dir
        # if not (cwd.endswith(path_in_repo)):
        #     paths = [relative_path[1], path_in_repo]
        #     common = os.path.commonpath(paths)
        #     # Get a common directory between path wrt cwd and absolute path
        #     print("common::", common)
        #     k=0
        #     # Get count of directories we need to navigate back from to reach the common directory
        #     print("/ count::", relative_path[1].count("/"))
        #     # Navigate back 'count' number of times to go to the common directory
        #     while k<relative_path[1].count("/")+1:
        #         os.chdir("..")
        #         cwd = os.getcwd()
        #         print("cwd::", cwd)
        #         k = k + 1
        # Now from the common directory navigate the the direcory containing the file
        os.chdir(path_in_repo)
        cwd = os.getcwd()
        print("cwd::", cwd)
        print("File::", file)
        # Get adoc file content
        content = utilities.read_file(file)
        print(content)
        i=1
        while (i<=count):
            # For each xref validation node for every assembly check all the fields within the node
            check_that("Validation message", validation_xref[str(i)]['pant:message'], equal_to(constants.xref_validation_msg))
            check_that("Validation type", validation_xref[str(i)]['pant:validationType'], equal_to("xref"))
            check_that("Xref target", validation_xref[str(i)]['pant:xrefTarget'], is_not_none())
            check_that("Validation status", validation_xref[str(i)]["pant:status"], equal_to("error"))
            target_path = validation_xref[str(i)]['pant:xrefTarget']
            print("target path::", target_path)
            # self.xref_target.append(target_path)
            print(self.xref_target)
            # In the xref target is not already a part of the included modules only then check if the target is persent
            # in the assembly adoc file
            if not (target_path in self.xref_target):
                check_that("File content", content, contains_string(target_path))
            i = i + 1

    @lcc.test('Verify xref validation for module in Customer Portal')
    def xref_validations_module_in_CP(self):
        utilities.click_element(self.driver, By.LINK_TEXT, locators.MENU_SEARCH_PAGE_LINK_TEXT)
        utilities.page_reload(self.driver)
        search_beta_page.select_repo(self.driver, fixture.repo_name)
        search_beta_page.search_module_and_click(self.driver, constants.xref_validation_module_name)
        utilities.wait(4)
        display_module_page.add_metadata_and_publish(self.driver)
        display_module_page.navigate_into_CP(self.driver)

        Xref_linkText1 = "Xref to assembly with complete path"
        Xref_linkText2 = "xref to file on same level"
        Xref_linkText3 = "Different module included in different assembly"

        CP_title_static_part = " | Red Hat Customer Portal"

        utilities.click_element(self.driver, By.LINK_TEXT, Xref_linkText1)
        utilities.switch_to_latest_tab(self.driver)
        check_that("Xref to assembly with complete path", utilities.get_page_title(self.driver),
                   "at-uploader | Assembly Publish test" + CP_title_static_part)
        utilities.switch_to_first_tab(self.driver)

        utilities.click_element(self.driver, By.LINK_TEXT, Xref_linkText2)
        utilities.switch_to_latest_tab(self.driver)
        check_that("xref to file on same level", utilities.get_page_title(self.driver),
                   "Content Test Module | Logging in to the web console using Kerberos authentication (Image present)" + CP_title_static_part)
        utilities.switch_to_first_tab(self.driver)

        utilities.click_element(self.driver, By.LINK_TEXT, Xref_linkText3)
        utilities.switch_to_latest_tab(self.driver)
        check_that("Different module included in different assembly", utilities.get_page_title(self.driver),
                   "at-uploader | Module type none" + CP_title_static_part)
        utilities.switch_to_first_tab(self.driver)

    def teardown_test(self, test, status):
        lcc.log_info("Moving back to screenshots dir")
        cwd = os.getcwd()
        print("cwd::", cwd)
        c = cwd.split("test-repo")[1].count("/")
        print("Move %s directories back" % c)
        k=0
        while (k<c):
            os.chdir("..")
            cwd = os.getcwd()
            print("cwd::", cwd)
            k = k + 1
        cwd = os.getcwd()
        print("cwd::", cwd)
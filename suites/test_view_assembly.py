import sys
import re
from helpers.base_screenshot import Screenshot
import lemoncheesecake.api as lcc
from lemoncheesecake.matching import *
from selenium.common.exceptions import TimeoutException
from pages import search_beta_page
from pages import display_module_page
from helpers import utilities
from helpers import constants
from helpers import locators
from fixtures import fixture
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By

from suites.test_publish_module import unpublish_module

sys.path.append("..")
from urllib.parse import urlparse
import subprocess
import logging
from helpers import base

url = fixture.url


@lcc.suite("Suite: Add metadata to assembly, publish assembly and view assembly content", rank=9)
class test_view_assembly(Screenshot):
    driver = lcc.inject_fixture("driver_obj")
    modules_count = 0
    module_titles = []

    @lcc.test("Verify that user can add metadata to assembly")
    def add_metadata(self):
        utilities.wait(5)
        utilities.click_element(self.driver, By.LINK_TEXT, "Search")
        utilities.page_reload(self.driver)
        # search_page.search_for_module_and_click(self.driver, constants.assembly_to_be_published)
        search_beta_page.select_repo(self.driver, fixture.repo_name)
        search_beta_page.search_module_and_click(self.driver, constants.assembly_to_be_published)
        utilities.click_element(self.driver, By.XPATH, locators.ADD_METADATA_BUTTON_XPATH)
        check_that("Edit metadata modal title",
                   utilities.get_text(self.driver, By.CSS_SELECTOR, locators.EDIT_METADATA_MODAL_TITLE_CSS),
                   contains_string(constants.edit_metadata_modal_title))
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
        utilities.wait(2)

    @lcc.test("Verify that user is able to publish assembly successfully")
    def publish_assembly(self):
        utilities.wait(5)
        utilities.click_element(self.driver, By.ID, locators.MODULE_DISPLAY_PUBLISH_BUTTON_ID)
        check_that("Button", utilities.get_text(
            self.driver, By.CSS_SELECTOR, locators.MODULE_DISPLAY_PREVIEW_BUTTON_CSS), contains_string("Preview"))
        check_that("Button", utilities.get_text(
            self.driver, By.ID, locators.MODULE_DISPLAY_UNPUBLISH_BUTTON_ID), contains_string("Unpublish"))
        # Add a check that the Published column contains some Published time.

    @lcc.test("Verify contents of assembly preview in pantheon")
    # 1. Verify assembly title is displayed as expected
    # 2. Verify product name is displayed as expected
    # 3. Verify product version is displayed as expected
    # 4. Verify image path is resolved and contains expected value
    # 5. Verify all included modules are displayed in assembly preview

    def preview_assembly(self):
        test_repo_name = base.config_reader('test_repo', 'repo_name')
        try:
            # Get list of modules included
            modules_included = utilities.find_elements_by_css_selector(self.driver, locators.MODULES_INCLUDED_LIST_CSS)
            test_view_assembly.modules_count = len(modules_included)
            for i in range(test_view_assembly.modules_count):
                test_view_assembly.module_titles.append(modules_included[i].text)
            utilities.click_element(self.driver, By.CSS_SELECTOR, locators.MODULE_DISPLAY_PREVIEW_BUTTON_CSS)
            utilities.wait(5)
            utilities.switch_to_latest_tab(self.driver)
            utilities.wait(7)
            assembly_title = utilities.find_shadow_dom_element(self.driver,locators.DOCUMENT_TITLE,
                                                               locators.MODULE_BODY_CONTENT_CSS).text
            print(assembly_title)
            check_that("Assembly title", constants.assembly_to_be_published, contains_string(assembly_title))
            product_name = utilities.find_shadow_dom_element(self.driver, locators.PRODUCT_NAME_ON_PREVIEW_CSS,
                                                             locators.MODULE_BODY_CONTENT_CSS).text
            print(product_name)
            check_that("Product name reflected on view page", product_name, contains_string(constants.product_name))
            product_version = utilities.find_shadow_dom_element(self.driver, locators.PRODUCT_VERSION_ON_PREVIEW_CSS,
                                                                locators.MODULE_BODY_CONTENT_CSS).text
            print(product_version)
            check_that("Product version reflected on view page", product_version,
                       contains_string(constants.product_version))
            image = utilities.find_shadow_dom_element(self.driver,locators.IMAGE_CSS,locators.MODULE_BODY_CONTENT_CSS)
            src = image.get_attribute("src")
            imageasset = urlparse(src)
            imageasset = imageasset.path.split("/")[2]
            cmd = "echo " + imageasset + "|base64 -d"
            try:
                # subprocess.check_call(cmd, shell=True)
                path = subprocess.getoutput(cmd)
                print("Image file path::", path)
                image_file = "/content/repositories/" + test_repo_name + "/entities/enterprise/assemblies/images/" + constants.image_file_name
                check_that("Path to image1", path, equal_to(image_file))
            except subprocess.CalledProcessError as e:
                lcc.log_info("Unable to decode imageasset")

            assembly_body = utilities.get_text(self.driver, By.CSS_SELECTOR, locators.ASSEMBLY_BODY_PREVIEW_CSS)
            for i in range(test_view_assembly.modules_count):
                check_that("Assembly body", assembly_body, contains_string(test_view_assembly.module_titles[i]))

        except Exception as e:
            lcc.log_error(e)

        finally:
            if (len(self.driver.window_handles) > 1):
                self.driver.close()
                utilities.switch_to_first_tab(self.driver)

    @lcc.test("Verify contents of assembly on CP")
    def view_assembly_on_cp(self):
        test_repo_name = base.config_reader('test_repo', 'repo_name')
        try:
            utilities.page_reload(self.driver)
            utilities.click_element(self.driver, By.CSS_SELECTOR, locators.VIEW_ON_PORTAL_LINK_CSS)
            utilities.wait(5)
            utilities.switch_to_latest_tab(self.driver)
            utilities.wait(7)
            check_that("URL portal is", self.driver.current_url, contains_string(
                "https://access.qa.redhat.com/documentation/en-us/" + constants.product_name_uri + "/" + constants.product_version + "/guide/"))

            assembly_title = utilities.find_shadow_dom_element(self.driver, locators.DOCUMENT_TITLE_CP,
                                                               locators.MODULE_BODY_ON_PORTAL_CSS).text
            check_that("Assembly title", assembly_title, contains_string(constants.assembly_to_be_published))
            product_name = utilities.find_shadow_dom_element(self.driver, locators.PRODUCT_NAME_ON_PREVIEW_CSS,
                                                             locators.MODULE_BODY_ON_PORTAL_CSS).text
            check_that("Product name reflected on view page", product_name, contains_string(constants.product_name))
            product_version = utilities.find_shadow_dom_element(self.driver, locators.PRODUCT_VERSION_ON_PREVIEW_CSS,
                                                                locators.MODULE_BODY_ON_PORTAL_CSS).text
            check_that("Product version reflected on view page", product_version,
                       contains_string(constants.product_version))
            image = utilities.find_shadow_dom_element(self.driver, locators.IMAGE_CSS, locators.MODULE_BODY_ON_PORTAL_CSS)
            src = image.get_attribute("src")
            imageasset = urlparse(src)
            imageasset = imageasset.path.split("/")[2]
            cmd = "echo " + imageasset + "|base64 -d"
            try:
                # subprocess.check_call(cmd, shell=True)
                path = subprocess.getoutput(cmd)
                print("Image file path::", path)
                image_file = "/content/repositories/" + test_repo_name + "/entities/enterprise/assemblies/images/" + constants.image_file_name
                check_that("Path to image1", path, equal_to(image_file))
            except subprocess.CalledProcessError as e:
                lcc.log_info("Unable to decode imageasset")

            assembly_body = utilities.get_text(self.driver, By.CSS_SELECTOR, locators.ASSEMBLY_BODY_PREVIEW_CSS)
            for i in range(test_view_assembly.modules_count):
                check_that("Assembly body", assembly_body, contains_string(test_view_assembly.module_titles[i]))

            guides_content_related = utilities.find_shadow_dom_element(self.driver,
                                                                       locators.CONTENT_RELATED_TO_GUIDES,
                                                                       locators.MODULE_BODY_ON_PORTAL_CSS)
            self.driver.execute_script("arguments[0].scrollIntoView();", guides_content_related)
            utilities.wait(20)
            check_that("Content related to this guide setcion", guides_content_related.is_displayed(), equal_to(True))
            # utilities.click_element(self.driver, By.XPATH, "//summary[text()='Content related to this guide']")
            additional_res_guide = utilities.find_shadow_dom_element(self.driver,
                                                                     locators.CONTENT_RELATED_GUIDES_RESOURCES,
                                                                     locators.MODULE_BODY_ON_PORTAL_CSS)
            check_that("Content related to this guide setcion to contain Addtional resources setion", additional_res_guide.is_displayed(), equal_to(True))

        except Exception as e:
            lcc.log_error(e)

        finally:
            if (len(self.driver.window_handles) > 1):
                self.driver.close()
                utilities.switch_to_first_tab(self.driver)

    def teardown_suite(self):
        response = unpublish_module(self,constants.assembly_to_unpublish, constants.variant)
        check_that("Unpublish request status code", response.status_code, equal_to(200))
        lcc.log_info("Assembly published for above test is unpublished successfully..")




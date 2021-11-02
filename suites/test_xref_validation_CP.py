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
class test_xref_validation_CP(Screenshot):
    driver = lcc.inject_fixture("driver_obj")
    xref_target = []

    @lcc.test('Verify xref validation for module')
    def xref_validations_module(self):
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
        check_that("Xref to assembly with complete path", utilities.get_page_title(self.driver), "at-uploader | Assembly Publish test" + CP_title_static_part)
        utilities.switch_to_first_tab(self.driver)

        utilities.click_element(self.driver, By.LINK_TEXT,Xref_linkText2)
        utilities.switch_to_latest_tab(self.driver)
        check_that("Xref to assembly with complete path", utilities.get_page_title(self.driver), "Content Test Module | Logging in to the web console using Kerberos authentication (Image present)"+CP_title_static_part)
        utilities.switch_to_first_tab(self.driver)

        utilities.click_element(self.driver, By.LINK_TEXT, Xref_linkText3)
        utilities.switch_to_latest_tab(self.driver)
        check_that("Xref to assembly with complete path", utilities.get_page_title(self.driver), "at-uploader | Module type none" + CP_title_static_part)
        utilities.switch_to_first_tab(self.driver)

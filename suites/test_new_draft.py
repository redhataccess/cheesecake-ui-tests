import sys
import pytz
import lemoncheesecake.api as lcc
from lemoncheesecake.matching import *
from helpers.base_screenshot import Screenshot
from fixtures import fixture
from helpers import utilities, constants, locators
from pages import search_beta_page, display_module_page
from selenium.webdriver.common.by import By
from datetime import datetime,timezone, timedelta

from suites.test_publish_module import unpublish_module

sys.path.append("..")
import os
import subprocess
from git import Repo


url = fixture.url
username = fixture.username
auth = fixture.auth
api_auth = fixture.api_auth
uploader_username = fixture.uploader_username
uploader_password = fixture.uploader_password


@lcc.suite("Suite: Upload new draft version", rank=11)
class test_new_draft(Screenshot):
    driver = lcc.inject_fixture("driver_obj")
    now = datetime.now(timezone.utc)
    print("Now::",now)
    now_plus_15 = now + timedelta(minutes=15)
    now_minus_15 = now - timedelta(minutes=15)
    print("Range::", now_minus_15, "--", now_plus_15)
    flag = False

    def check_date_in_range(self, date):
        flag = False
        if (self.now_minus_15 <= date <= self.now_plus_15):
            flag = True
            print("date-time::", date)
        return flag

    def setup_suite(self):
        utilities.wait(5)
        # Navigate to search page
        # Select repo and search for the assembly
        # Add metadata and publish the assembly using api endpoints and wait for the unpublish button to display
        utilities.click_element(self.driver, By.LINK_TEXT, "Search")
        utilities.page_reload(self.driver)
        # search_page.search_for_module_and_click(self.driver, constants.published_module)
        search_beta_page.select_repo(self.driver, fixture.repo_name)
        search_beta_page.search_module_and_click(self.driver, constants.assembly_new_draft_version)
        display_module_page.add_metadata_and_publish(self.driver)
        utilities.wait_for_element(self.driver, By.ID, locators.MODULE_DISPLAY_UNPUBLISH_BUTTON_ID)
        # Navigate to search page
        # Select repo and search for the module
        # Add metadata and publish the module using api endpoints and wait for the unpublish button to display
        utilities.click_element(self.driver, By.LINK_TEXT, "Search")
        # search_page.search_for_module_and_click(self.driver, constants.published_module)
        search_beta_page.select_repo(self.driver, fixture.repo_name)
        search_beta_page.search_module_and_click(self.driver, constants.module_new_draft_version)
        display_module_page.add_metadata_and_publish(self.driver)
        utilities.wait_for_element(self.driver, By.ID, locators.MODULE_DISPLAY_UNPUBLISH_BUTTON_ID)


    @lcc.test("Upload the repo via uploader script 2nd time")
    def upload_repo_again(self):
        lcc.log_info("Uploaded the repo again")
        os.chdir(fixture.project_dir_git)
        repo = Repo(fixture.project_dir_git)
        git = repo.git
        git.checkout("at-uploader2")
        subprocess.check_call(
                ('pantheon --user={} --password={} --server={} push'.format(uploader_username, uploader_password,
                                                                            url)), shell=True)
        # search_page.search_for_module_and_click(self.driver, constants.published_module)
        search_beta_page.select_repo(self.driver, fixture.repo_name)
        search_beta_page.search_module_and_click(self.driver, constants.assembly_new_draft_version+" 2")
        check_that("Draft card is displayed",
                   utilities.find_element(self.driver, By.CSS_SELECTOR, locators.DRAFT_CARD).is_displayed(), is_true())
        check_that("Published card is displayed",
                   utilities.find_element(self.driver, By.CSS_SELECTOR, locators.PUBLISHED_CARD).is_displayed(), is_true())

        # Modify the datetime string to be in same format as datetime.now()
        draft_date1 = (utilities.find_element(self.driver, By.CSS_SELECTOR, locators.UPLOAD_TIME_ON_DRAFT_CARD).text)
        draft_date2 = draft_date1.split("GMT")
        pub_date1 = (utilities.find_element(self.driver, By.CSS_SELECTOR, locators.UPLOAD_TIME_ON_PUBLISHED_CARD).text)
        pub_date2 = pub_date1.split("GMT")
        print("Date time now::", self.now)
        draft_date = datetime.strptime(draft_date2[0].strip(), '%a %b %d %Y %H:%M:%S')
        draft_date = draft_date.replace(tzinfo=pytz.utc)
        pub_date = datetime.strptime(pub_date2[0].strip(), '%a %b %d %Y %H:%M:%S')
        pub_date = pub_date.replace(tzinfo=pytz.utc)
        print("Type of date is now::",draft_date)
        lcc.log_info("pub_date::%s" % pub_date)
        lcc.log_info("draft_date::%s" % draft_date)

        check_that("Draft text displayed on card",
                   utilities.get_text(self.driver, By.CSS_SELECTOR, locators.DRAFT_CARD_TITLE), equal_to("Draft"))
        check_that("Published text displayed on card",
                   utilities.get_text(self.driver, By.CSS_SELECTOR, locators.PUBLISHED_CARD_TITLE), equal_to("Published"))
        check_that("Draft upload date in expected range", self.check_date_in_range(draft_date), is_true())
        check_that("Uploaded date for published card in expected range", self.check_date_in_range(pub_date), is_true())
        check_that("Uploaded date for published card should be less than draft uploaded date", pub_date < draft_date,
                   is_true())
        draft_card = utilities.find_element(self.driver, By.CSS_SELECTOR, locators.DRAFT_CARD)
        published_card = utilities.find_element(self.driver, By.CSS_SELECTOR, locators.PUBLISHED_CARD)
        check_that("Add metadata link present of draft card",
                   draft_card.find_element(By.XPATH, locators.ADD_METADATA_BUTTON_XPATH).is_displayed(), is_true())
        check_that("Add metadata link present of published card",
                   published_card.find_element(By.XPATH, locators.ADD_METADATA_BUTTON_XPATH).is_displayed(), is_true())
        check_that("Preview link present of draft card",
                   draft_card.find_element(By.CSS_SELECTOR, locators.MODULE_DISPLAY_PREVIEW_BUTTON_CSS).is_displayed(),
                   is_true())
        check_that("Preview link present of published card",
                   published_card.find_element(By.CSS_SELECTOR,
                                               locators.MODULE_DISPLAY_PREVIEW_BUTTON_CSS).is_displayed(), is_true())
        check_that("Publish button displayed on draft card",
                   draft_card.find_element(By.ID, locators.MODULE_DISPLAY_PUBLISH_BUTTON_ID).is_displayed(), is_true())
        check_that("Unpublish button displayed on published card",
                   published_card.find_element(By.ID, locators.MODULE_DISPLAY_UNPUBLISH_BUTTON_ID).is_displayed(), is_true())
        check_that("Attributes file path on draft card",
                   draft_card.find_element(By.CSS_SELECTOR, locators.ATTRIBUTE_FILE_CSS).text,
                   equal_to("enterprise/meta/attributes.adoc"))
        check_that("Attributes file path on published card",
                   published_card.find_element(By.CSS_SELECTOR, locators.ATTRIBUTE_FILE_CSS).text,
                   equal_to("enterprise/meta/attributes.adoc"))

    def teardown_suite(self):
        response = unpublish_module(self,constants.module_new_draft_unpublish, constants.variant)
        check_that("Unpublish request status code for module", response.status_code, equal_to(200))

        response = unpublish_module(self, constants.assembly_new_draft_unpublish, constants.variant)
        check_that("Unpublish request status code for assembly", response.status_code, equal_to(200))



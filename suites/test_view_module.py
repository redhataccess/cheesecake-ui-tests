import sys
import re
import subprocess
from urllib.parse import urlparse
from helpers.base_screenshot import Screenshot
import lemoncheesecake.api as lcc
from lemoncheesecake.matching import *
from selenium.common.exceptions import TimeoutException
from pages import search_page, display_module_page
from helpers import utilities, locators, constants, base
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
sys.path.append("..")
from fixtures import fixture

# SUITE = {
#     "description": "View module test",
#     "rank": "5"
# }

url = fixture.url


@lcc.suite("Suite: Module view page checks for unpublished modules and already published.", rank="6")
class test_view_module(Screenshot):
    driver = lcc.inject_fixture("driver_obj")

    def setup_suite(self):
        # Add metadata
        utilities.wait(5)
        utilities.click_element(self.driver, By.LINK_TEXT, "Search")
        search_page.search_for_module_and_click(self.driver, constants.published_module)
        utilities.click_element(self.driver, By.XPATH, locators.ADD_METADATA_BUTTON_XPATH)
        display_module_page.fill_edit_metadata_form(self.driver, constants.product_name, constants.product_version,
                                                    constants.use_case, constants.url_fragment)
        # Publish module using api
        utilities.wait(5)
        utilities.click_element(self.driver, By.ID, locators.MODULE_DISPLAY_PUBLISH_BUTTON_ID)
        utilities.wait_for_element(self.driver, By.ID, locators.MODULE_DISPLAY_UNPUBLISH_BUTTON_ID)

    @lcc.test("Verify that for authenticated user, unpublished module displays all expected checks: Preview, ability to"
              " Publish, and status")
    # @lcc.depends_on('test_publish_module.publish_module')
    def authenticated_user_view_unpublished_module(self):
        utilities.click_element(self.driver, By.LINK_TEXT, "Search")
        # # Click on the title if it is displayed on the first page
        # try:
        #     utilities.click_element(self.driver, By.LINK_TEXT, constants.unpublished_module)
        # # If the title is not found on the first page, search for the title and then click
        # except TimeoutException as e:
        search_page.search_for_module_and_click(self.driver, constants.unpublished_module)
        check_that("URL", self.driver.current_url, contains_string(url+constants.module_display_page_path_unpublished))
        check_that("Button",
                   utilities.get_text(self.driver, By.ID, locators.MODULE_DISPLAY_PUBLISH_BUTTON_ID),
                   contains_string("Publish"))
        check_that("Button",
                   utilities.get_text(self.driver, By.CSS_SELECTOR, locators.MODULE_DISPLAY_PREVIEW_BUTTON_CSS),
                   contains_string("Preview"))
        check_that("Publish status",
                   utilities.get_text(self.driver, By.CSS_SELECTOR, locators.MODULE_DISPLAY_PUBLISH_STATUS_CSS),
                   contains_string("--"))
        check_that("Module display page title",
                   utilities.get_text(self.driver, By.CSS_SELECTOR, locators.MODULE_DISPLAY_TITLE_CSS),
                   contains_string(constants.unpublished_module))

    @lcc.test("Verify that for authenticated user, a previously published module displays all expected checks: "
              "Unpublish and View buttons")
    # @lcc.depends_on('test_publish_module.publish_module')
    def authenticated_user_view_published_module(self):
        utilities.click_element(self.driver, By.LINK_TEXT, "Search")
        # # Click on the title if it is displayed on the first page
        # try:
        #     utilities.click_element(self.driver, By.LINK_TEXT, constants.module_to_be_published)
        # # If the title is not found on the first page, search for the title and then click
        # except TimeoutException as e:
        search_page.search_for_module_and_click(
            self.driver, constants.published_module)
        # utilities.find_element(self.driver, By.ID, locators.MODULE_DISPLAY_PUBLISH_BUTTON_ID)
        check_that("URL", self.driver.current_url,
                   contains_string(url + constants.module_display_page_path_published))
        check_that("Button", utilities.get_text(
            self.driver, By.CSS_SELECTOR, locators.MODULE_DISPLAY_PREVIEW_BUTTON_CSS), contains_string("Preview"))
        check_that("Button", utilities.get_text(
            self.driver, By.ID, locators.MODULE_DISPLAY_UNPUBLISH_BUTTON_ID), contains_string("Unpublish"))
        # Add a check that the Published column contains some Published time.

    @lcc.test("Verify that 'View on Customer Portal' link navigates to correct page and verify the presence of content")
    # @lcc.depends_on('test_publish_module.publish_module')
    def view_on_portal_link_test(self):
        try:
            utilities.wait(5)
            utilities.click_element(
                self.driver, By.CSS_SELECTOR, locators.VIEW_ON_PORTAL_LINK_CSS)
            utilities.wait(5)
            utilities.switch_to_latest_tab(self.driver)
            utilities.wait(7)
            lcc.log_info("Find the CP preview in the attachment below for debugging purposes")
            self.driver.save_screenshot("cp_preview_module.png")
            lcc.save_attachment_file("cp_preview_module.png")
            check_that("View on Portal URL path", self.driver.current_url,
                       contains_string(constants.view_on_portal_page_url))
            module_id_regex = re.compile(
                r'^[a-zA-Z0-9]{8}-[a-zA-Z0-9]{4}-[a-zA-Z0-9]{4}-[a-zA-Z0-9]{4}-[a-zA-Z0-9]{12}$')
            current__module_id = self.driver.current_url.split("/topic/")[1]
            check_that("View on Portal URL id",
                   current__module_id, match_pattern(module_id_regex))
            # content_body_on_portal = utilities.find_element(self.driver, By.CSS_SELECTOR, locators.MODULE_BODY_ON_PORTAL_CSS)
        except (TimeoutException, StaleElementReferenceException, NoSuchElementException) as e:
            lcc.log_error("Error finding element!!!")
            lcc.log_error(e)
        finally:
            self.driver.close()
            utilities.switch_to_first_tab(self.driver)

    @lcc.test("Verify that module content displays as expected on CP")
    def view_content_on_cp(self):
        # # try:
        # test_repo_name = base.config_reader('test_repo', 'repo_name')
        utilities.click_element(self.driver, By.LINK_TEXT, "Search")
        utilities.wait(5)
        search_page.search_for_module_and_click(self.driver, constants.published_module)
        utilities.wait(5)
        try:
            utilities.click_element(self.driver, By.CSS_SELECTOR, locators.VIEW_ON_PORTAL_LINK_CSS)
            utilities.switch_to_latest_tab(self.driver)
            utilities.wait(6)
            content_body_on_portal = self.driver.find_element_by_css_selector(locators.MODULE_BODY_CSS)
            # Verify content displayed on CP
            check_that("Module content displayed on the Customer Portal", content_body_on_portal.is_displayed(),
                       is_(True))
            check_that("Module title is displayed",
                       utilities.find_shadow_dom_element(self.driver, locators.MODULE_TITLE_ON_PORTAL_CSS, locators.MODULE_BODY_CSS).text,
                       equal_to(constants.published_module))
            check_that("Product name displayed on Customer Portal",
                       utilities.find_shadow_dom_element(self.driver, locators.CP_PRODUCT_NAME_CSS, locators.MODULE_BODY_CSS).text,
                       equal_to(constants.product_name))
            check_that("Product version displayed on Customer Portal",
                       utilities.find_shadow_dom_element(self.driver, locators.CP_PRODUCT_VERSION_CSS, locators.MODULE_BODY_CSS).text,
                       equal_to(constants.product_version))
            legal_notice = utilities.find_shadow_dom_element(self.driver, locators.LEGAL_NOTICE_ON_PORTAL_CSS,
                                                             locators.MODULE_BODY_CSS)
            check_that("legal notice is displayed at the bottom of preview page", legal_notice.text,
                       contains_string("Legal Notices for Trademarks"))
            legal_notice_href = legal_notice.get_attribute("href")
            check_that("verify legal notice link", legal_notice_href, contains_string(constants.legal_notice_link))
            image = utilities.find_shadow_dom_element(self.driver, locators.IMAGE_CSS, locators.MODULE_BODY_CSS)
            src = image.get_attribute("src")
            imageasset = urlparse(src)
            imageasset = imageasset.path.split("/")[2]
            cmd = "echo " + imageasset + "|base64 -d"
            try:
                # subprocess.check_call(cmd, shell=True)
                path = subprocess.getoutput(cmd)
                print("Image file path::", path)
                # image_file = "/content/repositories/" + test_repo_name + "/entities/enterprise/modules/images/" + constants.image_file_name
                check_that("Path to image1", path, contains_string(constants.image_file_name))
            except subprocess.CalledProcessError as e:
                lcc.log_info("Unable to decode imageasset")
        except Exception as e:
            lcc.log_info(e)
        finally:
            self.driver.close()
            utilities.switch_to_first_tab(self.driver)

    @lcc.test("verify attribute is resolving correctly on preview page")
    def verify_attribute_text(self):
        try:
            utilities.click_element(self.driver, By.LINK_TEXT, "Search")
            search_page.search_for_module_and_click(self.driver, constants.search_module_with_attribute)
            utilities.click_element(self.driver, By.CSS_SELECTOR, locators.MODULE_DISPLAY_PREVIEW_BUTTON_CSS)
            utilities.wait(2)
            utilities.switch_to_latest_tab(self.driver)
            attribute_text = utilities.find_shadow_dom_element(self.driver, locators.ATTRIBUTE_ON_PREVIEW_CSS,
                                                               locators.MODULE_BODY_CSS).text
            check_that("verify attribute is resolving correctly on preview page", attribute_text,
                       contains_string(constants.attribute))
        except Exception as e:
            lcc.log_info(e)
        finally:
            self.driver.close()
            utilities.switch_to_first_tab(self.driver)

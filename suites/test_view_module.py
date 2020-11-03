import sys
import re
from helpers.base_screenshot import Screenshot
import lemoncheesecake.api as lcc
from lemoncheesecake.matching import *
from selenium.common.exceptions import TimeoutException
from pages import search_page
from helpers import utilities
from helpers import constants
from helpers import locators
from fixtures import fixture
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
sys.path.append("..")

# SUITE = {
#     "description": "View module test",
#     "rank": "5"
# }

url = fixture.url


@lcc.suite("Suite: Module view page checks for unpublished modules and already published.", rank="6")
class test_view_module(Screenshot):
    driver = lcc.inject_fixture("driver_obj")

    @lcc.test("Verify that for authenticated user, unpublished module displays all expected checks: Preview, ability to"
              " Publish, and status")
    @lcc.depends_on('test_publish_module.publish_module')
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
                   utilities.get_text(self.driver, By.CSS_SELECTOR, locators.MODULE_DISPLAY_PUBLISH_BUTTON_CSS),
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
    @lcc.depends_on('test_publish_module.publish_module')
    def authenticated_user_view_published_module(self):
        utilities.click_element(self.driver, By.LINK_TEXT, "Search")
        # # Click on the title if it is displayed on the first page
        # try:
        #     utilities.click_element(self.driver, By.LINK_TEXT, constants.module_to_be_published)
        # # If the title is not found on the first page, search for the title and then click
        # except TimeoutException as e:
        search_page.search_for_module_and_click(
            self.driver, constants.module_to_be_published)
        utilities.find_element(self.driver, By.CSS_SELECTOR, locators.MODULE_DISPLAY_PUBLISH_BUTTON_CSS)
        check_that("URL", self.driver.current_url,
                   contains_string(url + constants.module_display_page_path_after_published_module))
        check_that("Button", utilities.get_text(
            self.driver, By.CSS_SELECTOR, locators.MODULE_DISPLAY_PREVIEW_BUTTON_CSS), contains_string("Preview"))
        check_that("Button", utilities.get_text(
            self.driver, By.CSS_SELECTOR, locators.MODULE_DISPLAY_PUBLISH_BUTTON_CSS), contains_string("Unpublish"))
        # Add a check that the Published column contains some Published time.

    @lcc.test("Verify that 'View on Customer Portal' link navigates to correct page and verify the presence of content")
    @lcc.depends_on('test_publish_module.publish_module')
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
            utilities.wait(6)
            content_body_on_portal = self.driver.find_element_by_css_selector(locators.MODULE_BODY_ON_PORTAL_CSS)
            # content_body_on_portal = utilities.find_element(self.driver, By.CSS_SELECTOR, locators.MODULE_BODY_ON_PORTAL_CSS)
            check_that("Module content displayed on the Customer Portal", content_body_on_portal.is_displayed(),
                       is_(True))
        except (TimeoutException, StaleElementReferenceException, NoSuchElementException) as e:
            lcc.log_error("Error finding element!!!")
            lcc.log_error(e)
        finally:
            self.driver.close()
            utilities.switch_to_first_tab(self.driver)

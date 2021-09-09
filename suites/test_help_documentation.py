import sys

from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
import lemoncheesecake.api as lcc
from lemoncheesecake.matching import *
from helpers import utilities, locators, constants


@lcc.suite("Suite: Tests for help documentation", rank=13)
class test_help_documentation():
    driver = lcc.inject_fixture("driver_obj")

    @lcc.test("Verify that help documentation is displayed")
    def help_doc(self):
        try:
            utilities.wait(2)
            utilities.click_element(self.driver, By.LINK_TEXT, locators.MENU_SEARCH_PAGE_LINK_TEXT)
            utilities.page_reload(self.driver)
            utilities.wait(1)
            utilities.click_element(self.driver, By.CSS_SELECTOR, locators.HELP_ICON_CLASS_NAME)
            utilities.click_element(self.driver, By.LINK_TEXT, locators.USER_GUIDE_LINK_TEXT)
            utilities.wait(2)
            utilities.switch_to_latest_tab(self.driver)
            lcc.log_info(self.driver.current_url)
            check_that("page url", self.driver.current_url, contains_string(constants.help_user_guide_url))
            #title_of_user_guide = utilities.find_shadow_dom_element(self.driver,
            #                                                       locators.TITLE_OF_USER_GUIDE_CSS,
            #                                                      locators.USER_GUIDE_PARENT_CSS).text
            title_of_user_guide=utilities.get_text(self.driver,By.CSS_SELECTOR,locators.TITLE_OF_USER_GUIDE_CSS)
            check_that("title of the page", title_of_user_guide, contains_string("Help"))
            st = utilities.get_text(self.driver, By.ID, locators.PAGE_DATA)
            check_that("Help Documemnt to ", st, not_(contains_string("Invalid include:")))
        except (TimeoutException, NoSuchElementException) as e:
            lcc.log_error(e)
        finally:
            self.driver.close()
            utilities.switch_to_first_tab(self.driver)
import sys
from helpers import base
import lemoncheesecake.api as lcc
from pages import login_page
from lemoncheesecake.matching import *
from helpers.base_screenshot import Screenshot
sys.path.append("..")


# SUITE = {
#     "description": "Login tests suite",
#     "rank": "1"
# }


@lcc.suite("Suite: User login functionality", rank="1")
class test_login(Screenshot):
    driver = lcc.inject_fixture("driver_obj")

    @lcc.test("Verify that user is able to login successfully and the username is displayed on top right")
    def verify_login_success(self):
        # 'driver' param is the webdriver object that is being called from 'setup' fixture and used through the scope
        # of the session.
        username = base.config_reader('login', 'username')
        #login_page.login(driver)
        logged_in_user = login_page.get_logged_in_username(self.driver)
        lcc.log_info("Logged in username: %s" % logged_in_user)
        assert_that("Logged in username is visible", logged_in_user,
                    contains_string(username), quiet=False)

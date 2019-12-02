import sys
from helpers import base
import lemoncheesecake.api as lcc
from pages import login_page
from helpers.browser_util import Driver
from helpers import utilities
from lemoncheesecake.matching import *
sys.path.append("..")


@lcc.suite("Login page suite")
class LoginTest(Driver):

    @lcc.test("Verify that user is able to login successfully")
    def verify_login_success(self):
        username = base.config_reader('login', 'username')
        login_page.login(self.driver)
        logged_in_user = login_page.get_logged_in_username(self.driver)
        assert_that("Logged in username is visible", logged_in_user, contains_string(username), quiet=False)


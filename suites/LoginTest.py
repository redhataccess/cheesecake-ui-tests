import sys
from helpers import base
import lemoncheesecake.api as lcc
from pages import login_page
from helpers.browser_util import Driver
from helpers import utilities
sys.path.append("..")


@lcc.suite("Login page tests")
class LoginTest(Driver):

    username = base.config_reader('login', 'username')

    @lcc.test("check login success")
    def verify_login_success(self):
        login_page.login(self.driver)
        logged_in_user = login_page.get_logged_in_username(self.driver)
        utilities.assert_contains_text(LoginTest.username, logged_in_user)

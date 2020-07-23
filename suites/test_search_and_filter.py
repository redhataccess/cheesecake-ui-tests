import sys
import lemoncheesecake.api as lcc
from lemoncheesecake.matching import *
from helpers import utilities
from helpers import constants
from helpers import locators
from helpers.base_screenshot import Screenshot
import time
import requests
from fixtures import fixture
from selenium.webdriver.common.by import By
sys.path.append("..")


@lcc.disabled()
@lcc.suite("Suite: Tests for all the search and filter functionality", rank="9")
class test_search_and_filter(Screenshot):
    driver = lcc.inject_fixture("driver_obj")

    @lcc.test('Verify that search results are as expected')
    def search_for_text(self):
        pass


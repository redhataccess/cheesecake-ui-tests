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
@lcc.suite("Suite: Tests for module preview", rank="8")
class test_module_preview(Screenshot):
    driver = lcc.inject_fixture("driver_obj")

    @lcc.test('Verify that the image included in the module is resolved correctly')
    # pick a module with an image and check for image presence on the UI.

    @lcc.test('Verify that the attributes resolve correctly in the module')
    # pick a module and add statements to it: resolve attributes.

    @lcc.test("Verify if the title/abstract/headline/description are placed accurately in the respective metadata fields")
    # use the api endpoints to verify this.


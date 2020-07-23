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
@lcc.suite("Suite: Tests for assemblies", rank="7")
class test_preview_assembly(Screenshot):
    driver = lcc.inject_fixture("driver_obj")

    @lcc.test('Verify that assembly can be previewed successfully and loads all the modules')
      # Add the list of assembly and modules included in the constants file and verify in the preview for all the
      # headings to be present

    @lcc.test("verify that the images resolve correctly in the assembly")
    # use the same data that was used for verifying the image presence in a module


    @lcc.test("verify that the attributes resolve correctly on the UI")
    # use the same data as used in test_module_preview.py




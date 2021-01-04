from helpers import utilities
from helpers import locators
from helpers import constants
import lemoncheesecake.api as lcc
from lemoncheesecake.matching import *
import urllib.parse as urllib
import sys
from fixtures import fixture
import requests
from helpers import base
from selenium.webdriver.common.by import By
sys.path.append("..")

username = base.config_reader('login', 'username')
auth = base.config_reader('login', 'password')

# Reset edit metadata form
def reset_edit_metadata_from(driver):
    utilities.select_value_from_dropdown(driver, By.CSS_SELECTOR, locators.PRODUCT_NAME_DROPDOWN_CSS, "Select a Product")
    utilities.select_value_from_dropdown(driver, By.CSS_SELECTOR, locators.PRODUCT_VERSION_DROPDOWN_CSS, "Select a Version")
    utilities.select_value_from_dropdown(driver, By.CSS_SELECTOR, locators.PRODUCT_USECASE_DROPDOWN_CSS, "Select Use Case")
    utilities.enter_text(driver, By.CSS_SELECTOR, locators.PRODUCT_URLFRAGMENT_CSS, "")

# Fills the edit metadata form with the values passed as parameters and clicks on the save button
def fill_edit_metadata_form(driver, product_name, product_version, usecase, url_fragment):
    utilities.wait(2)
    utilities.select_value_from_dropdown(driver, By.CSS_SELECTOR, locators.PRODUCT_NAME_DROPDOWN_CSS, product_name)
    utilities.wait(2)
    utilities.select_value_from_dropdown(driver, By.CSS_SELECTOR, locators.PRODUCT_VERSION_DROPDOWN_CSS, product_version)
    utilities.wait(2)
    utilities.select_value_from_dropdown(driver, By.CSS_SELECTOR, locators.PRODUCT_USECASE_DROPDOWN_CSS, usecase)
    utilities.wait(2)
    utilities.enter_text(driver, By.CSS_SELECTOR, locators.PRODUCT_URLFRAGMENT_CSS, url_fragment)
    utilities.wait(5)
    utilities.click_element(driver, By.CSS_SELECTOR, locators.EDIT_METADATA_SAVE_CSS)
    utilities.wait(2)

# Returns path to the adoc file from the display module page url for that module
def get_path_to_adoc(driver):
    url = driver.current_url
    temp = urllib.urlparse(url).fragment
    temp = temp.strip("/module")
    path = temp.split('?')[0]
    path = "content/"+path
    return path

# Adds metadata to the module which is currently open and publishes it
def add_metadata_and_publish(driver):
    # f = fixture()
    # lcc.log_info("Added following product information to the module::\nProduct name:" + f.product_name +"\nProduct version:"+constants.product_version+"\nUse case:"+constants.use_case)
    string = driver.current_url
    str = string.split("?")
    lcc.log_info(str[0])
    if "module" in str[0]:
        path = (str[0].replace("pantheon/#/module", "content"))
    elif "assembly" in str[0]:
        path = (str[0].replace("pantheon/#/assembly", "content"))
    else:
        lcc.log_info("Invalid url!!!")
    var = str[1].split("=")
    metadata_path = path + "/en_US/variants/" + var[1] +"/draft/metadata"
    product_uuid = fixture.get_product_id()
    body = {
        "productVersion":product_uuid,
        "documentUsecase":"Deploy",
        "urlFragment":"",
        "searchKeywords":""
    }
    # Add metadata from api
    add_metadata = requests.post(url=metadata_path, data=body, auth=(username, auth))
    lcc.log_info("Added metadata to::")
    lcc.log_info(path)
    utilities.page_reload(driver)

    # utilities.click_element(driver, By.XPATH, locators.ADD_METADATA_BUTTON_XPATH)
    # fill_edit_metadata_form(driver, constants.product_name, constants.product_version,
    #                                             constants.use_case, constants.url_fragment)
    body = {":operation": "pant:publish",
            "locale": "en_US",
            "variant": var[1]
            }
    publish = requests.post(url=path, data=body, auth=(username, auth))
    lcc.log_info("Published document::")
    lcc.log_info(path)
    # utilities.click_element(driver, By.ID, locators.MODULE_DISPLAY_PUBLISH_BUTTON_ID)
    # utilities.wait(10)
    utilities.page_reload(driver)
    utilities.wait(3)
    assert_that("Button contains text", utilities.get_text(driver, By.ID, locators.MODULE_DISPLAY_UNPUBLISH_BUTTON_ID), contains_string("Unpublish"))
    utilities.wait(5)

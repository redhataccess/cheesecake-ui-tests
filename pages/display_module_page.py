from helpers import utilities
from helpers import locators
from helpers import constants
import lemoncheesecake.api as lcc
import urllib.parse as urllib
import sys
sys.path.append("..")

# Reset edit metadata form
def reset_edit_metadata_from(driver):
    utilities.select_value_from_dropdown(driver, locators.PRODUCT_NAME_DROPDOWN_CSS, "Select a Product")
    utilities.select_value_from_dropdown(driver, locators.PRODUCT_VERSION_DROPDOWN_CSS, "Select a Version")
    utilities.select_value_from_dropdown(driver, locators.PRODUCT_USECASE_DROPDOWN_CSS, "Select Use Case")
    utilities.enter_text_by_css_selector(driver, locators.PRODUCT_URLFRAGMENT_CSS, "")

# Fills the edit metadata form with the values passed as parameters and clicks on the save button
def fill_edit_metadata_form(driver, product_name, product_version, usecase, url_fragment):
    utilities.select_value_from_dropdown(driver, locators.PRODUCT_NAME_DROPDOWN_CSS, product_name)
    utilities.select_value_from_dropdown(driver, locators.PRODUCT_VERSION_DROPDOWN_CSS, product_version)
    utilities.select_value_from_dropdown(driver, locators.PRODUCT_USECASE_DROPDOWN_CSS, usecase)
    utilities.enter_text_by_css_selector(driver, locators.PRODUCT_URLFRAGMENT_CSS, url_fragment)
    utilities.click_element_by_css_selector(driver, locators.EDIT_METADATA_SAVE_CSS)

# Returns path to the adoc file from the display module page url for that module
def get_path_to_adoc(driver):
    url = driver.current_url
    path = urllib.urlparse(url).fragment
    path = "content"+path
    return path

# Adds metadata to the module which is currently open and publishes it
def add_metadata_and_publish(driver):
    lcc.log_info("Added following product information to the module::\nProduct name:" +constants.product_name+"\nProduct version:"+constants.product_version+"\nUse case:"+constants.use_case+"\nURL fragment:"+constants.url_fragment)
    utilities.click_element_by_css_selector(driver, locators.EDIT_METADATA_DROPDOWN_CSS)
    utilities.click_element_by_css_selector(driver, locators.EDIT_METADATA_BUTTON_CSS)
    fill_edit_metadata_form(driver, constants.product_name, constants.product_version,
                                                constants.use_case, constants.url_fragment)
    utilities.wait(2)
    utilities.click_element_by_css_selector(driver, locators.MODULE_DISPLAY_PUBLISH_BUTTON_CSS)
    utilities.page_reload(driver)
    utilities.wait(5)

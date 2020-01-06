from helpers import utilities
from helpers import locators
import sys
sys.path.append("..")

#Reset edit metadata form
def reset_edit_metadata_from(driver):
    utilities.select_value_from_dropdown(driver, locators.PRODUCT_NAME_DROPDOWN_CSS, "Select a Product")
    utilities.select_value_from_dropdown(driver, locators.PRODUCT_VERSION_DROPDOWN_CSS, "Select a Version")
    utilities.select_value_from_dropdown(driver, locators.PRODUCT_USECASE_DROPDOWN_CSS, "Select Use Case")
    utilities.enter_text_by_css_selector(driver, locators.PRODUCT_URLFRAGMENT_CSS, "")


from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from lemoncheesecake.matching import *
import lemoncheesecake.api as lcc
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException
import random
import string
import time


def wait_for_element(driver, locator_type, locator_value):
    try:
        wait = WebDriverWait(driver, 30)
        element = wait.until(
            ec.visibility_of_element_located((locator_type, locator_value)))
    except TimeoutException or StaleElementReferenceException as e:
        lcc.log_error(string(e))
        raise NoSuchElementException("Element not displayed on page for the locator::" + locator_type + "->" + locator_value)
    else:
        return element

def click_element(driver, locator_type, locator_value):
    element = wait_for_element(driver, locator_type, locator_value)
    element.click()

def enter_text(driver, locator_type, locator_value, text):
    element = wait_for_element(driver, locator_type, locator_value)
    element.clear()
    element.send_keys(text)

def find_element(driver, locator_type, locator_value):
    element = wait_for_element(driver, locator_type, locator_value)
    return element

def get_text(driver, locator_type, locator_value):
    element = wait_for_element(driver, locator_type, locator_value)
    text = element.text
    return text

def find_elements_by_id(driver, locator):
    try:
        element_list = driver.find_elements_by_id(locator)
    except NoSuchElementException as e:
        lcc.log_error(e)
    return element_list

def find_elements_by_class_name(driver, locator):
    try:
        elements_list_by_class = WebDriverWait(driver, 30).until(ec.visibility_of_all_elements_located((By.CLASS_NAME,
                                                                                                    locator)))
    except TimeoutException as e:
        lcc.log_error("Element not found after 30 sec wait!!!")
        lcc.log_error(e)
    return elements_list_by_class

def find_elements_by_css_selector(driver, locator):
    try:
        elements_list_by_css_selector = driver.find_elements(By.CSS_SELECTOR, locator)
    except NoSuchElementException as e:
        lcc.log_error(e)
    return elements_list_by_css_selector

def wait(count):
    time.sleep(count)

def switch_to_latest_tab(driver):
    driver.switch_to.window(driver.window_handles[1])

def switch_to_first_tab(driver):
    driver.switch_to.window(driver.window_handles[0])

# Verifies title for confirmation modal and accept the modal
def verify_and_accept_confirmation_modal(driver, modal_title_xpath, modal_title, confirmation_yes):
    check_that("Confirmation modal", get_text(driver, By.XPATH, modal_title_xpath), contains_string(modal_title))
    click_element(driver, By.CSS_SELECTOR, confirmation_yes)

def page_reload(driver):
    driver.refresh()

def select_value_from_dropdown(driver, locator_type, dropdown, value):
    try:
        select = Select(find_element(driver, locator_type, dropdown))
        select.select_by_visible_text(value)
    except NoSuchElementException as e:
        lcc.log_error(e)

def generate_random_string(string_length):
    # Generate a random string of fixed length
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(string_length))
    return random_string

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from lemoncheesecake.matching import *
import lemoncheesecake.api as lcc
from helpers import locators
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException
import random
import string
import time
from polling2 import poll


def wait_for_element(driver, locator_type, locator_value):
    try:
        wait = WebDriverWait(driver, 45)
        element = wait.until(
            ec.visibility_of_element_located((locator_type, locator_value)))
    except TimeoutException or StaleElementReferenceException as e:
        lcc.log_error(str(e))
        raise NoSuchElementException(
            "Element not displayed on page for the locator::" + locator_type + "->" + locator_value)
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
        element_list = driver.find_elements(By.ID, locator)
    except NoSuchElementException as e:
        lcc.log_error(str(e))
    return element_list


def find_elements_by_class_name(driver, locator):
    try:
        elements_list_by_class = WebDriverWait(driver, 30).until(ec.visibility_of_all_elements_located((By.CLASS_NAME,
                                                                                                    locator)))
    except TimeoutException as e:
        lcc.log_error("Element not found after 30 sec wait!!!")
        lcc.log_error(str(e))
    return elements_list_by_class


def find_elements_by_css_selector(driver, locator):
    try:
        elements_list_by_css_selector = driver.find_elements(By.CSS_SELECTOR, locator)
    except NoSuchElementException as e:
        lcc.log_error(str(e))
    return elements_list_by_css_selector

def find_elements_by_XPATH(driver, locator):
    try:
        elements_list_by_XPATH = driver.find_elements(By.XPATH, locator)
    except NoSuchElementException as e:
        lcc.log_error(str(e))
    return elements_list_by_XPATH

def wait(count):
    time.sleep(count)


def switch_to_latest_tab(driver):
    wait(5)
    driver.switch_to.window(driver.window_handles[1])
    lcc.log_info("Find the CP preview in the attachment below for debugging purposes")
    random = generate_random_string(3)
    file_name = "cp_preview_" + random + ".png"
    driver.save_screenshot(file_name)
    lcc.save_attachment_file(file_name)


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
        lcc.log_error(str(e))


def generate_random_string(string_length):
    # Generate a random string of fixed length
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(string_length))
    return random_string

def get_shadow_root(driver, shadow_root_parent):
    try:
        shadow_host = find_element(driver, By.CSS_SELECTOR,shadow_root_parent )
    except (TimeoutException, NoSuchElementException) as e:
        lcc.log_error(e)
    else:
        root_ele = driver.execute_script("return arguments[0].shadowRoot", shadow_host)
        return root_ele

def find_shadow_dom_element (driver,locator, shadow_root_parent):
    shadow_root = get_shadow_root(driver, shadow_root_parent)
    element = shadow_root.find_elements(By.CSS_SELECTOR, locator)
    return element

def read_file(filename):
    file = open(filename)
    line = file.read()
    file.close()
    return line

def get_CP_page_header(driver):
    headerTitle = driver.execute_script("return document.querySelector('#rhdocs').shadowRoot.querySelector('.rhdocs__header__primary-wrapper > h1').innerText")
    return headerTitle

def go_back_to_previous_page(driver):
    driver.execute_script("window.history.go(-1)")

def java_script_executor(driver,jsquery):
    driver.execute_script(jsquery)

def get_text_from_shadow_dom_element_CP(driver, css_selector):
    return driver.execute_script("return document.querySelector('#rhdocs').shadowRoot.querySelector('"+css_selector+"').innerText")


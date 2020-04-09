from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from lemoncheesecake.matching import *
from selenium.webdriver.support.ui import Select
import lemoncheesecake.api as lcc
from datetime import datetime
import random
import string
import time

# now_time = datetime.utcnow()

def click_element_by_xpath(driver, locator_value):
    wait = WebDriverWait(driver, 15)
    element = wait.until(
        ec.presence_of_element_located((By.XPATH, locator_value)))
    element.click()


def click_element_by_css_selector(driver, locator_value):
    wait = WebDriverWait(driver, 15)
    element = wait.until(ec.presence_of_element_located(
        (By.CSS_SELECTOR, locator_value)))
    element.click()


def click_element_by_id(driver, locator_value):
    wait = WebDriverWait(driver, 15)
    element = wait.until(
        ec.presence_of_element_located((By.ID, locator_value)))
    element.click()


def click_element_by_class_name(driver, locator_value):
    wait = WebDriverWait(driver, 15)
    element = wait.until(ec.presence_of_element_located(
        (By.CLASS_NAME, locator_value)))
    element.click()


def enter_text_by_xpath(driver, locator, value):
    wait = WebDriverWait(driver, 15)
    element = wait.until(ec.presence_of_element_located((By.XPATH, locator)))
    element.clear()
    element.send_keys(value)


def enter_text_by_css_selector(driver, locator, value):
    wait = WebDriverWait(driver, 15)
    element = wait.until(ec.presence_of_element_located(
        (By.CSS_SELECTOR, locator)))
    element.clear()
    element.send_keys(value)


def enter_text_by_id(driver, locator, value):
    wait = WebDriverWait(driver, 15)
    element = wait.until(ec.presence_of_element_located((By.ID, locator)))
    element.clear()
    element.send_keys(value)


def enter_text_by_class_name(driver, locator, value):
    wait = WebDriverWait(driver, 15)
    element = wait.until(
        ec.presence_of_element_located((By.CLASS_NAME, locator)))
    element.clear()
    element.send_keys(value)


def find_element_by_partial_text(driver, locator):
    wait = WebDriverWait(driver, 15)
    element = wait.until(ec.presence_of_element_located(
        (By.PARTIAL_LINK_TEXT, locator)))
    return element


def find_element_by_css(driver, locator):
    wait = WebDriverWait(driver, 15)
    element = wait.until(ec.presence_of_element_located(
        (By.CSS_SELECTOR, locator)))
    return element


def find_elements_by_id(driver, locator):
    element_list = driver.find_elements_by_id(locator)
    return element_list


def find_element_by_class_name(driver, locator):
    element = WebDriverWait(driver, 15).until(ec.presence_of_element_located((By.CLASS_NAME, locator)))
    return element


def find_elements_by_class_name(driver, locator):
    elements_list_by_class = WebDriverWait(driver, 30).until(ec.visibility_of_all_elements_located((By.CLASS_NAME,
                                                                                                    locator)))
    return elements_list_by_class


def find_elements_by_css_selector(driver, locator):
    elements_list_by_css_selector = driver.find_elements(By.CSS_SELECTOR, locator)
    return elements_list_by_css_selector


def click_element_by_link_text(driver, locator_value):
    element = find_element_by_partial_text(driver, locator_value)
    element.click()


def get_text_by_xpath(driver, locator):
    text = driver.find_element_by_xpath(locator).text
    return text


def get_text_by_css(driver, locator):
    text = driver.find_element_by_css_selector(locator).text
    return text


def wait(count):
    time.sleep(count)


def switch_to_latest_tab(driver):
    driver.switch_to.window(driver.window_handles[1])


def switch_to_first_tab(driver):
    driver.switch_to.window(driver.window_handles[0])


# Verifies title for confirmation modal and accept the modal
def verify_and_accept_confirmation_modal(driver, modal_title_xpath, modal_title, confirmation_yes):
    check_that("Confirmation modal", get_text_by_xpath(
        driver, modal_title_xpath), contains_string(modal_title))
    click_element_by_css_selector(driver, confirmation_yes)


def page_reload(driver):
    driver.refresh()


def select_value_from_dropdown(driver, dropdown, value):
    select = Select(driver.find_element_by_css_selector(dropdown))
    select.select_by_visible_text(value)


def generate_random_string(string_length):
    # Generate a random string of fixed length
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(string_length))
    return random_string

def get_current_date_time(now_time):
    # datetime object containing current date and time
    print ("now =", now_time)
    dt_string = now_time.strftime("%b %d, %Y %H:%M")
    print ("date and time =", dt_string)
    return dt_string

def get_current_time_plus_one(time):
    min_plus_one = str(time.minute + 1)
    print ("min = ", min_plus_one)
    dt_string_plus1 = time.strftime("%b %d, %Y %H:") + min_plus_one
    print ("plus one =", dt_string_plus1)
    return dt_string_plus1

def get_current_time_minus_one(time):
    min_minus_one = str(time.minute - 1)
    print ("min = ", min_minus_one)
    dt_string_minus1 = time.strftime("%b %d, %Y %H:") + min_minus_one
    print ("minus one =", dt_string_minus1)
    return dt_string_minus1
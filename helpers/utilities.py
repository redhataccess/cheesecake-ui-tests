from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from lemoncheesecake.matching import *
from selenium.webdriver.support.ui import Select
import random
import string
import time


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

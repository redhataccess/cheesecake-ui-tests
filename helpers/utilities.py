from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def click_element_by_xpath(driver, locator_value):
    wait = WebDriverWait(driver, 15)
    element = wait.until(ec.presence_of_element_located((By.XPATH, locator_value)))
    element.click()


def click_element_by_css_selector(driver, locator_value):
    wait = WebDriverWait(driver, 15)
    element = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, locator_value)))
    element.click()


def click_element_by_id(driver, locator_value):
    wait = WebDriverWait(driver, 15)
    element = wait.until(ec.presence_of_element_located((By.ID, locator_value)))
    element.click()


def click_element_by_class_name(driver, locator_value):
    wait = WebDriverWait(driver, 15)
    element = wait.until(ec.presence_of_element_located((By.CLASS_NAME, locator_value)))
    element.click()


def enter_text_by_xpath(driver, locator, value):
    wait = WebDriverWait(driver, 15)
    element = wait.until(ec.presence_of_element_located((By.XPATH, locator)))
    element.send_keys(value)


def enter_text_by_css_selector(driver, locator, value):
    wait = WebDriverWait(driver, 15)
    element = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, locator)))
    element.send_keys(value)


def enter_text_by_id(driver, locator, value):
    wait = WebDriverWait(driver, 15)
    element = wait.until(ec.presence_of_element_located((By.ID, locator)))
    element.send_keys(value)


def enter_text_by_class_name(driver, locator, value):
    wait = WebDriverWait(driver, 15)
    element = wait.until(ec.presence_of_element_located((By.CLASS_NAME, locator)))
    element.send_keys(value)


def find_element_by_partial_text(driver, locator):
    wait = WebDriverWait(driver, 15)
    element = wait.until(ec.presence_of_element_located((By.PARTIAL_LINK_TEXT, locator)))
    return element


def assert_text(driver, expected_value, locator):
    actual_value = WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH, locator))).text
    assert actual_value == expected_value

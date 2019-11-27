from selenium import webdriver
import lemoncheesecake.api as lcc
from webdriver_manager.chrome import ChromeDriverManager

import helpers.base as base


class Driver(object):

    url = base.config_reader('qa', 'base_url')

    def setup_suite(self, setup_test_repo):
        lcc.log_info("Inside setup")
        #global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver = driver
        self.driver.get(Driver.url)
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)


    def teardown_suite(self):
        self.driver.close()
        self.driver.quit()

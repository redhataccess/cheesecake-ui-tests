import lemoncheesecake.api as lcc
import datetime
import sys
sys.path.append("..")


class Screenshot:
    # Calling the driver fixture in every class to avoid confusion in case anyone forgets to inherit the
    # Screenshot class.
    # The Screenshot class needs to be inherited in each suite class for the below method to be implemented.
    driver = None

    def teardown_test(self, test, status):
        if status == "passed":
            pass
        elif status == "failed":
            lcc.log_info("Please find the screenshot below as a failure was observed in the test...")
            test_name = test.name
            now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            screenshot_filename = test_name + now + ".png"
            self.driver.save_screenshot(screenshot_filename)
            lcc.save_attachment_file(screenshot_filename)
        else:
            lcc.log_info("Status of the test not known and unable to capture a screenshot.")




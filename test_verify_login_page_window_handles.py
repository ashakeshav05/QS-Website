# #########################################
# Test Case = Verify the login page using window handles

# Objective: The window handling feature allows one to handle single as well as multiple windows in Selenium
# Main Steps:
# 1.	Open the Chrome browser.
# 2.	Navigate to https://www.qs.com/qs-solution-login/
# 3.	Click on QS HUB Login
# 4.	Another new tab will open
# 5.	And then capture the “QS HUB logo” inner text.
# 6.	And display the inner text on console page.
# 7.	And close the previous browser tab, which is the first one.

# Author: Asha M
# Date: June 17th, 2025
################################
#
# Copyright 2025 QS Quacquarelli Symonds,Bangalore
#
###############################
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from webdriver_manager.chrome import ChromeDriverManager

class TestQSLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        options = Options()# creates a new instance of the Options class
        # The browser window will remain open even if the script that's
        # launching it is terminated or interrupted.
        options.add_experimental_option("detach", True)
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                                      options=options)
        cls.driver.maximize_window()
        cls.driver.get("https://www.qs.com/qs-solution-login/")
        cls.accept_cookies(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    @classmethod
    def accept_cookies(cls, driver):
        # Accept button in Cookies dialog
        accept_button = WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.ID, "hs-eu-confirmation-button")))

        driver.execute_script("arguments[0].scrollIntoView();", accept_button)
        driver.execute_script("arguments[0].click();", accept_button)
        # Check for Accept button available
        cls.assertIsNotNone(accept_button, "Failed to find accept cookies button")

    def test_click_login_button(self):
        """Click login button on the QS website."""

        login_button = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "//a[@href='https://qs-hub2.qs."
                                                                   "com/wp-login.php' and text()="
                                                                   "'Login']")))

        login_button.click()
        self.assertTrue(login_button.is_enabled(), "Login button is not clickable")

    def test_get_inner_text(self):
        """Get the inner text of the specified element"""

        time.sleep(2)
        # As window will be changed navigating to new window and getting the inner text of the logo
        orig_window = self.driver.current_window_handle
        for handle in self.driver.window_handles:
            if handle != orig_window:
                self.driver.switch_to.window(handle)
                break

        element = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//a[@href='https:"
                                                                       "//qs-hub2.qs.com/']")))

        inner_text = element.get_attribute("textContent")

        print(f"'QS HUB logo' inner text >> {inner_text}")
        self.assertIsNotNone(inner_text, "Inner text is None")

if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)
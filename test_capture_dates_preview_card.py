# #########################################
# Test Case = Capture the Dates of all the preview card available on the page
# Objective: Ensure that the date is visible on all preview cards.
# Main Steps:
# 1. Open the Chrome browser
# 2. Navigate to https://www.qs.com/insights/
# 3. Select “QS news” value from the “Topics” dropdown.
# 4. Then capture the Dates of all the preview cards. (Ex: 23 Jan 2025)
# 5. And display on the console page.

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
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

class TestQSInsights(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        options = Options()# creates a new instance of the Options class
        # The browser window will remain open even if the script that's
        # launching it is terminated or interrupted.
        options.add_experimental_option("detach", True)
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                                      options=options)
        cls.driver.maximize_window()
        cls.driver.get("https://www.qs.com/insights/")

    @classmethod
    def tearDownClass(cls):
        #Exit Chrome Browser
        cls.driver.quit()

    def test_accept_cookies(self):
        """Accept cookies on the QS website"""

        accept_button = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.ID, "hs-eu-confirmation-button")))
        # Check for Accept button enabled
        self.assertTrue(accept_button.is_enabled(), "Accept cookies button is not enabled")
        self.driver.execute_script("arguments[0].scrollIntoView();", accept_button)
        self.driver.execute_script("arguments[0].click();", accept_button)

    def test_select_category_get_dates(self):
        """Get the dates of the articles"""

        drop_down = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.CLASS_NAME, "category-select")))
        # selecting QS news in drop down
        select = Select(drop_down)
        select.select_by_value("qs-news")
        self.assertTrue(drop_down.is_enabled(), "Category dropdown is not enabled")

        time.sleep(4)  # takes a while to retrieve dates from the webpage
        date_elements = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_all_elements_located((By.CSS_SELECTOR,
                                                                  "p[id^='published_"
                                                                  "date_container']")))
        for index, el in enumerate(date_elements, start=1):
            print(f"{index}. {el.text}")
            self.assertIsNotNone(el.text, "No dates found")

if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)
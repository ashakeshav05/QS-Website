# #########################################
# Test Case = Verify broken images in the footer section
# Objective: Check that there are no broken images in the insights section.
# Main Steps:
# 1.	Open the Chrome browser.
# 2.	Navigate to https://www.qs.com/insights/
# 3.	Check any broken images available in the insights section.
# 4.	And display the broken images links in console section.

# Author: Asha M
# Date: June 17th, 2025
################################
#
# Copyright 2025 QS Quacquarelli Symonds,Bangalore
#
###############################
import requests
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from webdriver_manager.chrome import ChromeDriverManager

class TestBrokenImages(unittest.TestCase):
    def setUp(self):
        self.driver = self.initialize_driver() # Launch Chrome Browser
        self.accept_cookies(self.driver) # Accept cookies

    def tearDown(self):
        # Exit Chrome Browser
        self.driver.quit()

    def initialize_driver(self):
        """
        :return: Driver will launch Chrome browser and supports for further need to perform
        in the web page
        Initialize the Chrome WebDriver with options
        """
        options = Options()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.maximize_window()
        driver.get("https://www.qs.com/insights/")
        return driver

    def accept_cookies(self, driver):
        """
        :param driver: Chrome WebDriver
        :return: N/A
        Accept cookies on the QS website
        """
        accept_button = WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.ID, "hs-eu-confirmation-button")))
        driver.execute_script("arguments[0].scrollIntoView();", accept_button)
        driver.execute_script("arguments[0].click();", accept_button)
        self.assertIsNotNone(accept_button, "Failed to find accept cookies button")

    def test_broken_images(self):
        """
        :return: N/A
        Check for broken Images
        """
        images = self.driver.find_elements(By.TAG_NAME, "img")

        broken_images = []
        for image in images:
            src = image.get_attribute("src")
            if src:
                response = requests.get(src)
                if response.status_code != 200:
                    broken_images.append(src)
                    print("Broken Images:", src)
            else:
                print("No Broken Images found:")

        self.assertFalse(broken_images, f"Found {len(broken_images)} broken images: {broken_images}")


if __name__ == "__main__":
    unittest.main()
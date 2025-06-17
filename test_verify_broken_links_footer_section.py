# #########################################
# Test Case = Verify broken links in the footer section

# Objective: Check that there are no broken links in the footer section.
# Main Steps:
# 1. Open the Chrome browser
# 2. Navigate to https://www.qs.com/
# 3. Navigate to footer section
# 4. Check any broken links are available in the footer section.
# 5. And display the broken links in console sections

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
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions

class TestLinks(unittest.TestCase):
    def setUp(self):
        options = Options() #creates a new instance of the Options class
        #The browser window will remain open even if the script that's
        # launching it is terminated or interrupted.
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.maximize_window()
        self.driver.get("https://www.qs.com/")
        self.accept_cookies(self.driver)
        self.find_total_links()

    def tearDown(self):
        # Exit Chrome Browser
        self.driver.quit()

    def accept_cookies(self, driver):
        """Accept cookies on the QS website"""
        accept_button = WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.ID, "hs-eu-confirmation-button")))
        # Viewing the Accept button and clicking on it
        driver.execute_script("arguments[0].scrollIntoView();", accept_button)
        driver.execute_script("arguments[0].click();", accept_button)
        self.assertIsNotNone(accept_button, "Failed to find accept cookies button")

    def find_total_links(self):
        # Scrolling to footer of the page
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Get all the available links
        links = self.driver.find_elements(By.TAG_NAME, "a")
        print("Total Number of Links:", len(links))
        self.assertGreater(len(links), 0, "No links found on the page")

    def test_broken_links(self):
        """Check for broken links on the page."""
        links = self.driver.find_elements(By.TAG_NAME, "a")

        broken_links = []  # Storing the links one after other
        for link in links:
            href = link.get_attribute("href") # Taking 'href' from the HTML page
            if href.startswith("http"):
                try:
                    response = requests.get(href)   #Taking response code
                    if response.status_code >= 400:
                        print(f"Broken link: {href} (Status Code: {response.status_code})")
                        # Adding all the broken links
                        broken_links.append((href, response.status_code))
                    else:
                        print("No broken link found.")

                except requests.RequestException as e:
                    print(f"Error checking link {href}: {e}")

        self.assertFalse(broken_links, f"Found {len(broken_links)} broken links: {broken_links}")

if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)
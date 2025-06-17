# #########################################
# Test Case = Valid Submission Flow on Contact us page

# Objective: Ensure that the form accepts valid input and displays a success message..
# Main Steps:
# 1. Open the Chrome browser
# 2. Navigate to https://www.qs.com/contact-us/
# 3. Fill all the mandatary fields.
# 4. Click on submit.
# 5. And capture the below success message using TestNG assertion mechanism.

######Remainining#####
# Click on 'Submit' button cannot be performed as Captcha should be handled by Admin only and error is Occurring ,
# only Admins has the rights.
# Required Success message using TestNG assertion mechanism could not be captured as it dependent on Step 4

# Author: Asha M
# Date: June 17th, 2025
################################
#
# Copyright 2025 QS Quacquarelli Symonds,Bangalore
#
###############################

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

class TestQSContactUs(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        options = Options()# creates a new instance of the Options class
        # The browser window will remain open even if the script that's
        # launching it is terminated or interrupted.
        options.add_experimental_option("detach", True)
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        cls.driver.maximize_window()
        cls.driver.get("https://www.qs.com/contact-us/")

    @classmethod
    def tearDownClass(cls):
        # Exit Chrome browser
        cls.driver.quit()

    def test_accept_cookies(self):
        """Accept cookies on the QS website"""

        accept_button = WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable((By.ID, "hs-eu-confirmation-button")))

        self.assertTrue(accept_button.is_enabled(), "Accept cookies button is not enabled")
        self.driver.execute_script("arguments[0].scrollIntoView();", accept_button)
        self.driver.execute_script("arguments[0].click();", accept_button)

        iframe = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//iframe"
                                                                       "[starts-with(@id, "
                                                                       "'hs-form-iframe')]")))

        self.driver.switch_to.frame(iframe)
        self.assertTrue(iframe, "Iframe not found")

    def test_fill_candidate_details(self):
        """Fill the details with the candidate"""
        # Enter Candidate Name
        first_name = self.driver.find_element(By.NAME, "firstname")
        first_name.send_keys("Asha")
        self.assertEqual(first_name.get_attribute("value"), "Asha", "First name has not entered"
                                                                    " correctly")
        # Enter Candidate last name
        last_name = self.driver.find_element(By.NAME, "lastname")
        last_name.send_keys("Muniraju")
        self.assertEqual(last_name.get_attribute("value"), "Muniraju",
                         "Last name has not entered correctly")
        # Select Country
        dropdown = self.driver.find_element(By.NAME, "country")
        select = Select(dropdown)
        select.select_by_visible_text("India")
        self.assertEqual(select.first_selected_option.text, "India", "Country not selected "
                                                                     "correctly")
        # Enter Candidate mail id
        email = self.driver.find_element(By.NAME, "email")
        email.send_keys("asham23keshav@QS.COM")
        self.assertEqual(email.get_attribute("value"), "asham23keshav@QS.COM", "Email not "
                                                                               "entered correctly")
        # Enter Job title
        job_title = self.driver.find_element(By.NAME, "jobtitle")
        job_title.send_keys("Software Tester")
        self.assertEqual(job_title.get_attribute("value"), "Software Tester",
                         "Job title not entered correctly")

        # Enter Organisation name
        comp_name = self.driver.find_element(By.NAME, "company")
        comp_name.send_keys("QS Organisation")
        self.assertEqual(comp_name.get_attribute("value"), "QS Organisation",
                         "Company not entered correctly")

    def test_select_interests(self):
        """Select the interests"""
        # WebDriver wait used for consistent clicking
        interest = WebDriverWait(self.driver, 20).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "//input[@type='checkbox'"
                                                                   " and @value='"
                                                                   "digital_innovation']")))

        self.driver.execute_script("arguments[0].click();", interest)
        self.assertTrue(interest.is_selected(), "Interest not selected")

    def test_agree_to_communications(self):
        """Agree to receive communications"""

        communications = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "//input[@type="
                                                                   "'checkbox' and "
                                                                   "@name='LEGAL_CONSENT."
                                                                   "subscription_type_163138980']")))

        self.driver.execute_script("arguments[0].click();", communications)
        self.assertTrue(communications.is_selected(), "Communications not selected")

    def test_send_message_to_qs(self):
        """Send a message to QS"""

        send_message = "Hello I'm excited to join QS Family"
        message = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.NAME, "message_to_qs")))

        message.send_keys(send_message)
        self.assertEqual(message.get_attribute("value"), send_message, "Message not sent correctly")

    ###Commenting out as CAPTCHA requires Admin permission to proceed,Hence skipping further steps
    '''def test_click_submit_button(self):
        """Submit the button"""
        time.sleep(2)
        submit_button = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "//input[@type='submit' and 
            @value='Submit']")))
        submit_button.click()'''

if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)
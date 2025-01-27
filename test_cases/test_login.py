# Import necessary modules
import re # Regular expressions module for pattern matching

import pytest
from selenium.webdriver.common.by import By  # Selenium module for locating web elements
from base_pages.Login_page import Login_Page # Import Login_Page class to interact with the login page
from time import sleep
from utilities.read_properties import ReadConfig # Utility to read configuration values (e.g., login info)
from utilities.custom_logger import LogMaker # Custom logger for logging test execution details

# Test class for Login functionality
class Test_01_Login:
    # Read configuration values for login test
    login_page_url = ReadConfig.get_login_page_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    invalid_username = ReadConfig.get_invalid_username()
    logger = LogMaker.log_gen()

    @pytest.mark.regression
    # Test case 1: Validate the title of the login page
    def test_title_validation(self, setup):
        """
                Verifies that the login page's title matches the expected title.

                :param setup: WebDriver instance provided by the pytest fixture.
                """
        self.logger.info("****************Test_01_Login****************")
        self.logger.info("****************verification of login page title****************")
        self.driver = setup # Initialize WebDriver instance
        self.driver.get(self.login_page_url) # Open the login page

        # Get the actual title of the login page
        act_title = self.driver.title
        exp_title = 'Account Login' # Expected title
        #print(act_title) # Print the actual title (for debugging purposes)

        # Validate if the actual title matches the expected title
        if act_title == exp_title:
            self.logger.info("****************pass****************") # Log success
            assert True # Pass the test
        else:
            # Capture a screenshot if the title validation fails
            self.screenshot_path = 'E:\\automationteststore\\screenshots\\test_title_validation.png'
            self.driver.save_screenshot(self.screenshot_path)
            self.logger.info("****************failed****************") # Log failure
            assert False # Fail the test
        self.driver.close() # Close the browser

    @pytest.mark.regression
    @pytest.mark.sanity
    # Test case 2: Validate login with valid credentials
    def test_valid_login(self, setup):
        """
                Verifies that login with valid credentials is successful.

                :param setup: WebDriver instance provided by the pytest fixture.
                """
        self.logger.info("****************Test_01_Login****************")
        self.logger.info("****************verification of valid login****************")
        self.driver = setup # Initialize WebDriver instance
        self.driver.get(self.login_page_url) # Open the login page

        # Create an instance of the Login_Page class
        self.admin_lp = Login_Page(self.driver)

        # Enter valid username and password
        self.admin_lp.enter_username(self.username)
        sleep(2) # Optional
        self.admin_lp.enter_password(self.password)
        sleep(2) # Optional
        self.admin_lp.click_login()
        sleep(2) # Optional

        # Verify if the login was successful by checking the displayed text
        span = self.driver.find_element(By.CSS_SELECTOR, "span.maintext").text.strip()
        if span == "MY ACCOUNT":
            assert True
            self.logger.info("****************passed****************") # Log success
        else:
            self.logger.info("****************failed****************") # Log failure
            assert False # Fail the test
        self.driver.close() # Close the browser

    @pytest.mark.regression
    # Test case 3: Validate login with invalid credentials
    def test_invalid_login(self, setup):
        """
                Verifies that login with invalid credentials is unsuccessful and displays the correct error message.

                :param setup: WebDriver instance provided by the pytest fixture.
                """
        self.logger.info("****************Test_01_Login****************")
        self.logger.info("****************verification of valid login****************")
        self.driver = setup # Initialize WebDriver instance
        self.driver.get(self.login_page_url) # Open the login page
        self.driver.implicitly_wait(10) # Implicit wait for elements to load

        # Create an instance of the Login_Page class
        self.admin_lp = Login_Page(self.driver)
        # Enter invalid username and valid password
        self.admin_lp.enter_username(self.invalid_username)
        #sleep(5)
        self.admin_lp.enter_password(self.password)
        #sleep(5)
        self.admin_lp.click_login() # Click the login button
        #sleep(5)
        # Verify if the correct error message is displayed
        actual_message = self.driver.find_element(By.CSS_SELECTOR, "div[class='alert alert-error alert-danger']").text.strip()
        if re.search(re.escape("Error: Incorrect login or password provided."), actual_message):
            self.logger.info("****************passed****************")
            assert True
        else:
            self.logger.info("****************failed****************")
            assert False
        self.driver.close()

# Import necessary modules
import re # Regular expressions module for pattern matching
import pytest
from selenium.webdriver.common.by import By
from base_pages.Login_page import Login_Page # Import Login_Page class to interact with the login page
from utilities.read_properties import ReadConfig # Utility to read configuration values (e.g., login info)
from utilities.custom_logger import LogMaker # Custom logger for logging test execution details

# Test class for Login functionality
@pytest.mark.regression
class TestLogin:

    logger = LogMaker.log_gen() # return logger

    @pytest.fixture(autouse=True) # does not need to be passed as parameter, runs before every test
    def setup_driver(self, setup):
        self.driver = setup
        # return url from read_properties
        self.url = ReadConfig.get_login_page_url()
        self.username = ReadConfig.get_username()
        self.password = ReadConfig.get_password()
        self.invalid_username = ReadConfig.get_invalid_username()
        # Create an instance of the Login_Page class
        self.lp = Login_Page(self.driver)

    # Test case 1: Validate the title of the login page
    def test_title_validation(self):
        self.logger.info("Validating login page title")

        self.driver.get(self.url)
        assert self.driver.title == "Account Login", "Title mismatch"

    @pytest.mark.sanity
    # Test case 2: Validate login with valid credentials
    def test_valid_login(self, setup):
        self.logger.info("Verification of valid login")
        self.driver.get(self.url) # Open the login page

        # Enter valid username and password
        self.lp.enter_username(self.username)
        self.lp.enter_password(self.password)
        self.lp.click_login()

        span = self.driver.find_element(By.CSS_SELECTOR, "span.maintext").text.strip()
        assert span == "MY ACCOUNT", "Test failed. Not logged in with valid credentials."

    # Test case 3: Validate login with invalid credentials
    def test_invalid_login(self, setup):
        self.logger.info("Verification of invalid login")
        self.driver.get(self.url)
        self.driver.implicitly_wait(10) # Implicit wait for elements to load

        # Enter invalid username and valid password
        self.lp.enter_username(self.invalid_username)
        #sleep(5)
        self.lp.enter_password(self.password)
        #sleep(5)
        self.lp.click_login()
        #sleep(5)

        actual_message = self.driver.find_element(By.CSS_SELECTOR, "div[class='alert alert-error alert-danger']").text.strip()
        assert re.search(re.escape("Error: Incorrect login or password provided."), actual_message)

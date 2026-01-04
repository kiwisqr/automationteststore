import random
import string
import re

import pytest

from base_pages.Create_Account_page import CreateAccount
from selenium.webdriver.common.by import By
from utilities.custom_logger import LogMaker
from utilities.read_properties import ReadConfig
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.regression
class TestCreateAccount:

    logger = LogMaker.log_gen()

    @pytest.fixture(autouse=True)
    def setup_driver(self, setup):
        self.driver = setup
        self.url = ReadConfig.get_login_page_url()
        self.create_acc = CreateAccount(self.driver)

    @pytest.mark.sanity
    def test_create_account(self, setup):
        self.logger.info("Validation of account creation")
        self.driver.get(self.url)  # Open the login page

        self.create_acc.get_to_create_account_page()
        self.logger.info("Providing info started")

        self.create_acc.enter_first_name("Claudia")
        self.create_acc.enter_last_name("Boier")
        email = generate_random_email()
        self.create_acc.enter_email(email)
        self.create_acc.enter_adress1("Pandurilor")
        self.create_acc.enter_city("Targu Mures")
        self.create_acc.select_country("Romania")
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, self.create_acc.textbox_region), "Mures"))
        self.create_acc.select_region("Mures")
        self.create_acc.enter_zip_code("540278")
        login_name = generate_random_login_name()
        self.create_acc.enter_login_name(login_name)
        self.create_acc.enter_password("123456")
        self.create_acc.enter_password_confirm("123456")
        self.create_acc.click_agree_privacy_policy()
        self.create_acc.clk_continue()
        validation_text = self.driver.find_element(By.CSS_SELECTOR, "#maincontainer > div > div.col-md-9.col-xs-12.mt20 > div > h1 > span.maintext").text.strip().capitalize()
        print("Text is:", validation_text)
        assert re.search(re.escape("Your account has been created!"), validation_text)
        screenshot_path = 'E:\\automationteststore\\screenshots\\test_create_account.png'
        self.driver.save_screenshot(screenshot_path)

def generate_random_email():
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    domain = random.choice(['gmail.com', 'yahoo.com', 'outlook.com'])
    return f'{username}@{domain}'

def generate_random_login_name():
    login_name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return login_name
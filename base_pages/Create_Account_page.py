# This file contains the locators and methods for the Create Account page functionality.
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class CreateAccount:
    # Locators for the create account page elements
    continue_create_Account = "#accountFrm > fieldset > button"
    textbox_first_name = "#AccountFrm_firstname"
    textbox_last_name = "#AccountFrm_lastname"
    textbox_email = "#AccountFrm_email"
    textbox_address1 = "#AccountFrm_address_1"
    textbox_city = "#AccountFrm_city"
    textbox_region = "#AccountFrm_zone_id"
    textbox_zipcode = "#AccountFrm_postcode"
    textbox_country = "#AccountFrm_country_id"
    textbox_login_name = "#AccountFrm_loginname"
    textbox_password = "#AccountFrm_password"
    textbox_password_confirm = "#AccountFrm_confirm"
    agree_privacy_policy = "#AccountFrm_agree"
    click_continue = "button[title='Continue']"

    def __init__(self, driver):
        """
               Constructor to initialize the driver.

               :param driver: WebDriver instance used to interact with the browser.
               """
        self.driver = driver

    # Action method to get to create account page
    def get_to_create_account_page(self):
        self.driver.find_element(By.CSS_SELECTOR, self.continue_create_Account).click()

    # Action methods for interacting with the create account page
    def enter_first_name(self, first_name):
        self.driver.find_element(By.CSS_SELECTOR, self.textbox_first_name).send_keys(first_name)

    def enter_last_name(self, last_name):
        self.driver.find_element(By.CSS_SELECTOR, self.textbox_last_name).send_keys(last_name)

    def enter_email(self, email):
        self.driver.find_element(By.CSS_SELECTOR, self.textbox_email).send_keys(email)

    def enter_adress1(self, adress1):
        self.driver.find_element(By.CSS_SELECTOR, self.textbox_address1).send_keys(adress1)

    def enter_city(self, city):
        self.driver.find_element(By.CSS_SELECTOR, self.textbox_city).send_keys(city)

    def select_region(self, region):
        dropdown = Select(self.driver.find_element(By.CSS_SELECTOR, self.textbox_region))
        dropdown.select_by_visible_text(region)

    def enter_zip_code(self, zipcode):
        self.driver.find_element(By.CSS_SELECTOR, self.textbox_zipcode).send_keys(zipcode)

    def select_country(self, country):
        dropdown = Select(self.driver.find_element(By.CSS_SELECTOR, self.textbox_country))
        dropdown.select_by_visible_text(country)

    def enter_login_name(self, login_name):
        self.driver.find_element(By.CSS_SELECTOR, self.textbox_login_name).send_keys(login_name)

    def enter_password(self, password):
        self.driver.find_element(By.CSS_SELECTOR, self.textbox_password).send_keys(password)

    def enter_password_confirm(self, password_confirm):
        self.driver.find_element(By.CSS_SELECTOR, self.textbox_password_confirm).send_keys(password_confirm)

    def click_agree_privacy_policy(self):
        self.driver.find_element(By.CSS_SELECTOR, self.agree_privacy_policy).click()

    def clk_continue(self):
        self.driver.find_element(By.CSS_SELECTOR, self.click_continue).click()






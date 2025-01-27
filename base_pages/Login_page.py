# This file contains the locators and methods for the Admin login page functionality.
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

class Login_Page:
    # Locators for the login page elements
    textbox_username_id = "loginFrm_loginname"
    textbox_password_id = "loginFrm_password"
    login_btn_xpath = "//button[normalize-space()='Login']"
    account_menu = "//*[@id='main_menu_top']/li[2]"
    account_submenu_logout = "//*[@id='main_menu_top']/li[2]/ul/li[2]"
    account_submenu_login = "//*[@id='main_menu_top']/li[2]/ul/li[1]"


    def __init__(self, driver):
        """
               Constructor to initialize the driver.

               :param driver: WebDriver instance used to interact with the browser.
               """
        self.driver = driver
    # Action methods for interacting with the login page
    def enter_username(self, username):
        """
                Clears the username input field and enters the provided username.

                :param username: The username to input in the username field.
                """
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def enter_password(self, password):
        """
               Clears the password input field and enters the provided password.

               :param password: The password to input in the password field.
               """
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def click_login(self):
        """
                Clicks the login button to attempt login.
                """
        self.driver.find_element(By.XPATH, self.login_btn_xpath).click()

    def log_out(self):
        """
                Clicks the logout button to attempt logout.
                """
        menu = self.driver.find_element(By.XPATH, self.account_menu)
        submenu = self.driver.find_element(By.XPATH, self.account_submenu_logout)
        actions = ActionChains(self.driver).move_to_element(menu)
        actions.perform()
        submenu.click()

    def log_in(self):
        menu = self.driver.find_element(By.XPATH, self.account_menu)
        submenu = self.driver.find_element(By.XPATH, self.account_submenu_login)
        actions = ActionChains(self.driver).move_to_element(menu)
        actions.perform()
        submenu.click()


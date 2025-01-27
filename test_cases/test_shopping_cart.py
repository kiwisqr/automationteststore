# Import necessary modules
import re # Regular expressions module for pattern matching

import pytest
from selenium.webdriver.common.by import By  # Selenium module for locating web elements
from base_pages.Login_page import Login_Page # Import Login_Page class to interact with the login page
from base_pages.Products_page import ProductsPage
from base_pages.Shopping_Cart_page import ShoppingCartPage
from time import sleep
from utilities.read_properties import ReadConfig # Utility to read configuration values (e.g., login info)
from utilities.custom_logger import LogMaker # Custom logger for logging test execution details

class Test_04_Add_to_cart:
    # Read configuration values for login test
    login_page_url = ReadConfig.get_login_page_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = LogMaker.log_gen()

    @pytest.mark.sanity
    @pytest.mark.regression
    # Test case 1: Add to cart
    def test_add_to_cart(self, setup):
        self.driver = setup
        self.driver.get(self.login_page_url)
        self.lp = Login_Page(self.driver)
        self.lp.enter_username(self.username)
        self.lp.enter_password(self.password)
        self.lp.click_login()
        self.p = ProductsPage(self.driver)
        self.p.enter_cheeks_submenu()
        prp_list = self.p.add_items_to_cart()
        self.sc = ShoppingCartPage(self.driver)
        self.sc.click_cart_icon()
        self.sc.add_title_to_list()
        self.p.add_items_to_cart()
        cart_list = self.sc.add_title_to_list()
        assert prp_list == cart_list

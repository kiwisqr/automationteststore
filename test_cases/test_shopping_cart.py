# Import necessary modules

import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from base_pages.Shopping_Cart_page import ShoppingCartPage
from utilities.read_properties import ReadConfig # Utility to read configuration values (e.g., login info)
from utilities.custom_logger import LogMaker # Custom logger for logging test execution details

class Test_04_Cart:
    # Read configuration values for login test
    login_page_url = ReadConfig.get_login_page_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = LogMaker.log_gen()

    @pytest.mark.sanity
    @pytest.mark.regression
    # Test case 1: Add to cart
    def test_add_to_cart(self, logged_in_cheeks_page):
        self.p = logged_in_cheeks_page
        prp_list = self.p.add_items_to_cart()
        self.sc = ShoppingCartPage(self.driver)
        self.sc.click_cart_icon()
        cart_list = self.sc.add_title_to_list()
        assert all(item in cart_list for item in prp_list)

    def test_remove_from_cart(self, logged_in_cheeks_page):
        self.p = logged_in_cheeks_page
        self.p.add_items_to_cart()
        self.sc = ShoppingCartPage(self.driver)
        self.sc.click_cart_icon()
        self.sc.add_title_to_list()
        removed_item = self.sc.click_remove_item()
        updated_cart_list = self.sc.add_title_to_list()
        assert removed_item not in updated_cart_list, f"Item '{removed_item}' was not removed from the cart"
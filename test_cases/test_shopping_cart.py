# Import necessary modules

import pytest
from anyio import sleep
from selenium.webdriver.remote.webdriver import WebDriver

from base_pages.Products_page import ProductsPage
from base_pages.Shopping_Cart_page import ShoppingCartPage
from utilities.read_properties import ReadConfig # Utility to read configuration values (e.g., login info)
from utilities.custom_logger import LogMaker # Custom logger for logging test execution details

@pytest.mark.regression
class TestCart:
    # Read configuration values for login test
    logger = LogMaker.log_gen()

    @pytest.fixture(autouse=True)
    def setup_driver(self, setup):
        self.driver = setup
        self.sc = ShoppingCartPage(self.driver)
        self.page_prod = ProductsPage(self.driver)

    @pytest.fixture
    def add_items_to_cart(self):
        """Adds items to the cart and returns the list of items"""
        self.driver.get("https://automationteststore.com/")
        self.page_prod.enter_cheeks_submenu()
        items_added = self.page_prod.add_items_to_cart()
        yield items_added
        # optional cleanup: remove all items from cart if needed

    @pytest.mark.regression
    def test_add_to_cart(self, add_items_to_cart):
        """Test that added items appear in the cart"""
        self.sc.click_cart_icon()
        cart_list = self.sc.add_title_to_list()
        assert all(item in cart_list for item in add_items_to_cart)

    def test_remove_from_cart(self, add_items_to_cart):
        """Test that removing an item updates the cart"""
        self.sc.click_cart_icon()
        self.sc.add_title_to_list()
        removed_item = self.sc.click_remove_item()
        updated_cart_list = self.sc.add_title_to_list()
        assert removed_item not in updated_cart_list, f"Item '{removed_item}' was not removed from the cart"
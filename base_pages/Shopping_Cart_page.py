# This file contains the locators and methods for the Shopping cart page functionality.
from selenium.webdriver.common.by import By

class ShoppingCartPage:
    # Locators for the shopping cart page elements
    cart_icon = "//*[@id='main_menu_top']/li[3]"
    product_titles= "//*[@class='align_left']/a"

    def __init__(self, driver):
        self.driver = driver

    def click_cart_icon(self):
        self.driver.find_element(By.XPATH, self.cart_icon).click()

    def add_title_to_list(self):
        products = self.driver.find_elements(By.XPATH, self.product_titles)
        cart_list = []
        for product in products:
            text = product.text.lower()
            cart_list.append(text)
        return cart_list

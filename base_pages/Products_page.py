# This file contains the locators and methods for the Products page functionality.
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductsPage:
    # Locators for the create account page elements
    makeup_menu = "//*[@id='categorymenu']/nav/ul/li[3]/a"
    makeup_cheeks_submenu = "//*[@id='categorymenu']/nav/ul/li[3]/div/ul[1]/li[1]/a"
    add_items_cart_buttons = "//div[@class='pricetag jumbotron']/a/i"

    def __init__(self, driver):
        self.driver = driver

    # Action method to get to create account page
    def enter_cheeks_submenu(self):
        menu = self.driver.find_element(By.XPATH, self.makeup_menu)
        submenu = self.driver.find_element(By.XPATH, self.makeup_cheeks_submenu)
        actions = ActionChains(self.driver).move_to_element(menu)
        actions.perform()
        submenu.click()

    def add_items_to_cart(self):
        btns = self.driver.find_elements(By.XPATH, self.add_items_cart_buttons)
        prp_list = []
        for btn in btns:
            text = btn.find_element(By.XPATH, "parent::a/parent::div/parent::div/parent::div/div/div/a").text.lower()
            if "tropiques minerale loose bronzer" in text:
                continue
            else:
                btn.click()
                prp_list.append(text)
        return prp_list









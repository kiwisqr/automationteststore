import pytest

from base_pages.Login_page import Login_Page
from utilities.read_properties import ReadConfig
from utilities.custom_logger import LogMaker
from utilities import excel_utils

class TestLoginDataDriven:

    logger = LogMaker.log_gen()
    path = "E:\\automationteststore\\test_data\\login_data.xlsx"
    status_list = []

    @pytest.fixture(autouse=True)
    def setup_driver(self, setup):
        self.driver = setup
        self.url = ReadConfig.get_login_page_url()
        self.lp = Login_Page(self.driver)

    def test_login_data_driven(self, setup):
        self.logger.info("Verification of valid login data driven")
        self.driver.implicitly_wait(10)
        self.driver.get(self.url)

        self.rows = excel_utils.get_row_count(self.path, "Sheet1")
        #sleep(5)
        print(self.rows)

        for row in range(2, self.rows + 1):
            self.username = excel_utils.read_data(self.path, "Sheet1", row, 1)
            self.password = excel_utils.read_data(self.path, "Sheet1", row, 2)
            self.exp_login = excel_utils.read_data(self.path, "Sheet1", row, 3)

            self.lp.enter_username(self.username)
            self.lp.enter_password(self.password)
            self.lp.click_login()

            act_title = self.driver.title
            exp_title = "My Account"
            if act_title == exp_title:
                if self.exp_login == "Yes":
                    self.logger.info("test data has passed")
                    self.status_list.append("Pass")
                    self.lp.log_out()
                    self.lp.log_in()
                elif self.exp_login == "No":
                    self.logger.info("test data has failed")
                    self.status_list.append("Fail")
                    self.lp.log_out()
                    self.lp.log_in()
            elif act_title != exp_title:
                if self.exp_login == "Yes":
                    self.logger.info("test data has failed")
                    self.status_list.append("Fail")
                elif self.exp_login == "No":
                    self.logger.info("test data has passed")
                    self.status_list.append("Pass")

        print("Status list is:", self.status_list)
        if "Fail" in self.status_list:
            self.logger.info("Test valid login data driven failed")
            assert False
        else:
            self.logger.info("Test valid login data driven passed")
            assert True


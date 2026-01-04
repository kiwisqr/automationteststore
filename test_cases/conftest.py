# Import necessary modules and libraries
from pytest_metadata.plugin import metadata_key # Key for accessing pytest metadata
import pytest # Pytest framework for writing and running tests
from selenium import webdriver # Selenium WebDriver for browser automation
from base_pages.Login_page import Login_Page
from base_pages.Products_page import ProductsPage
from utilities.read_properties import ReadConfig


# Define a pytest command-line option for specifying the browser
def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser: chrome or edge"
    )

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser").lower()

@pytest.fixture()
def setup(browser):
    """ Initialize WebDriver and return it """

    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.maximize_window()
    yield driver     # return driver

    driver.quit()    # closes after test

@pytest.fixture()
def add_items_to_cart(setup):
    # driver1.get(ReadConfig.get_login_page_url())
    # lp = Login_Page(driver1)
    # lp.enter_username(ReadConfig.get_username())  # or fetch from a config
    # lp.enter_password(ReadConfig.get_password())
    # lp.click_login()
    setup.get("https://automationteststore.com/")
    page = ProductsPage(setup)
    page.enter_cheeks_submenu()
    items_added = page.add_items_to_cart()
    # request.cls.driver = driver1
    yield page, items_added



# Add custom metadata to pytest html report
def pytest_configure(config):
    """
        Adds custom metadata to pytest's test report.

        :param config: Pytest's configuration object.
        """
    config.stash[metadata_key]['Project Name'] = 'automationteststore'
    config.stash[metadata_key]['Test Module Name'] = 'Login Tests'
    config.stash[metadata_key]['Tester Name'] = 'Claudia'

# Optional hook to modify pytest metadata
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    """
        Customizes the pytest metadata displayed in the test report.

        :param metadata: Metadata dictionary to modify.
        """
    metadata.pop('Plugins', None)




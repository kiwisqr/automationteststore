# Import necessary modules and libraries
from pytest_metadata.plugin import metadata_key # Key for accessing pytest metadata
import pytest # Pytest framework for writing and running tests
from selenium import webdriver # Selenium WebDriver for browser automation
from base_pages.Login_page import Login_Page
from base_pages.Products_page import ProductsPage
from utilities.read_properties import ReadConfig


# Define a pytest command-line option for specifying the browser
def pytest_addoption(parser):
    """
        Adds a custom command-line option to pytest for specifying the browser to use during tests.

        :param parser: The parser for command-line arguments in pytest.
        """
    parser.addoption(
        "--browser", # The command-line option (e.g., --browser chrome)
        action="store", # Action to store the value of the option
        default="chrome", # Default value if no option is provided
        help="Specify the browser: chrome or edge" # Help text displayed for this option
    )

# Fixture to retrieve the browser option value
@pytest.fixture()
def browser(request):
    """
        Retrieves the browser specified in the pytest command-line arguments.

        :param request: Pytest's built-in request object.
        :return: The browser type specified in the command-line arguments.
        """
    return request.config.getoption("--browser")

# Fixture to set up the WebDriver based on the specified browser
@pytest.fixture()
def setup(browser):
    """
        Initializes the WebDriver based on the specified browser and returns the driver instance.

        :param browser: The browser type (chrome or edge) passed from the command-line arguments.
        :return: An instance of the WebDriver for the specified browser.
        """
    global driver # Declare driver as a global variable
    if browser == "chrome":
        driver = webdriver.Chrome() # Initialize Chrome WebDriver
    elif browser == "edge":
        driver = webdriver.Edge() # Initialize Edge WebDriver
    else:
        # Raise an error if the specified browser is not supported
        raise ValueError("Unsupported browser")
    driver.maximize_window()
    return driver

@pytest.fixture()
def logged_in_cheeks_page(setup, request):
    driver1 = setup
    driver1.get(ReadConfig.get_login_page_url())
    lp = Login_Page(driver1)
    lp.enter_username(ReadConfig.get_username())  # or fetch from a config
    lp.enter_password(ReadConfig.get_password())
    lp.click_login()

    p = ProductsPage(driver1)
    p.enter_cheeks_submenu()
    request.cls.driver = driver1
    return p



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




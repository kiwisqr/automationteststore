# Import the configparser module to read and handle configuration files
import configparser

# Initialize the RawConfigParser to read the configuration file
config = configparser.RawConfigParser()

# Read the configuration file from the specified path
config.read("E:\\automationteststore\\configurations\\config.ini")

# Define the ReadConfig class for fetching configuration values
class ReadConfig:
    """
        A utility class to read configuration values from the config.ini file.
        Each method retrieves a specific value from the configuration file.
        """
    @staticmethod
    def get_login_page_url():
        """
                Reads and returns the login page URL from the configuration file.

                :return: The login page URL as a string.
                """
        login_page_url = config.get('login info', 'login_page_url')
        return login_page_url

    @staticmethod
    def get_username():
        """
                Reads and returns the valid username from the configuration file.

                :return: The valid username as a string.
                """
        username = config.get('login info', 'username')
        return username

    @staticmethod
    def get_password():
        """
                Reads and returns the valid password from the configuration file.

                :return: The valid password as a string.
                """
        password = config.get('login info', 'password')
        return password

    @staticmethod
    def get_invalid_username():
        """
                Reads and returns the invalid username for testing negative scenarios from the configuration file.

                :return: The invalid username as a string.
                """
        invalid_username = config.get('login info', 'invalid_username')
        return invalid_username

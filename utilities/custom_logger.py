# Import the logging module for creating and managing log files
import logging

class LogMaker:
    @staticmethod
    def log_gen():
        """
                Generates and configures a logger for logging test execution details.

                :return: A logger instance configured to write logs to a specific file.
                """
        logging.basicConfig(filename="E:\\automationteststore\\logs\\automationteststore.log", # Path to the log file
                            format = '%(asctime)s:%(levelname)s:%(message)s', # Log format: timestamp, log level, and message
                            datefmt="%Y-%m-%d %H:%M:%S", # Date and time format
                            force=True # Ensures existing loggers are overridden with the new configuration
                            )

        # Get a logger instance
        logger = logging.getLogger()

        # Set the default logging level to INFO
        logger.setLevel(logging.INFO)

        # Return the configured logger instance
        return logger
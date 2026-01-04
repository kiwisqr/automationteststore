# Import the logging module for creating and managing log files
import logging

class LogMaker:
    @staticmethod
    def log_gen():
        """
                Generates and configures a logger for logging test execution details.

                :return: A logger instance configured to write logs to a specific file.
                """
        # Create logs directory inside the project/workspace
        log_dir = os.path.join(os.getcwd(), "logs")
        os.makedirs(log_dir, exist_ok=True)

        # Log file path
        log_file = os.path.join(log_dir, "automationteststore.log")

        logging.basicConfig(
            filename=log_file,
            format="%(asctime)s:%(levelname)s:%(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
            force=True
        )

        # Get a logger instance
        logger = logging.getLogger()

        # Set the default logging level
        logger.setLevel(logging.INFO)

        return logger
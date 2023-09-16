import logging

class LogWriter:
    def __init__(self, log_level: int):
        """
        Initialize the LogWriter instance.

        Args:
            log_level (int): The logging level for messages to be written.
        """

        self.log_level = log_level

    def write(self, message: str):
        """
        Write a log message.

        Args:
            message (str): The log message to be written.

        Notes:
            This method is called when using the `print()` function.
        """

        if message.strip():  # do not log empty lines
            logging.log(self.log_level, message.strip())

    def flush(self):
        """
        Flush the log writer.
        """

        pass 
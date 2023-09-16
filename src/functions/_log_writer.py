import logging

class LogWriter:
    def __init__(self, log_level):
        self.log_level = log_level

    def write(self, message):
        if message.strip():  # do not log empty lines
            logging.log(self.log_level, message.strip())

    def flush(self):
        pass 
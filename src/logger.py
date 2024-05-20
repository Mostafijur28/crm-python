import logging

class Logger:
    def __init__(self, log_file='workflow.log'):
        logging.basicConfig(filename=log_file, level=logging.INFO)

    def log(self, message):
        logging.info(message)
        print(message)

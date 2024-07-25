import logging

# Configuring the logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Creating a handler to write logs to a file
file_handler = logging.FileHandler('my-log-file.log')
file_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# Creating a handler to write logs to the console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# Writing the log
logger.info('Hello, Members!')
logger.debug('Debug message.')
logger.warning('Warning message.')
logger.error('Error message.')

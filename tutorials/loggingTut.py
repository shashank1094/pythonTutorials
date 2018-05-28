# Using Python's standard logging module
# Link to the tutorial is here :
# https://fangpenlin.com/posts/2012/08/26/good-logging-practice-in-python/
# and
# https://docs.python.org/3.6/library/logging.html
import logging

# logging.basicConfig(level=logging.INFO)
# # logging.basicConfig(level=logging.DEBUG)
# logger = logging.getLogger(__name__)
# logger.info('Start reading database')
# # read database here
# records = {'john': 55, 'tom': 66}
# logger.debug('Records: %s', records)
# logger.info('Updating records ...')
# # update records here
# logger.info('Finish updating records')

logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)
logger.setLevel(logging.DEBUG)
# create a file handler
handler = logging.FileHandler('loggingTutLogs.txt')
handler.setLevel(logging.DEBUG)
# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(module)s - %(message)s')
handler.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(handler)
logger.info('Hello baby')
logger.info('Start reading database')
# read database here
records = {'john': 55, 'tom': 66}
logger.debug('Records: %s', records)
logger.info('Updating records ...')
# update records here
logger.info('Finish updating records')


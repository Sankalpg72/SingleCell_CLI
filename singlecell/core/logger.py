import logging 
import sys

FILE_LOG = 'C:\\Users\\sanka\\Desktop\\SingleCell_CLI\\singlecell\\pipeline.log'

logger = logging.getLogger()
logger.setLevel(level = logging.DEBUG)

stream_handler = logging.StreamHandler(sys.stdout)
stream_formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
stream_handler.setFormatter(stream_formatter)
logger.addHandler(stream_handler)


file_handler = logging.FileHandler(FILE_LOG)
file_formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


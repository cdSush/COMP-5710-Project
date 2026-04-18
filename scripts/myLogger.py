# scripts/myLogger.py
import logging
import os

def giveMeLoggingObject():

    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, 'PROJECT-LOGGER.log')

    format_str = '%(asctime)s:%(message)s'
    #file_name  = 'PROJECT-LOGGER.log'
    ### creates one Global logger: logging.basicConfig
    logging.basicConfig(format=format_str, filename=file_path, level=logging.INFO, force=True)
    loggerObj = logging.getLogger('simple-logger')
    return loggerObj

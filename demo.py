from visa_prediction_system.logger import logging
from visa_prediction_system.exception import VisaException
import sys


logging.info("Welcome to our Custome log")


try:
    a=2/0
    
except Exception as e:
    raise VisaException(e, sys) 
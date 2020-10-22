import logging
import inspect

def getCustomerLogger(level):
    loggername = inspect.stack()[1][3]
    logger = logging.getLogger(loggername)
    logger.setLevel(level)
    fileHandler = logging.FileHandler("C:/Users/Ram/Desktop/nopecommerceApp/Logs/Automation.log",mode='a')
    fileHandler.setLevel(level)
    formatter = logging.Formatter("%(asctime)s-%(name)s-%(levelname)s-%(message)s",datefmt="%m-%d-%Y %H:%M:%S")
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)
    return logger

import logging
from logging.config import fileConfig


def get_logger(module_name):
    fileConfig('../logging.conf', disable_existing_loggers=False)
    logger = logging.getLogger("ApartmentApplication").getChild(module_name)
    return logger

import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(name)s] [%(levelname)s] %(message)s')


def get_logger(name=__name__):
    logger = logging.getLogger(name)
    return logger

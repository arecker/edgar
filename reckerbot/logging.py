import logging
import sys


def _make_logger(level=logging.INFO):
    logger = logging.getLogger('reckerbot')
    logger.setLevel(level)
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(level)
    formatter = logging.Formatter('%(levelname)s: %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


logger = _make_logger()

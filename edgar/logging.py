import logging
import sys


def _make_logger(level=logging.CRITICAL):
    logger = logging.getLogger('edgar')
    logger.setLevel(level)
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('%(levelname)s: %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


logger = _make_logger()

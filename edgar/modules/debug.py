"""
advanced debugging features
"""

import logging

from edgar import logger, Module


module = Module('debug')

_log_levels = {
    'debug': logging.DEBUG,
    'warning': logging.WARNING,
    'info': logging.INFO,
    'critical': logging.CRITICAL
}


@module.register
def log(level):

    """set the logging level"""

    choice = _log_levels[level.lower()]

    logger.info('setting log level to %s', level.lower())
    logger.setLevel(choice)


@module.register
def ping():
    print('pong')

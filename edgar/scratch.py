from . import logger


def scratch_logging():
    logger.debug('this is a debug message')
    logger.info('this is an info message')
    logger.warn('this is an warning message')
    logger.error('this is an error message')
    logger.critical('this is a critical message')
    try:
        int('fish')
    except Exception:
        logger.exception('this is an exception')


def main():
    logger.info('running scratch_logging')
    scratch_logging()

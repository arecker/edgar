"""
root edgar module
"""
from edgar import logger, Module


module = Module('edgar')


@module.register
def ping():
    """
    prints the word 'pong'
    """
    print('pong')


@module.register
def logging(option=''):
    """
    toggle logging level
    """
    if not option:
        print('please specify logging level')
    elif option == 'debug':
        print('setting logging level to DEBUG')
        logger.setLevel(logging.DEBUG)
    elif option == 'info':
        print('setting logging level to info')
        logger.setLevel(logging.INFO)
    elif option in ['off', 'critical', 'false']:
        print('disabling logger')
        logger.setLevel(logging.CRITICAL)

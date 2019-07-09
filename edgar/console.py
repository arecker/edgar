"""
supports the edgar console interface
"""

import re

from edgar import logger, load_module


def main(name='edgar'):
    """
    launches an edgar console session, loading module <name>
    """
    logger.info('loading module %s', name)
    module = load_module(name)
    prompt = f'{name.upper()}> '

    while True:
        command, args = _sanitize_input(input(prompt))

        if command == 'exit':
            logger.debug('exit called, leaving %s', name)
            break
        
        logger.debug('calling command %s with args %s', command, args)
        module.manifest[command](*args)


def _sanitize_input(response):
    logger.debug('received raw response: %s', response)

    # normalize casing
    response = response.lower()

    # remove everything that's not a-z, a space, or comma
    response = re.compile('[^a-z, ]').sub('', response)

    # separate command name from args
    response = response.split(' ')
    command, args = response[0].strip(), response[1:]

    return command, [arg.strip() for arg in args]

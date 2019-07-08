import re

from edgar import logger, load_module


def run(name='edgar'):
    logger.info('loading module %s', name)
    module = load_module(name)
    module.help()

    while True:
        response = _sanitize_input(input(module.console_prompt()))
        logger.debug('received response: %s', response)
        function, args = response[0], response[1:]
        logger.debug('calling function %s with args %s', function, args)
        module.manifest[function](*args)


def _sanitize_input(response):
    regex = re.compile('[^a-zA-Z\, ]')
    cleaned = regex.sub('', response)

    if ',' in cleaned:
        arglist = cleaned.split(',')
    else:
        arglist = [cleaned]

    return [arg.lower() for arg in arglist]

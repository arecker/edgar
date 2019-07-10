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
    logger.debug('setting prompt to %s', prompt)

    logger.debug('building help text from manifest %s', module.manifest)
    help_msg = _manifest_to_help_text(module.manifest)

    while True:
        command, args = _sanitize_input(input(prompt))

        if command == 'exit':
            logger.debug('exit called, leaving %s', name)
            break
        elif command == 'reload':
            module = load_module(name)
        elif command == 'help':
            print(help_msg)
        else:
            try:
                logger.debug('calling command %s with args %s', command, args)
                load_module(name).manifest[command](*args)
            except KeyError:
                print(f'Unrecognized command: {command}')
                print(help_msg)


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


def _manifest_to_help_text(manifest):
    commands = dict([
        (command, (func.__doc__ or '').strip())
        for command, func
        in manifest.items()
    ])

    commands.update({
        'exit': 'exit the current module',
        'help': 'show available commands',
        'reload': 'reload the current module',
    })

    output = '\n'.join([
        f'{command.ljust(20)} {docstring.ljust(20)}'
        for command, docstring
        in sorted(commands.items(), key=lambda t: t[0])
    ])

    return f'Available Commands:\n{output}'

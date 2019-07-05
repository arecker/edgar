import subprocess

from . import logger


def run(cmd):
    logger.debug('running shell command %s', cmd)

    try:
        cmd_list = cmd.split(' ')
        output = subprocess.run(cmd_list, capture_output=True, check=True)
        msg = 'command %s succeeded: %s'
        logger.debug(msg, cmd, output.stdout.decode('utf-8').strip())
    except subprocess.CalledProcessError as e:
        msg = 'command %s returned an error (%d): %s'
        logger.error(msg, cmd, e.returncode, e.stderr.decode('utf-8').strip())
        output = e

    return [
        output.returncode,
        output.stdout.decode('utf-8'),
        output.stderr.decode('utf-8')
    ]

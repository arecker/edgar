from os import environ

API_TOKEN = environ['SLACK_TOKEN']
ERRORS_TO = 'alex'

PLUGINS = [
    'reckerbot.plugins',
]

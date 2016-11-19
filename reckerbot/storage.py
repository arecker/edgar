import re

from slackbot.bot import respond_to
from slacker import Slacker
from hurry.filesize import size

from reckerbot import NON_BOT_API_TOKEN


slacker = Slacker(NON_BOT_API_TOKEN)


def get_file_count():
    response = slacker.files.list(count=0)
    return response.body['paging']['total']


def get_files():
    response = slacker.files.list(count=get_file_count())
    return response.body['files']


def get_sorted_files(biggest_to_smallest=True):
    files = get_files()
    files.sort(key=lambda f: f['size'], reverse=biggest_to_smallest)
    return files


def display_file(message, file):
    message.reply('\n'.join([
        '*{}* - {}'.format(file['title'], size(file['size'])),
        file['permalink']
    ]))


@respond_to('count files|count the files', re.IGNORECASE)
def count_files(message):
    count = get_file_count()

    if count is 1:
        message.reply('We have 1 file'.format(count))
    else:
        message.reply('We have {} files'.format(count))


@respond_to('biggest file', re.IGNORECASE)
def biggest_file(message):
    files = get_sorted_files(biggest_to_smallest=True)
    display_file(message, files[0])


@respond_to('smallest file', re.IGNORECASE)
def smallest_file(message):
    files = get_sorted_files(biggest_to_smallest=False)
    display_file(message, files[0])


@respond_to('total file size|total file usage|total storage', re.IGNORECASE)
def total_usage(message):
    message.reply(
        '{} files are taking up about {}'.format(
            get_file_count(),
            size(sum(f['size'] for f in get_files()))
        )
    )

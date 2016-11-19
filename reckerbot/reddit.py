import re

from slackbot.bot import respond_to
import praw


reddit = praw.Reddit(user_agent='recker')


@respond_to('subreddit (.*)', re.IGNORECASE)
def count_files(message, query):
    try:
        reddit.get_subreddit(query).fullname
        message.reply('https://reddit.com/r/{}'.format(query))
    except praw.errors.InvalidSubreddit:
        message.reply('No subreddit "{}"'.format(query))

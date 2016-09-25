import re

from slackbot.bot import respond_to
from bs4 import BeautifulSoup
import requests


@respond_to('search for (.*)', re.IGNORECASE)
def search(message, query):
    response = requests.get('http://duckduckgo.com/html/', {'q': query})
    soup = BeautifulSoup(response.content, "html.parser")
    results = soup.find_all('a', {'class': 'result__a'})

    try:
        link = results[0].attrs['href']
        message.reply('Here\'s what I found\n{}'.format(link))
    except IndexError:
        message.reply('Found no results for "{}"'.format(query))

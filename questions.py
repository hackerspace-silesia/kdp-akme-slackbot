from slackbot.bot import respond_to
from pprint import pformat
from wit import Wit

import re
import os

access_token = os.environ.get('WIT_ACCESS_TOKEN')
wit = Wit(access_token)


@respond_to('(.*)', re.IGNORECASE)
#@listen_to('(.*)', re.IGNORECASE)
def hi(message, query):
    message.react('+1')
    query = query.strip()
    try:
        response = wit.message(query, verbose=True)
    except Exception as e:
        print(e)
        message.reply('eh :(')
    else:
        entities = pformat(response['entities'])
        message.reply('```%s```' % entities)

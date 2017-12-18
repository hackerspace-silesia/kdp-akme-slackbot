from slackbot.bot import respond_to
from slackbot.bot import listen_to
import re


@respond_to('co +to +jest (.*)', re.IGNORECASE)
def hi(message, query):
    message.reply(query)
    message.react('+1')


@respond_to('czym +jest +(.*)', re.IGNORECASE)
def hi(message, query):
    message.reply(query)
    message.react('+1')


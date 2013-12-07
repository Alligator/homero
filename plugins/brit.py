import random
from util import hook, http
from twython import Twython
from lxml import html
from time import sleep

token = None

def init(key, secret):
  global token
  if not token:
    token = Twython(key, secret, oauth_version=2).obtain_access_token()

@hook.command
def brit(inp, bot=None, say=None):
  global token
  init(bot.config['api_keys']['twitter_key'], bot.config['api_keys']['twitter_secret'])
  twitter = Twython(bot.config['api_keys']['twitter_key'], access_token=token)
  j = [t['text'] for t in twitter.get_user_timeline(screen_name='SoVeryBritish', count=100) if 'http' not in t['text'] and '#' not in t['text']]
  tweet = random.choice(j)
  say(tweet)

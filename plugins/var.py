from util import hook, http
import random
from twython import Twython

token = None

def init(key, secret):
  global token
  if not token:
    token = Twython(key, secret, oauth_version=2).obtain_access_token()

def get_tweets(key):
  twitter = Twython(key, access_token=token)
  j = twitter.search(q='game rumor')
  return j['statuses']

@hook.command
def var(inp, bot=None, say=None):
  init(bot.config['api_keys']['twitter_key'], bot.config['api_keys']['twitter_secret'])
  tweets = [i['text'] for i in get_tweets(bot.config['api_keys']['twitter_key'])]# if '@' not in i['text']]
  print tweets
  t = random.choice(tweets)
  if t.lower().startswith('rumor'):
    t = t[5:].strip()
  say('<Var>: %s' % t)

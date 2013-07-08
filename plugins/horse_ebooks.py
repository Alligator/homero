from util import hook, http
import time
from twython import Twython

token = None

def init(key, secret):
  global token
  if not token:
    token = Twython(key, secret, oauth_version=2).obtain_access_token()

def get_tweet(key):
  twitter = Twython(key, access_token=token)
  j = twitter.get_user_timeline(screen_name='Horse_ebooks', count=2)
  return j[0]['text'].replace('\n', ' ')

last = time.time()
last_tweet = ''
# last_tweet = get_tweet()

@hook.event('*')
def horse(inp, bot=None, conn=None):
  global last, url, last_tweet
  init(bot.config['api_keys']['twitter_key'], bot.config['api_keys']['twitter_secret'])
  if time.time() - last > 240:
    last = time.time()
    tweet = get_tweet(bot.config['api_keys']['twitter_key'])
    if tweet == last_tweet:
      return
    if 't.co' in tweet:
      return
    conn.cmd('PRIVMSG #sa-minecraft Horse_ebooks: %s' % tweet)
    last_tweet = tweet

@hook.command('horse', autohelp=False)
def horse_cmd(inp, bot=None, say=None):
  global url, last, last_tweet
  init(bot.config['api_keys']['twitter_key'], bot.config['api_keys']['twitter_secret'])
  if time.time() - last > 120:
    last = time.time()
    last_tweet = get_tweet(bot.config['api_keys']['twitter_key'])
  say('Horse_ebooks: %s' % last_tweet)

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
def vice(inp, bot=None, say=None):
  if random.random() > 0.5:
    h = http.get_xml('http://www.vice.com/rss')
    item = random.choice(h.xpath('//item'))
    say(item.xpath('title')[0].text)
    sleep(20)
    say('that vice was real - ' + item.xpath('link')[0].text)
  else:
    global token
    init(bot.config['api_keys']['twitter_key'], bot.config['api_keys']['twitter_secret'])
    twitter = Twython(bot.config['api_keys']['twitter_key'], access_token=token)
    j = twitter.get_user_timeline(screen_name='Vice_Is_Hip', count=100)
    tweet = random.choice(j)
    say(tweet['text'])
    sleep(20)
    say('that vice was fake - ' + 'https://twitter.com/UpWorthIt/status/' + tweet['id_str'])

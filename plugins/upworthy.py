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
def upworthy(inp, bot=None, say=None):
  if random.random() > 0.5:
    h = http.get_html('http://www.upworthy.com/random')
    say(h.xpath('//*[@id="pagetitle"]/header/h1')[0].text)
    url = h.xpath('/html/head/link[6]')[0].attrib['href']
    sleep(20)
    say('that upworthy was real - ' + url)
  else:
    global token
    init(bot.config['api_keys']['twitter_key'], bot.config['api_keys']['twitter_secret'])
    twitter = Twython(bot.config['api_keys']['twitter_key'], access_token=token)
    j = twitter.get_user_timeline(screen_name='UpWorthIt', count=100)
    tweet = random.choice(j)
    say(tweet['text'])
    sleep(20)
    say('that upworthy was fake - ' + 'https://twitter.com/UpWorthIt/status/' + tweet['id_str'])

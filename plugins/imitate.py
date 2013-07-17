import random
import string
import re
import time

from collections import defaultdict
from random import choice
from urllib2 import HTTPError, unquote
from twython import Twython

from util import hook, http

cache = {}

token = None

def init(key, secret):
  global token
  if not token:
    token = Twython(key, secret, oauth_version=2).obtain_access_token()

def get_tweets(key, name):
  twitter = Twython(key, access_token=token)
  return twitter.get_user_timeline(screen_name=name, count=200)


def get_cached(name, bot):
  global imi_cache
  init(bot.config['api_keys']['twitter_key'], bot.config['api_keys']['twitter_secret'])
  if name in cache and time.time() - cache[name][0] + 60 * 60 * 24 > 0:
    print name, 'in cache'
    return cache[name][1]
  text = '. '.join([t['text'] for t in get_tweets(bot.config['api_keys']['twitter_key'], name)]) + '.'
  cache[name] = (time.time(), text)
  print name, 'not in cache'
  return text

@hook.command
def imitate(inp, bot=None):
  ".imitate <account> -- use a markov text generator to imiatate a twitter account"
  text = ''
  for name in inp.split():
    try:
      text += get_cached(name, bot)
    except HTTPError, e:
      if e.code == 404:
        return "user not found"
      else:
        print e.code
        return

  # remove weird characters
  text = re.sub('\t+|\n+', ' ', text)
  text = ''.join([c.lower() for c in text if c in string.printable])

  words = text.split()
  prev = words[0]
  buff = []
  chain = defaultdict(lambda: defaultdict(set))

  for i, word in enumerate(words[1:]):
    if '#' in word or '@' in word or 'http' in word:
      continue
    prev2 = tuple(buff[-2:])
    if word[-1] in '.!?':
      chain[word][None].add(0)
      buff = []
      prev = word[:-1]
    else:
      chain[prev][word].add(prev2)
      buff.append(word)
      prev = word

  word = choice(chain.keys())
  output = []
  while True:
    output.append(word)
    nxt = ''
    k = []
    for poss, hist in chain[word].items():
      n = [x for x in hist if x == tuple(output[-2:])]
      if n:
        k.append(poss)
    if len(k) > 0:
      nxt = choice(k)
    else:
      if chain[word]:
        nxt = choice(chain[word].keys())
      else:
        break
    word = nxt
    if not word:
      break
  return ' '.join(output)


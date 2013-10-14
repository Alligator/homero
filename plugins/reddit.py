import simplejson as json
import random
from util import hook
from util import http

@hook.command
def city(inp):
  jsonData = http.get_json('http://www.reddit.com/r/cityporn/.json')
  j= random.choice(jsonData['data']['children'])['data']
  return j['title'] + ' ' + j['url']

@hook.command
def danl(inp, say=None):
  subreddit = [
    "TheRedPill",
    'seduction',
    'CuckoldCommunity',
  ]
  jsonData = http.get_json('http://www.reddit.com/r/' + random.choice(subreddit) + '/.json')
  say('<danl> ' + random.choice(jsonData['data']['children'])['data']['title'].lower())

@hook.command
def hitze(inp, say=None):
  hitzelist = [
    "ahahaaha",
    "lol",
    "heh",
    "omg.",
    "uugh",
    "why..",
    "lol pcgaming",
    "rip",
    "sperg",
    "omg hyle",
  ]

  subreddit = [
    "pics",
    "wtf",
    "cityporn",
    "gaming",
    "minecraftcirclejerk",
    "gifs",
    "nba",
  ]

  noSelf = False
  while noSelf == False:
    jsonData = http.get_json('http://www.reddit.com/r/' + random.choice(subreddit) + '/.json')
    potentialURL = random.choice(jsonData['data']['children'])['data']['url']
    if 'reddit' in potentialURL:
      noSelf = False
    else:
      noSelf = True

  say("<hitz> " + potentialURL + " " + random.choice(hitzelist))

@hook.command
def var(inp, say=None):
  subreddit =  [
    'Games',
  ]
  jsonData = http.get_json('http://www.reddit.com/r/' + random.choice(subreddit) + '/search.json?q=rumors&restrict_sr=on&sort=new')
  say('<Var> ' + random.choice(jsonData['data']['children'])['data']['title'].lower())

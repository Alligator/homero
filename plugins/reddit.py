import simplejson as json
import random
from util import hook
from util import http

@hook.command
def alligator(inp, say=None):
  subreddit =  [
    'britishproblems',
  ]
  jsonData = http.get_json('http://www.reddit.com/r/' + random.choice(subreddit) + '/.json')
  say('<@alligator> ' + http.unescape(random.choice(jsonData['data']['children'])['data']['title'].lower()))

@hook.command
def city(inp):
  jsonData = http.get_json('http://www.reddit.com/r/cityporn/.json')
  j= http.unescape(random.choice(jsonData['data']['children'])['data'])
  return j['title'] + ' ' + j['url']

@hook.command
def ghost(inp, say=None):
  subreddit = [
    'dungeonsanddragons',
  ]
  jsonData = http.get_json('http://www.reddit.com/r/' + random.choice(subreddit) + '/.json')
  say('<Ghoster> ' + http.unescape(random.choice(jsonData['data']['children'])['data']['title'].lower()))

@hook.command
def hurt(inp, say=None):
  subreddit = [
    'Buddhism',
    'explainlikeimfive',
    'gifs',
    'Eve',
    'weightlifting',
    'MensRights',
    'hardbodies',
    'DoesAnybodyElse',
  ]
  jsonData = http.get_json('http://www.reddit.com/r/' + random.choice(subreddit) + '/.json')
  say('<Hurt> ' + http.unescape(random.choice(jsonData['data']['children'])['data']['title'].lower()))

@hook.command
def danl(inp, say=None):
  subreddit = [
    'TheRedPill',
    'seduction',
    'CuckoldCommunity',
    'BikePorn',
    'electronic_cigarette',
  ]
  jsonData = http.get_json('http://www.reddit.com/r/' + random.choice(subreddit) + '/.json')
  say('<danl> ' + http.unescape(random.choice(jsonData['data']['children'])['data']['title'].lower()))

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

  say("<hitz> " + potentialURL + " " + http.unescape(random.choice(hitzelist)))

@hook.command
def var(inp, say=None):
  subreddit =  [
    'Games',
  ]
  jsonData = http.get_json('http://www.reddit.com/r/' + random.choice(subreddit) + '/search.json?q=rumors&restrict_sr=on&sort=new')
  say('<Var> ' + http.unescape(random.choice(jsonData['data']['children'])['data']['title'].lower()))


@hook.command(autohelp=False)
def movietime(inp):
  ".movietime <query> -- return a random movie from r/fullmoviesonyoutube or search if you supply a query"
  if inp:
    jsonData = http.unescape(http.get_json('http://www.reddit.com/r/fullmoviesonyoutube/search.json?q={}&restrict_sr=on&sort=new&limit=1'.format(inp)))
    try:
      movie = jsonData['data']['children'][0]['data']
    except IndexError, e:
      return 'no results'
  else:
    jsonData = http.get_json('http://www.reddit.com/r/fullmoviesonyoutube.json')
    movie = http.unescape(random.choice(jsonData['data']['children'])['data'])
  return movie['title'] + ' ' + movie['url']

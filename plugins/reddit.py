import simplejson as json
import random
import time
from util import hook
from util import http

queue = {}

def reddit_get(subreddit):
  if subreddit not in queue or len(queue[subreddit]['posts']) == 0 or time.time() - queue[subreddit]['time'] > 400:
    jsonData = http.get_json('http://www.reddit.com/r/' + subreddit + '/.json')
    queue[subreddit] = {
        'posts': [http.unescape(d['data']['title'].lower()) for d in jsonData['data']['children']],
        'time': time.time()
    }
  p = queue[subreddit]['posts']
  c = random.choice(p)
  p.remove(c)
  return c

@hook.command
def alligator(inp, say=None):
  say('<@alligator> ' + reddit_get('britishproblems'))

@hook.command
def city(inp):
  return reddit_get('cityporn')

@hook.command
def ghost(inp, say=None):
  say('<Ghosters> ' + reddit_get('fatpeoplestories'))

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
  say('<Hurt> ' + reddit_get(random.choice(subreddit)))

@hook.command
def danl(inp, say=None):
  subreddit = [
    'TheRedPill',
    'seduction',
    'CuckoldCommunity',
    'BikePorn',
    'electronic_cigarette',
  ]
  say('<danl> ' + reddit_get(random.choice(subreddit)))

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
  say('<Var> ' + reddit_get(random.choice(subreddit)))


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
    movie = random.choice(jsonData['data']['children'])['data']
  return http.unescape(movie['title'] + ' ' + movie['url'])

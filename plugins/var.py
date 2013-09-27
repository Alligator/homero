from util import hook, http
import random

@hook.command
def var(inp, say=None):
  subreddit =  [
    'Games',
  ]
  jsonData = http.get_json('http://www.reddit.com/r/' + random.choice(subreddit) + '/search.json?q=rumors&restrict_sr=on&sort=new')
  say('<Var> ' + random.choice(jsonData['data']['children'])['data']['title'].lower())

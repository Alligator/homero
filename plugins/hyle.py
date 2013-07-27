import simplejson as json
import random
from util import hook
from util import http

subreddits = []
subreddits = open('plugins/hyle.txt').read().splitlines()

def write():
  open('plugins/hyle.txt', 'w').writelines([n + '\n' for n in subreddits])

@hook.command
def delhyle(inp, nick=None):
  global subreddits
  if nick != 'hyle':
    return
  if inp in subreddits:
    subreddits.remove(inp)
    write()
    return 'removed r/' + inp
  else:
    return 'not there mate'

@hook.command
def addhyle(inp, nick=None):
  global subreddits
  if nick != 'hyle':
    return
  try :
    j = http.get_json('http://reddit.com/r/' + inp + '.json')
  except ValueError, e:
    return 'not a subreddit mate'
  if inp not in subreddits:
    subreddits.append(inp)
    write()
    return 'added r/' + inp
  else:
    return 'already in the list mate'

@hook.command
def listhyle(inp):
  return ''.join(subreddits)

@hook.command
def hyle(inp, say=None):
  global subreddits

  jsonData = http.get_json('http://www.reddit.com/r/' + random.choice(subreddits) + '/.json')
  say('<hyle> ' + random.choice(jsonData['data']['children'])['data']['title'].lower())

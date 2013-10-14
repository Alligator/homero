from util import hook
from random import choice
import string
import urllib2

@hook.command
def puush(inp):
  url = 'http://puu.sh/{}'
  for i in range(5):
    x = str(choice(range(1, 4)))
    x += choice(list(string.ascii_uppercase))
    x += ''.join([choice(string.ascii_letters) for i in range(3)])
    u = url.format(x)
    if check_puush(u):
      return u
  return "didn't find one in 5 attempts :("
  # http://puu.sh/4DQRH

def check_puush(url):
  try:
    txt = urllib2.urlopen(url).read(2)
    return True
  except urllib2.HTTPError:
    return False

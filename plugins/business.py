from util import hook
import requests
from random import choice
import re

bidness = open('plugins/business.txt', 'Ur').readlines()

@hook.command
def business(inp, say=None):
  man = requests.get('http://realbusinessmen.com/random').url
  words = re.sub('\n', '', choice(bidness))
  say(man)
  say('"' + words + '"')

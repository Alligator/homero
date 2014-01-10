from util import hook
import requests

@hook.command('gad')
@hook.command
def dog(inp):
  return requests.get('http://goodassdog.tumblr.com/random').url

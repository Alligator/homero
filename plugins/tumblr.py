from util import hook
import requests

@hook.command('gad')
@hook.command
def dog(inp):
  return requests.get('http://goodassdog.tumblr.com/random').url

@hook.command
def realbusinessmen(inp):
  return requests.get('http://realbusinessmen.com/random').url

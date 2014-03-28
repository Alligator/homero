from util import hook, http
import requests
from cgi import escape
import time
import json

streaming = False

def check_stream():
  j = http.get_json('https://api.twitch.tv/kraken/streams/breadcrew')
  return bool(j['stream'])

@hook.event('*', limit=2)
def stream(inp, conn=None):
  global streaming
  s = check_stream()
  if s and not streaming:
    streaming = True
    conn.cmd('privmsg #sa-minecraft \x0313someone started streaming http://stream.alligatr.co.uk/')
  elif not s and streaming:
    streaming = False

def channelupdate(params, bot):
  params['oauth_token'] = bot.config['api_keys']['twitch']
  url = 'https://api.twitch.tv/kraken/channels/breadcrew'
  resp = requests.put(url, data=params)
  if resp.status_code == 200:
    return 'channel info updated'
  else:
    return 'uh oh something went wrong ' + str(resp.status_code)

@hook.command(limit=5)
@hook.command('strgame')
def setgame(inp, chan=None, bot=None):
  if chan != '#sa-minecraft':
    return
  params = { 'channel[game]': inp }
  return channelupdate(params, bot)

@hook.command(limit=5)
@hook.command('strtitle')
def settitle(inp, chan=None, bot=None):
  if chan != '#sa-minecraft':
    return
  params = { 'channel[status]': inp }
  return channelupdate(params, bot)

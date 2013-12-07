from util import hook, http
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
    open('/var/www/stream.alligatr.co.uk/stream.json', 'w').write(json.dumps({'msg':''}))

@hook.command('stream')
def streamcmd(inp, chan=None, nick=None):
  if inp and chan == '#sa-minecraft' and len(inp) < 100:
    open('/var/www/stream.alligatr.co.uk/stream.json', 'w').write(json.dumps({'msg':escape(inp)}))
    return 'stream title set: http://stream.alligatr.co.uk'
  s = check_stream()
  if s:
    return '\x0313someone is streaming http://stream.alligatr.co.uk/'
  else:
    return 'no-one is streaming'

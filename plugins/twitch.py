from util import hook, http
from cgi import escape
import time
import random
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
    if random.random() > 0.9:
      conn.cmd('privmsg #sa-minecraft \x0313someone started screaming http://scream.alligatr.co.uk/')
    else:
      conn.cmd('privmsg #sa-minecraft \x0313someone started streaming http://stream.alligatr.co.uk/')
  elif not s and streaming:
    streaming = False

@hook.command('stream')
def streamcmd(inp, chan=None):
  if inp and chan == '#sa-minecraft' and len(inp) < 50:
    open('/var/www/stream.alligatr.co.uk/stream.json', 'w').write(json.dumps({'msg':escape(inp)}))
    return 'stream title set: http://stream.alligatr.co.uk'
  s = check_stream()
  t = 'streaming' if random.random() > 0.1 else 'screaming'
  if s:
    return '\x0313someone is '+t+' http://'+t[:6]+'.alligatr.co.uk/'
  else:
    return 'no-one is '+t

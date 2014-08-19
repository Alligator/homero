from util import hook

import requests
import re

@hook.command(limit=1, autohelp=False)
def yo(inp, chan=None, bot=None):
  ".yo [username] [link] -- annoy everyone. (send a yo to HOMERYO to subscribe)."
  # if chan != '#sa-minecraft':
  #   return
  url = "http://api.justyo.co/yoall/"
  if inp == '':
    params = { 'api_token': bot.config['api_keys']['yo'] }
  else:
    sp = inp.split(' ')
    if len(sp) == 2 and sp[1].startswith('http'):
      params = { 'link': sp[1], 'username': sp[0], 'api_token': bot.config['api_keys']['yo'] }
      url = "http://api.justyo.co/yo/"
    elif len(sp) == 1:
      params = { 'link': sp[0], 'api_token': bot.config['api_keys']['yo'] }
    else:
      return yo.__doc__
  # if inp == '':
  #   url = "http://api.justyo.co/yoall/"
  # else:
  #   url = "http://api.justyo.co/yo/"
  #   params['username'] = inp
  resp = requests.post(url, data=params)
  if resp.status_code != 201 and resp.status_code != 200:
    return 'uh oh something went wrong (api returned {})'.format(resp.status_code)
  else:
    return 'Yo'

@hook.event('*', limit=1)
def checkyo(paraml, conn=None):
  log = open('/tmp/yo.log', 'r').readlines()
  for line in log:
    m = re.search(r'name=(.*) ', line)
    if m:
      name = m.group(1)
      conn.cmd('privmsg #sa-minecraft Yo from ' + name)
  open('/tmp/yo.log', 'w').close() # clear the file

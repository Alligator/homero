from util import hook

import requests
import re

@hook.command(limit=1, autohelp=False)
def yo(inp, chan=None, bot=None):
  ".yo -- annoy everyone. (send a yo to HOMERYO to subscribe)."
  if chan != '#sa-minecraft':
    return
  params = { 'api_token': bot.config['api_keys']['yo'] }
  if inp == '':
    url = "http://api.justyo.co/yoall/"
  else:
    url = "http://api.justyo.co/yo/"
    params['username'] = inp
  resp = requests.post(url, data=params)
  if resp.status_code != 201:
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

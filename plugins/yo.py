from util import hook

import requests
import re
import urlparse
import json

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

latlngcache = {}

@hook.event('*', limit=1)
def checkyo(paraml, conn=None, bot=None):
  global latlngcache
  log = open('/tmp/yo.log', 'r').readlines()
  msg = ''
  for line in log:
    m = re.search(r'name=(.*) ', line)
    if m:
      name = m.group(1)
      if '&' in name:
        name, query = name.split('&')
        query = urlparse.parse_qs(query)
        if 'location' in query:
          if query['location'][0] in latlngcache:
            addr = latlngcache[query['location'][0]]
          else:
            url = 'https://maps.googleapis.com/maps/api/geocode/json'
            params = { 'latlng': query['location'][0].replace(';', ','), 'key': bot.config['api_keys']['geocoding'] }
            data = json.loads(requests.get(url, params=params).text)
            addr = data['results'][0]['formatted_address']
            latlngcache[query['location'][0]] = addr
          link = 'http://maps.google.com/maps?z=12&t=m&q=loc:{}'.format(query['location'][0].replace(';', '+'))
          msg = '{} @ {} {}'.format(name, addr, link)
        if 'link' in query:
          msg = '{} {}'.format(name, query['link'][0])
      else:
        msg = name
      conn.cmd('privmsg #sa-minecraft Yo from ' + msg)
  open('/tmp/yo.log', 'w').close() # clear the file

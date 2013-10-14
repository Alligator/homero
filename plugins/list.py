from util import hook
from collections import defaultdict
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
import urllib2
from pprint import pprint

@hook.command(adminonly=True)
def listplugins(inp, bot=None):
  plugs = defaultdict(lambda: defaultdict(list))
  count = 0
  for func, info in bot.plugs['command']:
    plugs[func._filename]['commands'].append((info['name'], func.__doc__))
    count += 1

  for func, info in bot.plugs['event']:
    plugs[func._filename]['events'].append((info['name'], info['events']))
    count += 1

  out = ''
  for k in sorted(plugs.keys()):
    p = plugs[k]
    out += k + '\n'

    if 'commands' in p:
      for cmd in sorted(p['commands'], key=lambda x: x[0]):
        out += '  ' + cmd[0]
        out += ' -> ' + cmd[1] + '\n' if cmd[1] is not None else '\n'

    if 'events' in p:
      if 'commands' in p:
        out += '\n'
      for evt in sorted(p['events'], key=lambda x: x[0]):
        out += '  ' + evt[0]
        out += ' (event) -> ' + ', '.join(evt[1]) + '\n'

    out += '\n'

  out +='\n total: ' + str(count)

  register_openers()
  datagen, headers = multipart_encode({'sprunge': out})
  request = urllib2.Request('http://sprunge.us', datagen, headers)
  return urllib2.urlopen(request).read()

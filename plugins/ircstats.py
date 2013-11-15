from util import hook

from datetime import datetime
import json

# ok so it's gonna be a dictionary like this:
# {
#   sponge: {
#     aliases: <list of aliases>,
#     lines: <list of lines>
#   }
# }
# 
# keys are current nick, if a nick changes the value get assigned to a new key and the old key is added to the aliases list
# 

class IRCStats(object):
  def __init__(self, path):
    self.path = path
    try:
      self.stats = json.loads(open(self.path, 'r').read())
    except Exception, e:
      self.stats = {
        'users': {},
        'daily': [0]*24*7
      }

  # JSON makes defaultdict weird, roll yer own
  def add(self, nick):
    return self.stats['users'].setdefault(nick, {
      'aliases': [],
      'lines': [0]*24
    })

  def new_line(self, nick, hour, day):
    self.add(nick)
    self.stats['users'][nick]['lines'][hour] += 1
    self.stats['daily'][hour + (day*24)] += 1
    self.write()

  def nick_change(self, old, new):
    # if the new nick is already there just use it
    if new in self.stats['users']:
      return

    # switch to new key
    self.stats['users'][new] = self.stats['users'][old]
    del self.stats['users'][old]

    # add old key to aliases
    if old not in self.stats['users'][new]['aliases']:
      self.stats['users'][new]['aliases'].append(old)

    # remove new nick from anyone else who might have it
    for user, data in self.stats['users'].iteritems():
      if new in data['aliases']:
        data['aliases'].remove(new)

    self.write()

  def write(self):
    open(self.path, 'w').write(json.dumps(self.stats))

  def __str__(self):
    return str(dict(self.users))

stats = IRCStats('/var/www/stats.json')

@hook.event('PRIVMSG')
def irc_msg(paraml, input=None, nick=None, chan=None):
  if chan != '#sa-minecraft':
    return
  d = datetime.now().utctimetuple()
  hour = d.tm_hour
  day = d.tm_wday
  stats.new_line(nick, hour, day)

@hook.event('NICK')
def irc_nickchange(paraml, input=None, nick=None, chan=None):
  stats.nick_change(nick, paraml[0])

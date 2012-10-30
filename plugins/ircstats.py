from util import hook
import time
import json

# ok let me write this down
#
# from and to being the nicks switching from and to
# if to exists do nothing, the stats will get added to this nick
# if to doesn't exists add to as an alias to from
#

class Stats(object):
  def __init__(self):
    try:
      self.stats = json.loads(open('/var/www/stats.json', 'r').read())
    except Exception, e:
      self.stats = []

  def get(self, nick):
    for i, user in enumerate(self.stats):
      if nick in user['aliases']:
        return i
    self.stats.append({
      'aliases': [nick],
      'posts': []
    })
    return len(self.stats) - 1

  def add_post(self, nick):
    self.stats[self.get(nick)]['posts'].append(time.time())
    self.write()

  def exists(self, nick):
    for user in self.stats:
      if nick in user['aliases']:
        return True
    return False

  def nick_change(self, frm, to):
    if not self.exists(to):
      i = self.get(frm)
      if to not in self.stats[i]:
        self.stats[i]['aliases'].append(to)
      self.write()

  def write(self):
    j = json.dumps(self.stats)
    open('/var/www/stats.json', 'w').write(j)

stats = Stats();

@hook.singlethread
@hook.event('PRIVMSG')
def ircstats(paraml, input=None, nick=None, bot=None):
  if input['chan'] != '#sa-minecraft':
    return

  global stats
  stats.add_post(nick)

@hook.event('NICK')
def nickchange(paraml, input=None, nick=None):
  if input['chan'] != '#sa-minecraft':
    return

  global stats
  stats.nick_change(nick, paraml[0])
  # nick = old nick
  # paraml[0] = new nick

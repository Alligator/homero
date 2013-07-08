from util import hook
from time import sleep

chans = {}

@hook.command
def bully(inp, say=None):
  say('{}: I feel offended by your recent action(s). Please read http://stop-irc-bullying.eu/stop'.format(inp))

@hook.command(adminonly=True)
def bullyall(inp, chan=None, conn=None, say=None):
  if chan.startswith('#'):
    conn.cmd('NAMES {}'.format(chan))
    sleep(2) # im the worst
    for name in chans[chan]:
      bully(name, say)

@hook.event('353')
def get_names(paraml):
  global chans
  chan = paraml[2]
  names = paraml[3:]
  chans[chan] = names[0].strip().split(' ')

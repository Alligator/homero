from util import hook

@hook.command
def bully(inp, say=None):
  say('{}: I feel offended by your recent action(s). Please read http://stop-irc-bullying.eu/stop'.format(inp))

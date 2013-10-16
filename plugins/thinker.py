from util import hook
import math

@hook.command(multiline=True)
def think(inp, say=None):
  lines = inp.split('\n')
  print repr(inp)
  c = math.ceil(len(lines)/2.0)
  out = ''
  for i, line in enumerate(lines):
    if i+1 == c:
      say(u'(  .  __ . ) . o O ( {} )'.format(line))
    else:
      say(u'                     {}'.format(line))

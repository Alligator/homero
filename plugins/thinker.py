from util import hook

@hook.command
def think(inp, say=None):
  return '(  .  __ . ) . o O ( {} )'.format(inp)

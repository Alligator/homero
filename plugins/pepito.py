from util import hook
from random import randint

@hook.command
def pepito(inp, say=None):
  say('<peptio> hey guys i just ate {} pills'.format(randint(68, 1489)))

from util import hook
from random import randint

@hook.command
def pepito(inp, say=None):
  amt = randint(68, 1489)
  say(u'<peptio> hey guys i just ate {} pills'.format(unichr(0x1F4AF) if amt == 100 else amt))

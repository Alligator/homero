from util import hook
import re

@hook.regex('send(\s)+spike', re.IGNORECASE)
def spike(inp, say=None):
  say('spike sent')

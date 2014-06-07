from util import hook
import re

@hook.regex('send(\s)+spike', re.IGNORECASE)
def spike(inp, say=None):
  say('spike sent')

@hook.regex('anime', re.IGNORECASE)
def anime(inp):
  return 'I think you mean animé.'

@hook.regex('illwinter')
def trillwinter(inp, say=None):
  return say('TRILLWINTER')

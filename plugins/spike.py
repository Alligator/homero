from util import hook
import re

@hook.regex('send(\s)+spike', re.IGNORECASE)
def spike(inp, say=None):
  say('spike sent')

@hook.regex('anime', re.IGNORECASE, ignorechannels=['#ffgoons'])
def anime(inp, channel=None):
  return 'I think you mean animé.'

@hook.regex(r'(?<!tr)illwinter', re.IGNORECASE)
def trillwinter(inp, say=None):
  return say('TRILLWINTER')

@hook.regex(r'hot pants', re.IGNORECASE)
def hotpants(inp, say=None):
  say('Jesus Christ.')

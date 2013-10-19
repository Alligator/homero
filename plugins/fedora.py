from util import hook
from textwrap import wrap
from itertools import izip_longest
from math import ceil

@hook.command(multiline=True)
def fedora(inp, say=None):
  fed = [
    unicode('\x0301,01▃▃▃▃▃\x03▇▇▅▅▇▇     ', 'utf-8', 'replace'),
    unicode('\x0301,01▃▃▃\x03▃▃▇▇▇▇▇▇▃▃   ', 'utf-8', 'replace'),
    unicode('\x0301,01▃▃▃▃\x03◢┃▃╮╭▃┃◣    ', 'utf-8', 'replace'),
    unicode('\x0301,01▃▃▃▃\x03◢┃╮┃┃╭┃◣    ', 'utf-8', 'replace'),
    unicode('\x0301,01▃▃▃▃\x03◢┃▃▆▆▃┃◣    ', 'utf-8', 'replace'),
    unicode('\x0301,01▃▃▃▃\x03◢◣╰▕▍╯◢◣    ', 'utf-8', 'replace'),
    unicode('\x0301,01▃▃▃▃▃\x03▇◣╭╮◢▇     ', 'utf-8', 'replace'),
    unicode('▃▅▆▇▇▇▇▅▅▇▇▇▇▆▅▃', 'utf-8', 'replace')
  ]
  txt = wrap(inp, 80)
  start = int(ceil(float(len(fed) - len(txt)) / 2))
  if start < 0:
    start = 0j
  else:
    for l in fed[:start]:
      say(l)
  for f, l in izip_longest(fed[start:], txt):
    say(f + (l if l else ''))

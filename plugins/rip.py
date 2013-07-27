from util import hook, strip_formatting
from textwrap import wrap

WIDTH = 40

@hook.command
def rip(inp, say=None):
  if inp == '': return
  og = inp
  inp = inp.encode('utf-8')
  width = WIDTH + 4

  if len(inp) > WIDTH:
    txt = wrap(inp, WIDTH)
  else:
    width = len(inp) + 4
    txt = [inp]

  topfiller = str.center('', width-5, '-')

  headstone = []
  headstone.append('  _.' + topfiller + '-._\n')
  headstone.append(' |' + str.center('RIP', width) + '|\n')
  for line in txt:
    headstone.append(' |' + str.center(line.upper(), width) + '|\n')
  headstone.append(' |' + str.center('', width, '_') + '|\n')
  headstone.append('|' + str.center('', width+2, '_') + '|')

  for l in headstone:
    say(l.decode('utf-8'))

@hook.command
def bread(inp, say=None):
  og = inp
  inp = inp.encode('utf-8')
  topfiller = str.center('', len(strip_formatting.strip(og))-1, '-')

  top = '  .' + topfiller + '-.\n'

  width = len(top)-3

  rip = ' |' + str.center('', width) + '|\n'
  nmr = ' |' + str.center(inp.upper(), width) + '|\n'
  lsr = ' |' + str.center('', width, '_') + '|\n'

  headstone = [top, rip, nmr, lsr]
  for l in headstone:
    say(l.decode('utf-8'))

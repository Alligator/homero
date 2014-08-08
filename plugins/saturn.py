from util import hook
from random import choice

quotes = [
  'i nOt sURE. BOinG!',
  'wE fEEl GROOvE! Hi HO. mE mR. SatURn. tHis PlacE, all aRE mR. SatURn',
  'DO yOU want mE tO OPERatE On yOU? DinG?',
  'DRink cOffEE BEfORE GO?',
  'ZOOm!',
  'GO in HOt SPRinG. waSH BaRf Off yOU BODy!',
  'maKE nEw tHinG! mUSt maKE! DaDDy! BOinG!',
  'i wiSH fall in lOvE...',
  'BOinG'
]

@hook.command
def saturn(inp):
  mappings = {
    'a': 'ᗩ',
    'b': 'ᗷ',
    'c': 'ᘓ',
    'd': 'ᗪ',
    'e': 'ᕮ',
    'f': 'ᖴ',
    'g': 'ᕤ',
    'h': 'ᗁ',
    'i': 'ᓮ',
    'j': 'ᒎ',
    'k': 'ᔌ',
    'l': 'ᒪ',
    'm': 'ᙏ',
    'n': 'ᑎ',
    'o': 'ᘎ',
    'p': 'ᖘ',
    'q': 'ᕴ',
    'r': 'ᖇ',
    's': 'ᔕ',
    't': 'ᒮ',
    'u': 'ᘮ',
    'v': 'ᐯ',
    'w': 'ᙎ',
    'x': '᙭',
    'y': 'ᖿ',
    'z': 'ᔓ',
    "'": 'ᐞ'
  }
  out = ''
  if inp == '':
    inp = choice(quotes)
  for c in inp.lower():
    if c in mappings:
      out += mappings[c]
    else:
      out += c.encode('utf-8')
    out += ' '
  print len(out)
  return out.decode('utf-8', errors='ignore')

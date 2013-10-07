from util import hook, strip_formatting
from random import randint, choice
from collections import OrderedDict
import string

#------------------------------------------------------------------------------
# COLORS

colors = OrderedDict([
  ('red',    '\x0304'),
  ('orange', '\x0307'),
  ('yellow', '\x0308'),
  ('green',  '\x0309'),
  ('cyan',   '\x0303'),
  ('ltblue', '\x0310'),
  ('rylblue','\x0312'),
  ('blue',   '\x0302'),
  ('magenta','\x0306'),
  ('pink',   '\x0313'),
  ('maroon', '\x0305')
])

@hook.command
def red(inp): return color('red %s' % inp)
@hook.command
def orange(inp): return color('orange %s' % inp)
@hook.command
def yellow(inp): return color('yellow %s' % inp)
@hook.command
def green(inp): return color('green %s' % inp)
@hook.command
def cyan(inp): return color('cyan %s' % inp)
@hook.command
def ltblue(inp): return color('ltblue %s' % inp)
@hook.command
def rylblue(inp): return color('rylblue %s' % inp)
@hook.command
def blue(inp): return color('blue %s' % inp)
@hook.command
def magenta(inp): return color('magenta %s' % inp)
@hook.command
def pink(inp): return color('pink %s' % inp)
@hook.command
def maroon(inp): return color('maroon %s' % inp)

@hook.command
def color(inp):
  c = inp.split(' ')[0]
  if c in colors:
    return colors[c] + inp[len(c)+1:]
  else:
    return inp
color.__doc__ = 'color name text - print text in color, available colors: ' + ' '.join(colors.keys())

@hook.command
def rot13(inp):
  return inp.encode('rot13')

@hook.command
def rainbow(inp):
  inp = unicode(inp)
  inp = strip_formatting.strip(inp)
  col = colors.items()
  out = ""
  l = len(colors)
  for i, t in enumerate(inp):
      out += col[i % l][1] + t
  return out

@hook.command
def wrainbow(inp):
  inp = unicode(inp)
  col = colors.items()
  inp = strip_formatting.strip(inp).split(' ')
  out = []
  l = len(colors)
  for i, t in enumerate(inp):
      out.append(col[i % l][1] + t)
  return ' '.join(out)

@hook.command
def usa(inp):
  inp = strip_formatting.strip(inp)
  c = [colors['red'], '\x0300', colors['blue']]
  l = len(c)
  out = ''
  for i, t in enumerate(inp):
    out += c[i % l] + t
  return out


#------------------------------------------------------------------------------
# CASE

@hook.command
def upper(inp):
  return inp.upper()

@hook.command
def lower(inp):
  return inp.lower()

@hook.command
def capwords(inp):
  return string.capwords(inp)


#------------------------------------------------------------------------------
# STRANGE

@hook.command
def bubble(inp):
  out = unicode()
  for c in inp:
    print c
    if not c == ' ':
      out += c + unichr(0x020DD)
    out += ' '
  return out

@hook.command
def ruin(inp):
  sets = [
    (0x0300, 0x036F),
    (0x1DC0, 0x1DE6),
    (0x20D0, 0x20F0)
  ]
  out = u''
  l = len(inp)
  for ind, c in enumerate(inp):
    out += c
    if randint(0, l) < ind + 1:
      for i in range(ind/4):
        out += unichr(randint(*choice(sets)))
  return out

@hook.command
def change(inp):
  # fuck y
  vowels = 'aeiou'
  letters = 'abcdefghijklmnopqrstuvwxyz'
  numbers = '1234567890'
  out = ''
  if choice((True, False)):
    inp = inp.upper()
  else:
    inp = inp.lower()

  for c in inp:
    if randint(0, 12) > 11:
      continue
    if randint(0, 10) > 9 and c.lower() in letters:
      c = choice(letters)
    elif randint(0, 9) > 8 and c in numbers:
      c = choice(numbers)
    if randint(0, 9) > 8 and c in vowels:
      c = 'X'
    out += c
  return out

@hook.command
def flip(inp):
  flipTable = {
    u'\u0021' : u'\u00A1',
    u'\u0022' : u'\u201E',
    u'\u0026' : u'\u214B',
    u'\u0027' : u'\u002C',
    u'\u0028' : u'\u0029',
    u'\u002E' : u'\u02D9',
    u'\u0033' : u'\u0190',
    u'\u0034' : u'\u152D',
    u'\u0036' : u'\u0039',
    u'\u0037' : u'\u2C62',
    u'\u003B' : u'\u061B',
    u'\u003C' : u'\u003E',
    u'\u003F' : u'\u00BF',
    u'\u0041' : u'\u2200',
    u'\u0042' : u'\U00010412',
    u'\u0043' : u'\u2183',
    u'\u0044' : u'\u25D6',
    u'\u0045' : u'\u018E',
    u'\u0046' : u'\u2132',
    u'\u0047' : u'\u2141',
    u'\u004A' : u'\u017F',
    u'\u004B' : u'\u22CA',
    u'\u004C' : u'\u2142',
    u'\u004D' : u'\u0057',
    u'\u004E' : u'\u1D0E',
    u'\u0050' : u'\u0500',
    u'\u0051' : u'\u038C',
    u'\u0052' : u'\u1D1A',
    u'\u0054' : u'\u22A5',
    u'\u0055' : u'\u2229',
    u'\u0056' : u'\u1D27',
    u'\u0059' : u'\u2144',
    u'\u005B' : u'\u005D',
    u'\u005F' : u'\u203E',
    u'\u0061' : u'\u0250',
    u'\u0062' : u'\u0071',
    u'\u0063' : u'\u0254',
    u'\u0064' : u'\u0070',
    u'\u0065' : u'\u01DD',
    u'\u0066' : u'\u025F',
    u'\u0067' : u'\u0183',
    u'\u0068' : u'\u0265',
    u'\u0069' : u'\u0131',
    u'\u006A' : u'\u027E',
    u'\u006B' : u'\u029E',
    u'\u006C' : u'\u0283',
    u'\u006D' : u'\u026F',
    u'\u006E' : u'\u0075',
    u'\u0072' : u'\u0279',
    u'\u0074' : u'\u0287',
    u'\u0075' : u'\u006E',
    u'\u0076' : u'\u028C',
    u'\u0077' : u'\u028D',
    u'\u0079' : u'\u028E',
    u'\u007B' : u'\u007D',
    u'\u203F' : u'\u2040',
    u'\u2045' : u'\u2046',
    u'\u2234' : u'\u2235'
  }
  inp = unicode(inp)
  out = ''
  for c in inp[::-1]:
    if c in flipTable:
      out += flipTable[c]
    else:
      out += c

  return out

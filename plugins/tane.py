from util import hook, strip_formatting
from collections import OrderedDict
from datetime import datetime
import re

taned = False

@hook.event('*')
def tane_event(paraml, conn=None):
    global taned
    today = datetime.today()
    if today.weekday() == 4 and today.hour == 18 and not taned:
        taned = True
        conn.cmd('PRIVMSG #sa-minecraft ' + rainbow("I CAN'T WAIT"))
        conn.cmd('PRIVMSG #sa-minecraft http://tane.us/weekend.html')
        conn.cmd('PRIVMSG #sa-minecraft ' + rainbow("FOR THE WEEKEND TO BEGIN"))

    if today.weekday() != 4:
        taned = False

@hook.command
def tane(inp, say=None):
    today = datetime.today()
    if today.weekday() == 4:
      say(rainbow("I CAN'T WAIT"))
      say('http://tane.us/weekend.html')
      say(rainbow("FOR THE WEEKEND TO BEGIN"))
    else:
      return rainbow('с м е р т ь   ж д е т   в с е х   н а с')

colors = OrderedDict([
  ('red',    '\x0304'),
  ('ornage', '\x0307'),
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
def rainbow(inp):
  inp = inp.decode('utf-8')
  inp = strip_formatting.strip(inp)
  col = colors.items()
  out = ""
  l = len(colors)
  for i, t in enumerate(inp):
      out += col[i % l][1] + t
  return out

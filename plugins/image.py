from random import choice
from util import hook
from collections import deque, defaultdict
from PIL import Image, ImageDraw, ImageFont
import cStringIO
import requests
import base64
import simplejson
import textwrap

q = defaultdict(lambda: deque([], 8))
colors = [
  (0x55, 0x55, 0xFF), # blue
  (0x00, 0x00, 0xAA), # dark blue

  (0x55, 0xFF, 0x55), # green
  (0x00, 0xAA, 0x00), # dark green

  (0xFF, 0x55, 0x55), # red
  (0xAA, 0x00, 0x00), # dark red

  (0xFF, 0x55, 0xFF), # magenta
  (0xAA, 0x00, 0xAA), # dark magenta

  (0xFF, 0xFF, 0x55), # yellow
  (0xAA, 0x55, 0x00), # orange

  (0x55, 0xFF, 0xFF), # cyan
  (0x00, 0xAA, 0x00), # dark cyan

  (0xAA, 0xAA, 0xAA), # light grey
]

users = defaultdict(lambda: choice(colors))

# oh my god
def get_image(chan):
  img = Image.new('RGB', (638, 142))
  drw = ImageDraw.Draw(img)
  fnt = ImageFont.truetype(filename='/home/alligator/SourceCodePro-Regular.ttf', size=28)

  w, h = drw.textsize('#', font=fnt)
  hmargin = w
  vmargin = h/4
  h += vmargin*2
  imgw = w*81
  imgh = h * 11
  img = Image.new('RGB', (imgw, imgh))
  drw = ImageDraw.Draw(img)

  # top and bottom lines
  drw.text((hmargin, vmargin), '{:-^79}'.format('{ ' + chan + ' }'), fill=(200, 200, 200), font=fnt)
  drw.text((hmargin, (h * 9)+vmargin), '{:-^79}'.format(''), fill=(200, 200, 200), font=fnt)

  lines = q[chan]
  for i, (kind, nick, msg) in enumerate(lines):
    ch = ((i+1) * h) + vmargin
    if kind == 'msg':
      drw.text((hmargin, ch), '<', fill=(255, 255, 255), font=fnt)
      drw.text((hmargin + w, ch), nick, fill=users[nick.lower()], font=fnt)
      drw.text((hmargin + w * (len(nick)+1), ch), '> ' + msg, fill=(255, 255, 255), font=fnt)
    elif kind == 'cont':
      drw.text((hmargin + w * (len(nick)+3), ch), msg, fill=(255, 255, 255), font=fnt)
    elif kind == 'join':
      drw.text((hmargin, ch), '-!- {} joined the channel'.format(nick), fill=(170, 170, 170), font=fnt)
    elif kind == 'part':
      drw.text((hmargin, ch), '-!- {} left the channel'.format(nick), fill=(170, 170, 170), font=fnt)
  return img.resize((imgw/2, imgh/2), Image.ANTIALIAS)

def imagedraw(chan):
  img = get_image(chan)
  img.save('/var/www/irc.png', 'PNG')

def imageupload(chan, pw):
  img = get_image(chan)
  auth = ('enemy.forest.brigade@gmail.com', pw)
  o = cStringIO.StringIO()
  img.save(o, 'png')
  data = {'image': base64.b64encode(o.getvalue())}
  resp = requests.post('https://foauth.org/api.imgur.com/3/upload', data=data, auth=auth)
  try:
    j = simplejson.loads(resp.text)
    return j['data']['link']
  except Exception, e:
    print e

# @hook.singlethread
# @hook.command
def image(inp, bot=None, chan=None):
  if inp:
    chan = inp
  return imageupload(chan, bot.config['api_keys']['foauth'])

# @hook.singlethread
# @hook.event('JOIN')
def imagejoin(paraml, input=None, nick=None, chan=None):
  q[chan].append(('join', nick, ' joined ' + chan,))
  if chan == '#sa-minecraft':
    imagedraw(chan)

# @hook.singlethread
# @hook.event('PART')
def imagepart(paraml, input=None, nick=None, chan=None):
  q[chan].append(('part', nick, ' left ' + chan,))
  if chan == '#sa-minecraft':
    imagedraw(chan)

# @hook.singlethread
# @hook.event('PRIVMSG')
def imagething(inp, chan=None, nick=None):
  if inp[1].startswith('.'): return
  if len(inp[1]) + len(nick) + 5 > 79:
    txt = textwrap.wrap(inp[1], 79 - (len(nick) + 5))
    q[chan].append(('msg', nick, txt[0].encode('utf-8')))
    for line in txt[1:]:
      q[chan].append(('cont', nick, line.encode('utf-8')))
  else:
    q[chan].append(('msg', nick, inp[1].encode('utf-8')))
  if chan == '#sa-minecraft':
    imagedraw(chan)

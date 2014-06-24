from util import hook, http
from PIL import Image
import random
import cStringIO
import base64
import requests
import simplejson

@hook.command
def ca(inp, bot=None):
  try:
    rule = int(inp)
    if rule > 255:
      return '0 < rule < 255 fyi'
  except ValueError:
    rule = random.randint(0, 255)
  width = 200
  height = 200
  cells = []
  data = []

  for i in range(width):
    c = random.randint(0, 1)
    data.append(1-c)
    cells.append(c)


  for i in range(height-1):
    ncells = []
    for i, cell in enumerate(cells):
      patt = '0' if i == 0 else str(cells[i-1])
      patt += str(cell)
      patt += '0' if i == width-1 else str(cells[i+1])

      c = int(bool(rule & 2**int(patt, 2)))
      ncells.append(c)
      data.append(1-c)
    cells = ncells

  img = Image.new('1', (width, height), color=255)
  img.putdata(data)
  img = img.resize((width*2, height*2), Image.NEAREST)

  auth = ('enemy.forest.brigade@gmail.com', bot.config['api_keys']['foauth'])
  o = cStringIO.StringIO()
  img.save(o, 'png')
  data = {'image': base64.b64encode(o.getvalue())}
  resp = requests.post('https://foauth.org/api.imgur.com/3/upload', data=data, auth=auth)
  j = simplejson.loads(resp.text)
  return 'rule {}: {}'.format(rule, j['data']['link'])

from util import hook
import requests
import json

tags = {
  'sport': ['sport', 'nba'],
  'anime': ['cartoon']
}

def get_tags(imgurl):
  mash_params = {'nearest': True, 'imageurl': imgurl, 'timestamp':140000}

  mash_request = requests.post('http://clarifai.com/api/upload/', data=mash_params)
  mash_output = mash_request.json()
  return mash_output['files'][0]['predicted_classes']

@hook.regex(r'(https?://.*(?:imgur)?(?:gif|jpg|png))\s?')
def hitzimg(inp, lastparam=None, chan=None, nick=None, say=None):
  if chan != '#sa-minecraft' or nick != 'hitz': return
  t = get_tags(inp.group(0))
  for k, v in tags.iteritems():
    c = set(v).intersection(set(t))
    if len(c) > 0:
      say('/!\\ ALERT /!\\ HITZ ' + k.upper() + ' LINK DETECTED')
      return

@hook.command
def img(inp):
  return ', '.join(get_tags(inp))

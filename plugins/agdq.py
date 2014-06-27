import urllib2
import time
import requests

import lxml.html
from datetime import datetime, timedelta
from util import hook, http

schedule = []
current_game = ''

@hook.event('*', limit=5)
def get_agdq_schedule(paraml):
  global schedule, current_game
  j = http.get_json('https://api.twitch.tv/kraken/streams/speeddemosarchivesda')
  current_game = j['stream']['channel']['game']

  h = requests.get('http://gamesdonequick.com/schedule').text
  html = lxml.html.fromstring(h)
  x = html.xpath("//tbody[@id='runTable']//tr[not(contains(@id, 'daySplit'))]")
  # 7/29/2013 10:50:00
  # times are -5 ugh
  g = []
  for elm in x:
    tm = datetime.strptime(elm.getchildren()[0].text, '%m/%d/%Y %H:%M:%S') + timedelta(hours=7)
    tm = time.mktime(tm.timetuple())
    game = elm.getchildren()[1].text
    g.append([tm, game])
  schedule = g

@hook.command(limit=5)
def sgdq(inp):
  global schedule, current_game
  curr = None
  game = schedule[0][1]
  for i, (tm, gm) in enumerate(schedule[1:]):
    if current_game in gm:
      curr = gm
      game = schedule[i+2][1]
      return 'Next up: {} | Currently Playing: {}'.format(game, curr)
    game = gm

  # if we got here no game was found
  now = time.time()
  for i, (tm, gm) in enumerate(schedule[1:]):
    if tm > now:
      curr = schedule[i][1]
      game = gm
      return 'Next up: {} | Currently Playing: {}'.format(game, curr)

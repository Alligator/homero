# -*- coding: utf-8 -*-
from util import hook
import json
import requests
import re

@hook.command(autohelp=False)
def weather(inp, bot=None, reply=None, nick=None, db=None):
  ".wea [location] [dontsave] -- get weather for location"
  db.execute("create table if not exists weather(nick primary key, loc, lat, lng, desc)")
  dontsave = inp.endswith(' dontsave')
  if dontsave:
    loc = inp[:-9]
  loc = inp.lower().strip()

  addr = loc
  lat = None
  lng = None
  desc = None
  if not loc:
    loc = db.execute("select loc, lat, lng, desc from weather where nick=lower(?)",
                     (nick,)).fetchone()
    if not loc:
      return weather.__doc__
    addr, lat, lng, desc = loc

  if not lat or not lng or not desc:
    # do geocoding req
    url = 'https://maps.googleapis.com/maps/api/geocode/json'
    params = { 'address': addr, 'key': bot.config['api_keys']['geocoding'] }
    data = json.loads(requests.get(url, params=params).text)
    geo = data['results'][0]['geometry']['location']
    geo['desc'] = data['results'][0]['formatted_address']
  else:
    geo = { 'lat': lat, 'lng': lng, 'desc': desc }

  url = 'https://api.forecast.io/forecast/{}/{},{}'.format(bot.config['api_keys']['forecast'], geo['lat'], geo['lng'])
  data = json.loads(requests.get(url, params={'units': 'si'}).text)

  current = data['currently']
  forecast = data['daily']['summary']

  m = re.search(u'([-\d]+)°C', forecast)
  if m:
    t = str(int(int(m.group(1)) * (9.0/5.0)) + 32)
    e = m.end(0)
    forecast = forecast[:e] + '/' + t + 'F' + forecast[e:]

  summary = u'{} | {}°C/{}F | Humidity: {} | Wind: {}kph/{}mph'.format(
      current['summary'],     # summary
      int(current['temperature']), # temp in c
      int(current['temperature'] * (9.0/5.0)) + 32, # temp in f lmao
      '{}%'.format(int(current['humidity'] * 100)),
      int(round((current['windSpeed']*60*60)/1000)),
      int(round((current['windSpeed']*60*60)/1000 * 0.621371)))
  output = u'{} | {}'.format(geo['desc'], summary)
  reply(output)
  reply(forecast)

  if inp and not dontsave:
    db.execute("insert or replace into weather(nick, loc, lat, lng, desc) values (?,?,?,?,?)",
               (nick.lower(), addr, geo['lat'], geo['lng'], geo['desc']))
    db.commit()
  return

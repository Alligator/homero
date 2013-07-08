from util import hook, http
from pprint import pprint

@hook.command(autohelp=False)
def weather(inp, bot=None, reply=None, nick=None, db=None):
  '.weather <location> [dontsave] -- gets weather data for location'

  request = 'http://api.worldweatheronline.com/free/v1/weather.ashx?key={0}&q={1}&num_of_days=1&format=json'

  loc = inp

  # init db
  db.execute("create table if not exists weather(nick primary key, loc)")

  dontsave = inp.endswith(' dontsave')
  if dontsave:
    loc = inp[:-9]

  loc = inp.lower().strip()

  # no address given
  if not loc:
    loc = db.execute("select loc from weather where nick=lower(?)",
                     (nick,)).fetchone()
    if not loc:
      return weather.__doc__
    loc = loc[0]

  try:
    j = http.get_json(request.format(bot.config['api_keys']['wwo'], http.quote_plus(loc)))
  except IOError, e:
    print e
    return 'um the api broke or something'

  if 'current_condition' not in j['data']:
    return 'Location not found'
  
  w = j['data']['current_condition'][0]
  print w
  w['city'] = j['data']['request'][0]['query']
  w['desc'] = w['weatherDesc'][0]['value']
  print w
  reply('{city}: {desc}, {temp_F}F/{temp_C}C, Humidity: {humidity}%, '\
         'Wind: {windspeedKmph}kph/{windspeedMiles}mph'.format(**w))

  if inp and not dontsave:
    db.execute("insert or replace into weather(nick, loc) values (?,?)",
               (nick.lower(), loc))
    db.commit()

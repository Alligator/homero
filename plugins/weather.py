"weather, thanks to google"

from util import hook, http

def get_weather_xml(nick, db, loc=None):
  db.execute("create table if not exists weather(nick primary key, loc)")
  
  inp = loc

  dontsave = loc.endswith(" dontsave")
  if dontsave:
    loc = loc[:-9].strip().lower()

  if not loc:
    loc = db.execute("select loc from weather where nick=lower(?)",
        (nick,)).fetchone()
    if not loc:
      return weather.__doc__
    loc = loc[0]

  w = http.get_xml('http://www.google.com/ig/api', weather=loc)

  if inp and not dontsave:
    db.execute("insert or replace into weather(nick, loc) values (?,?)",
        (nick.lower(), loc))
    db.commit()

  return w.find('weather')

@hook.command(autohelp=False)
def weather(inp, nick='', reply=None, db=None):
  ".weather <location> [dontsave] -- gets weather data from Google"
  w = get_weather_xml(nick, db, inp)

  if w.find('problem_cause') is not None:
    return "couldn't fetch weather data for '%s', try using a zip or " \
        "postal code." % inp

  info = dict((e.tag, e.get('data')) for e in w.find('current_conditions'))
  info['city'] = w.find('forecast_information/city').get('data')
  info['high'] = w.find('forecast_conditions/high').get('data')
  info['low'] = w.find('forecast_conditions/low').get('data')

  reply('%(city)s: %(condition)s, %(temp_f)sF/%(temp_c)sC (H:%(high)sF'\
      ', L:%(low)sF), %(humidity)s, %(wind_condition)s.' % info)

  if inp and not dontsave:
    db.execute("insert or replace into weather(nick, loc) values (?,?)",
        (nick.lower(), loc))
    db.commit()

@hook.command(autohelp=False)
def forecast(inp, nick=None, reply=None, db=None):
  w = get_weather_xml(nick, db, inp)

  if w.find('problem_cause') is not None:
    return "couldn't fetch weather data for '%s', try using a zip or " \
        "postal code." % inp

  # im laffin v. hard at this monstrosity
  out = ' | '.join(['{0}: H:{1}F L:{2}F. {3}'.format(a.find('day_of_week').get('data'), a.find('low').get('data'), a.find('high').get('data'), a.find('condition').get('data')) for a in w.findall('forecast_conditions')])
  city = w.find('forecast_information/city').get('data')

  reply('{0} | {1}'.format(city, out))

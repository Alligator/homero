from util import hook, http
from urllib2 import quote

@hook.command(autohelp=False)
def weather(inp, nick=None, reply=None, db=None, bot=None):
  'weather'
  # init the db
  db.execute('create table if not exists weather(nick primary key, loc)')

  # location and dontsave
  dontsave = inp.endswith(' dontsave')
  if inp and dontsave:
    inp = inp[:-9].strip().lower()

  # no location:
  if not inp:
    inp = db.execute('select loc from weather where nick=lower(?)', (nick,)).fetchone()
    # no location in db
    if not inp:
      return 'not in the db?'
    inp = inp[0]
  # just location
  elif not dontsave:
    db.execute('insert or replace into weather(nick, loc) values (?,?)', (nick.lower(), inp))
    db.commit()

  api_url = 'http://api.aerisapi.com/observations/{0}?client_id={1}&client_secret={2}'.format(quote(inp), bot.config['api_keys']['aeris_id'], bot.config['api_keys']['aeris_secret'])

  w = http.get_json(api_url)
  if w['success']:
    w = w['response']
    p = w['place']
    o = p['name'].capitalize() + ', '
    if p['state']:
      o += p['state'].capitalize() + ', '
    o += p['country'].upper()

    ob = w['ob']

    return '{0}: {1} ({2}C/{3}F) {4}% humidity'.format(o, ob['weather'], ob['tempC'], ob['tempF'], ob['humidity'])
  else:
    return 'not found'

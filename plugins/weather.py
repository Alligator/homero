from util import hook, http

@hook.command(autohelp=False)
def weather(inp, nick=None, reply=None, db=None, bot=None):
  'weather'
  # init the db
  db.execute('create table if not exists weather(nick primary key, loc)')

  api_url = 'http://api.wunderground.com/api/{0}/conditions/q/'.format(bot.config['api_keys']['wunderground'])

  # location and dontsave
  dontsave = inp.endswith(' dontsave')
  if inp and dontsave:
    inp = inp[:-9].strip().lower()

  # no location:
  if not inp:
    inp = db.execute('select loc from weather where nick=lower(?)', (nick,)).fetchone()
    # no location in db
    if not inp:
      return weather.__doc__
    inp = inp[0]
  # just location
  elif not dontsave:
    db.execute('insert or replace into weather(nick, loc) values (?,?)', (nick.lower(), inp))
    db.commit()

  response = http.get_json(api_url + inp + '.json')
  try:
    return response['response']['error']['description']
  except KeyError, e:
    pass

  # if we get multiple matches pick the first and re-request
  try:
    matches = response['response']['results']
    response = http.get_json(api_url + 'zmw:' + matches[0]['zmw'] + '.json')
    print response
  except KeyError, e:
    pass

  name = response['current_observation']['display_location']['full']

  return '{name} - {weather}, {temperature_string}'.format(name=name, **response['current_observation'])

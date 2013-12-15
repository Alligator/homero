from  util import hook, http

@hook.command('time')
def time_cmd(inp, reply=None, bot=None):
  if inp == 'lodon':
    inp = 'london'
  if inp == 'my life':
    return 'no:no'
  request = 'http://api.worldweatheronline.com/free/v1/tz.ashx?key={0}&q={1}&format=json'
  j = http.get_json(request.format(bot.config['api_keys']['wwo'], http.quote_plus(inp)))
  j = j['data']['time_zone'][0]
  utc = j['utcOffset'].split('.')[0]
  utc = '+' + utc if float(utc) >= 0 else utc
  return '{0} (UTC {1})'.format(j['localtime'], utc)

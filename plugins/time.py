from  util import hook, http

@hook.command('time')
def time_cmd(inp, reply=None):
  if inp == 'lodon':
    inp = 'london'
  t = http.get_json('http://www.worldweatheronline.com/feed/tz.ashx?key=a59771d9b2135559122607&q=%s&format=json' % inp)
  reply(t['data']['request'][0]['query'] + ' | ' + t['data']['time_zone'][0]['localtime'])

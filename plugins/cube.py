from util import hook, http

@hook.command
def cube(inp):
  up = '\x0309up'
  down = '\x0304down'
  status = http.get_json('http://direct.cyberkitsune.net/canibuycubeworld/status.json')
  stats = http.get_json('http://direct.cyberkitsune.net/canibuycubeworld/stats.json')

  siteup = str(round(((float(stats['siteup'])/stats['updatecount'])*100)*100)/100) + '%'
  regup = str(round(((float(stats['regup'])/stats['updatecount'])*100)*100)/100) + '%'
  shopup = str(round(((float(stats['shopup'])/stats['updatecount'])*100)*100)/100) + '%'

  out = 'Picroma is ' + (up if status['site'] else down) + ' \x03(%s)' % siteup
  out += ' | Registration is ' + (up if status['reg'] else down) + ' \x03(%s)' % regup
  out += ' | Shop is ' + (up if status['shop'] else down) + ' \x03(%s)' % shopup
  return out

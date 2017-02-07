from util import hook, http

currentStreamers = set()

@hook.event('*')#, limit=2)
def beam(inp, conn=None):
  global currentStreamers
  j = http.get_json('https://beam.pro/api/v1/teams/3457/users')
  streamers = set(map(lambda x: x['username'], filter(lambda x: x['channel']['online'], j)))
  newStreamers = streamers - currentStreamers
  currentStreamers = streamers
  for name in newStreamers:
      conn.cmd('privmsg #sa-minecraft \x0313{} started streaming http://stream.alligatr.co.uk/'.format(name))

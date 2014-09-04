from util import hook, http

streaming = {}

@hook.event('*', limit=2)
def hitbox(inp, conn=None):
  global streaming
  j = http.get_json('https://api.hitbox.tv/team/breadcrew?liveonly=true&media=true&fast=true')
  streams = j['media']['livestream']
  if len(streams) == 0:
    streaming = {}
    return
  new_streaming = {}
  for stream in streams:
    name = stream['media_display_name']
    if name not in streaming:
      conn.cmd('privmsg #sa-minecraft \x0313{} started streaming http://stream.alligatr.co.uk/hitbox.html'.format(name))
    new_streaming[name] = True
  streaming = new_streaming

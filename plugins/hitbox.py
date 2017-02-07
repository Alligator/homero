from util import hook, http

streaming = {}

@hook.event('*', limit=2)
def hitbox(inp, conn=None):
  global streaming
  j = http.get_json('https://api.hitbox.tv/team/breadcrew?media=true&media_type=live&liveonly=true')
  streams = j['media']['livestream']
  new_streaming = {}
  for stream in streams:
    name = stream['media_display_name']
    if stream['media_is_live'] == '1' and name not in streaming:
      conn.cmd('privmsg #sa-minecraft \x0313{} started streaming http://stream.alligatr.co.uk/'.format(name))
    new_streaming[name] = True
  streaming = new_streaming

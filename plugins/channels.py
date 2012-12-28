from util import hook

channel_list = []

@hook.event('JOIN')
def channel_join(paraml):
  global channel_lsit
  if paraml[0] not in channel_list:
    channel_list.append(paraml[0])

@hook.command(autohelp=False)
def channels(inp):
  return ', '.join(channel_list)

from util import hook
from datetime import datetime, timedelta
from math import floor

@hook.command
def beats(inp):
  d = datetime.utcnow() + timedelta(hours=1)
  local = d.strftime('%H:%M:%S')
  beats = int(floor((d.second + (d.minute * 60) + (d.hour * 3600)) / 86.4))
  return 'local time: {} | beat time: {}'.format(local, beats)

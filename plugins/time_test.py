from util import hook
import time

@hook.time(10)
def idiot(inp, bot=None):
  for key, conn in bot.conns.iteritems():
    conn.msg('#flf', '10 seconds passed ' + str(time.time()))

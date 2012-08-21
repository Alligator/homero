import random
from util import hook

@hook.command
def sbemail(inp):
  return "http://www.homestarrunner.com/sbemail%d.html" % random.randrange(1, 205)

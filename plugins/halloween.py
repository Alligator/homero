from util import hook
import re

@hook.command
@hook.command('boo')
def spook(inp, say=None, conn=None):
  say(" .-.      ")
  if inp:
    say("(o o) " + inp)
  else:
    say("(o o) boo!")
  say("| O \     ")
  say(" \   \    ")
  say("  `~~~'   ")

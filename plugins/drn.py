from util import hook
import random

def roll():
  r = random.randint(1, 6)
  if r == 6:
    return 5 + roll()
  else:
    return r

@hook.command(autohelp=False)
def drn(inp):
  ".drn -- does some nerd thing"
  return str(roll() + roll())

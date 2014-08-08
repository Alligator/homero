from util import hook

@hook.command
def yeah(inp):
  return 'woo'

@hook.command
def woo(inp):
  return 'yeah'

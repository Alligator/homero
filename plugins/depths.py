from util import hook

@hook.command
def depths(inp):
  return inp.replace('o', u'ø').encode('iso-8859-1')

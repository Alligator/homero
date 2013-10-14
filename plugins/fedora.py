from util import hook

@hook.command
def fedora(inp, say=None):
  say(unicode('     ▇▇▇▇▇▇     ', 'utf-8', 'replace'))
  say(unicode('   ▃▃▇▇▇▇▇▇▃▃   ', 'utf-8', 'replace'))
  say(unicode('    ◢┃▃╮╭▃┃◣    ', 'utf-8', 'replace'))
  say(unicode('    ◢┃╮┃┃╭┃◣ ', 'utf-8', 'replace') + inp)
  say(unicode('    ◢┃▃▆▆▃┃◣    ', 'utf-8', 'replace'))
  say(unicode('    ◢◣╰▕▍╯◢◣    ', 'utf-8', 'replace'))
  say(unicode('     ▇◣╭╮◢▇     ', 'utf-8', 'replace'))
  say(unicode('▃▅▆▇▇▇▇◣◢▇▇▇▇▆▅▃', 'utf-8', 'replace'))

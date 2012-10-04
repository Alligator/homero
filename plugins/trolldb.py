from util import hook
from random import choice
import re

# we got some serious newline problems
lines = [l for l in open('plugins/trolldb.txt', 'Ur').read().split('%') if len(l) < 500]

goonlines = [l for l in open('plugins/fatgoon.txt', 'Ur').read().split('%') if len(l) < 500]

@hook.command(autohelp=False)
def truth(inp, say=None):
    say(re.sub('\n', '', choice(lines)))
    return

@hook.command(autohelp=False)
def fatgoon(inp, say=None):
    say(re.sub('\n', '', choice(goonlines)))
    return

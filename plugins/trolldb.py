from util import hook
from random import choice
import re

lines = [l for l in open('plugins/trolldb.txt', 'r').read().split('%') if len(l) < 500]

@hook.command(autohelp=False)
def truth(inp, say=None):
    say(re.sub('\n', '', choice(lines)))
    return

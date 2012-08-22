from util import hook
from itertools import cycle

@hook.command('holidays')
@hook.command('xmas')
@hook.command
def christmas(text, say=None):
    c = cycle(['\x0304', '\x0309'])
    out = ""
    for t in text:
        out += c.next() + t
    say(out)

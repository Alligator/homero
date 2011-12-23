from util import hook
from itertools import cycle

@hook.command('holidays')
@hook.command
def christmas(text, say=None):
    c = cycle(['\x034', '\x039'])
    out = ""
    for t in text:
        out += c.next() + t
    say(out)

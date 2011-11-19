from util import hook
from datetime import datetime
from itertools import cycle, izip

taned = False

@hook.event('*')
#@hook.command
def tane(paraml, say=None):
    global taned
    today = datetime.today()
    if today.weekday() == 4 and today.hour == 18 and not taned:
        taned = True
        say(rainbow("I CAN'T WAIT"))
        say('http://tane.us/weekend.html')
        say(rainbow("FOR THE WEEKEND TO BEGIN"))

    if today.weekday() != 4:
        taned = False


def rainbow(text):
    c = cycle(['\x034', '\x037', '\x039', '\x0310', '\x036'])
    out = ""
    for t in text:
        out += c.next() + t
    return out

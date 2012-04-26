from util import hook
from random import random, choice
from time import time

last = 0
names = [
    'Mike',
    'Darv',
    'Reece',
    'Jess',
    'Tuck',
    'Matt',
    'Nate',
    'Shawn',
    'Scott',
    'Clay',
    'Bruce',
    'Chris',
]

@hook.event('PRIVMSG')
def mike(paraml, inp=None, say=None, chan=None):
    global last

    if last == 0:
        last = time()

    if 'http' in inp[1]:
        return

    if random() > 0.97 and chan == '#sa-minecraft' and time() - last > 600:
        last = time()
        say('%s, %s.' % (inp[1], choice(names)))


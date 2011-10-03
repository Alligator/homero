#!/usr/bin/env python

a = 34123

import os
import Queue
import sys
import time

sys.path += ['plugins']  # so 'import hook' works without duplication
sys.path += ['lib']
os.chdir(sys.path[0] or '.')  # do stuff relative to the install directory


class Bot(object):
    pass


bot = Bot()

print 'Loading plugins'

# bootstrap the reloader
eval(compile(open(os.path.join('core', 'reload.py'), 'U').read(),
    os.path.join('core', 'reload.py'), 'exec'))
reload_core(init=True)
config()
reload_plugs(init=True)

if not hasattr(bot, 'config'):
    exit()

print 'Connecting to IRC'

bot.conns = {}

try:
    for name, conf in bot.config['connections'].iteritems():
        if conf.get('ssl'):
            bot.conns[name] = SSLIRC(conf['server'], conf['nick'], conf=conf,
                    port=conf.get('port', 6667), channels=conf['channels'],
                    ignore_certificate_errors=conf.get('ignore_cert', True))
        else:
            bot.conns[name] = IRC(conf['server'], conf['nick'], conf=conf,
                    port=conf.get('port', 6667), channels=conf['channels'])
except Exception, e:
    print 'ERROR: malformed config file', e
    sys.exit()

bot.persist_dir = os.path.abspath('persist')
if not os.path.exists(bot.persist_dir):
    os.mkdir(bot.persist_dir)

print 'Running main loop'

last = 0

while True:

    # TIME DIFF STUFF
    call_time = False
    cur = time.time()
    if last == 0:
        last = cur
    # 10 seconds for testing.
    # gonna make it 1 min when its finished (lmao yeah right)
    if cur - last > 10:
        last = cur
        call_time = True

    reload()  # these functions only do things
    config()  # if changes have occured

    for conn in bot.conns.itervalues():
        if call_time:
            # doesnt work
            # TODO not be an idiot
            out = '420x69'
            main(conn, out)
        try:
            out = conn.out.get_nowait()
            main(conn, out)
        except Queue.Empty:
            pass
    while all(conn.out.empty() for conn in bot.conns.itervalues()):
        time.sleep(.1)
        cur = time.time()
        if cur - last > 10: break

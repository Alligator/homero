import os
import re
import random
import gc
import cPickle
import sys
import pdb
from collections import defaultdict

import objgraph
from util import hook
from guppy import hpy

@hook.command(autohelp=False)
def mem(inp):
    ".mem -- returns bot's current memory usage -- linux/windows only"

    if os.name == 'posix':
        status_file = open("/proc/%d/status" % os.getpid()).read()
        line_pairs = re.findall(r"^(\w+):\s*(.*)\s*$", status_file, re.M)
        status = dict(line_pairs)
        keys = 'VmSize VmLib VmData VmExe VmRSS VmStk'.split()
        return ', '.join(key + ':' + status[key] for key in keys)

    elif os.name == 'nt':
        cmd = "tasklist /FI \"PID eq %s\" /FO CSV /NH" % os.getpid()
        out = os.popen(cmd).read()

        total = 0
        for amount in re.findall(r'([,0-9]+) K', out):
            total += int(amount.replace(',', ''))

        return 'memory usage: %d kB' % total

    return mem.__doc__

# @hook.command(adminonly=True)
since = defaultdict(int)
@hook.event('*', limit=2)
def profile(inp, say=None, bot=None):
  global since
  print
  print '{:-^79}'.format(' memory usage ')
  print mem('')
  objgraph.show_growth()
  print
  print '{:-^79}'.format(' last called ')
  for name, c in since.iteritems():
    print '{}: {}'.format(c, name)
  print '{:-^79}'.format('')
  since = defaultdict(int)
  # print hpy().heap()[0].byvia
  # print sorted(objgraph.typestats(objgraph.get_leaking_objects()).iteritems(), key=lambda x: x[1])
  # objgraph.show_refs([x[0] for x in bot.plugs['event'] if x[1]['name'] == 'irc_msg'][0], filename='/var/www/homeromem.png', max_depth=5, refcounts=True)

@hook.sieve
def sieve_mem(bot, input, func, kind, args):
  global since
  since[args['name']] += 1
  return input

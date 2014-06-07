import os
import re
import random
import gc
import cPickle
import sys
import pdb
from collections import defaultdict, deque

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
        if inp == 'data':
          return status['VmData'].split()[0]
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
def profile():
  global since
  output = '{:-^79}'.format(' memory usage ')
  output += mem('')
  objgraph.show_growth()
  output += '{:-^79}'.format(' last called ')
  for name, c in since.iteritems():
    output += '{}: {}'.format(c, name)
  output += '{:-^79}'.format('')
  since = defaultdict(int)
  return output
  # print hpy().heap()[0].byvia
  # print sorted(objgraph.typestats(objgraph.get_leaking_objects()).iteritems(), key=lambda x: x[1])
  # objgraph.show_refs([x[0] for x in bot.plugs['event'] if x[1]['name'] == 'irc_msg'][0], filename='/var/www/homeromem.png', max_depth=5, refcounts=True)

prev = 0
calls = deque(maxlen=10)
@hook.sieve
def sieve_mem(bot, input, func, kind, args):
  global  prev, calls
  calls.append(args['name'])

  with open('memlog', 'a+') as f:
    data = int(mem('data'))
    if data > prev:
      f.write('\nmemory increase {} -> {} last calls:'.format(prev, data))
      for name in calls:
        f.write('\n  {}'.format(name))
      prev = data

  return input

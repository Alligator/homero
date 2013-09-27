import random
import string
import re
import time

from collections import defaultdict
from random import choice
from util import hook

cache = {}

token = None

def read_log_file(nick):
  reg = re.compile('\d\d:\d\d \<.([^\>]*)\> (.*)')
  f = open('/home/alligator/irclogs/synirc/#sa-minecraft.log')
  a = []
  for line in f:
    m = reg.match(line)
    if m and m.group(1) == nick:
      a.append(m.group(2))
  return a

# @hook.command(adminonly=True)
def markov(inp, say=None):
  ".imitate <account> -- use a markov text generator to imiatate a twitter account"

  lines = read_log_file(inp)

  chain = defaultdict(lambda: defaultdict(set))
  for line in lines:
    words = line.split()
    if len(words) < 1:
      continue
    prev = words[0]
    buff = []

    for i, word in enumerate(words[1:]):
      if 'http' in word:
        continue
      prev2 = tuple(buff[-2:])
      if word[-1] in '.!?':
        chain[word][None].add(0)
        buff = []
        prev = word[:-1]
      else:
        chain[prev][word].add(prev2)
        buff.append(word)
        prev = word

  word = choice(chain.keys())
  output = []
  while True:
    output.append(word)
    nxt = ''
    k = []
    for poss, hist in chain[word].items():
      n = [x for x in hist if x == tuple(output[-2:])]
      if n:
        k.append(poss)
    if len(k) > 0:
      nxt = choice(k)
    else:
      if chain[word]:
        nxt = choice(chain[word].keys())
      else:
        break
    word = nxt
    if not word:
      break
  say('<' + inp + '> ' + ' '.join(output))


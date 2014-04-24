from util import hook
import threading
import time

def bfadd(a, b):
  return (a + b) % 256

def run(prog):
  start = time.time()
  sq = map_braces(prog)
  cells = [0] * 20
  pp = 0
  cp = 0
  depth = 0
  output = ''
  while pp < len(prog):
    c = prog[pp]
    if c == '>':
      cp = bfadd(cp, 1)
    elif c == '<':
      cp = bfadd(cp, -1)
    elif c == '+':
      cells[cp] = bfadd(cells[cp], 1)
    elif c == '-':
      cells[cp] = bfadd(cells[cp], -1)
    elif c == '.':
      output += chr(cells[cp])
    elif c == ',':
      pass
    elif c == '[' and cells[cp] == 0:
      pp = sq[pp]
    elif c == ']' and cells[cp] != 0:
      pp = sq[pp]

    pp += 1
    if (time.time() - start) > 30:
      return 'program timed out'
  return output

def map_braces(prog):
  stack = []
  m = {}
  for i, c in enumerate(prog):
    if c == '[':
      stack.append(i)
    elif c == ']':
      pos = stack.pop()
      m[pos] = i
      m[i] = pos
  return m

@hook.command
def bf(inp):
  return run(inp)

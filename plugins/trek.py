from util import hook
from random import choice
import cPickle as pickle

lines = pickle.load(open('plugins/trek.pickle'))

@hook.command
def trek(inp):
    ".trek <character> <wordcount>. Characters include: Picard, Riker, Data, Worf, Geordi, Barclay, Q, Pulaski, Computer, Guinan, Troi, Beverly and Wesley. "
    try:
      char, count = inp.split()
      count = int(count)
    except ValueError:
      char = inp
      count = None

    char = char.upper()
    if char in lines:
      if count:
        if count < 1: count = 1
        o = count # store initial count
        d = -1    # search direction, lower first then higher
        while count not in lines[char]:
          count += d
          if count < 1:
            # if we didnt find anything lower, go higher
            count = o
            d = 1
        return choice(lines[char][count])
      else:
        c = choice(lines[char].keys())
        return choice(lines[char][c])

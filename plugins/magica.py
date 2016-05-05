from util import hook
from functools import partial
import random

d10 = partial(random.randint, 1, 10)

NORMAL = 1
BOTCH = 2
EXPLODE = 3

@hook.command
def ars(inp, state=NORMAL, multiplier=1):
  roll = d10()
  if len(inp) == 0: return str(roll)

  print inp, state, multiplier, roll

  if state == NORMAL:
    if roll == 10:
      return ars(inp, state=BOTCH)
    elif roll == 1:
      rolls, total = ars(inp, state=EXPLODE, multiplier=2)
      print rolls
      return '{} (1, {})'.format(total, ', '.join(rolls))
    else:
      return str(roll)

  if state == BOTCH:
    rolls = [str(d10()) for i in range(int(inp))]
    count = len(filter(lambda x: x == '10', rolls))
    b = 'botch' if count == 1 else 'botches'
    rolls.insert(0, '10')
    rolls = ['0' if i == '10' else i for i in rolls]
    if int(inp) > 0:
      return '{} {} ({})'.format(count, b, ', '.join(rolls))
    else:
      return '0'

  if state == EXPLODE:
    mroll = roll * multiplier
    if roll == 1:
      rolls, total = ars(inp, state=EXPLODE, multiplier=multiplier * 2)
      rolls.insert(0, str(roll))
      return rolls, total
    return [str(roll)], mroll

# @hook.command
# def ars_test(inp):
#   args = inp.split(' ')
#   if len(args) > 1:
#     start = int(args[1])
# 
#     def id10( a=[]):
#       if len(a) == 0:
#         a.append('a')
#         return start
#       else:
#         return random.randint(1, 10)
#       return magica_recur(args[0], start=args[1])
# 
#     global d10
#     d10 = id10 
#     return magica_recur(args[0])
#   else:
#     id10 = partial(random.randint, 1, 10)
#     global d10
#     d10 = id10 
#     return magica_recur(inp)


from util import hook
import string
import random
from datetime import datetime, date

def rotate(seed):
  random.seed(seed)
  alph = string.digits + string.letters + string.punctuation + ' '
  cyph = list(alph)
  random.shuffle(cyph)
  return alph, ''.join(cyph)

def sub(a, b, msg):
  return string.translate(msg.encode('utf-8'), string.maketrans(a, b))

@hook.command
def cipher(inp):
  "cipher isodate text -- substitution cipher based on the date. ISO dates look like this: 2013-11-13 (13th nov 2013). use decipher to, uh, decipher"
  date, msg = inp.split(' ', 1)
  try:
    d = datetime.strptime(date, '%Y-%m-%d').date().isoformat()
  except ValueError, e:
    return 'invalid date'
  a, b = rotate(d)
  print a
  print ''.join(b)
  return sub(a, b, msg)

@hook.command
def decipher(inp):
  "decipher ciphertext -- decipher ciphertext using today's date as the seed"
  d = date.today().isoformat()
  a, b = rotate(d)
  print a
  print ''.join(b)
  return sub(b, a, inp)

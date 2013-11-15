from util import hook
import re

@hook.command
def rle(inp):
  return ''.join([str(len(x[0] + x[1])) + x[0] for x in re.findall(r'(.)(\1*)', inp)])

@hook.command
def rld(inp):
  return ''.join([x[1] * int(x[0]) for x in re.findall(r'(\d+)([A-Za-z ])', inp) if int(x[0]) < 80])

@hook.command
def rlec(inp):
  return ''.join(['\x03' + '{:02}'.format(len(x[0] + x[1]) + 1) + x[0] for x in re.findall(r'(.)(\1*)', inp)])

@hook.command
def rldc(inp):
  return ''.join([x[1] * (int(x[0]) - 1) for x in re.findall('\x03(\d+)([A-Za-z ])', inp) if int(x[0]) < 80])

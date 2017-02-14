from util import hook
from random import choice
import HTMLParser
import re

jerklines = open('plugins/jerk.txt', 'Ur').readlines()
h = HTMLParser.HTMLParser()

goonlines = [l for l in open('plugins/fatgoon.txt', 'Ur').read().split('---') if len(l) < 500]

deeplines = [l.strip().split('\n') for l in open('plugins/deepthoughts.txt', 'Ur').read().split('%')]

@hook.command
def jerk(inp, say=None):
  say(h.unescape(choice(jerklines)).strip())

@hook.command(autohelp=False)
def fatgoon(inp, say=None):
    say(re.sub('\n', '', choice(goonlines)))

@hook.command
def deepthought(inp, say=None):
  c = choice(deeplines)
  say(c[0])
  say(c[1])
0


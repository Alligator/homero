from util import hook
from random import choice
import HTMLParser
import re

# we got some serious newline problems
lines = [l for l in open('plugins/trolldb.txt', 'Ur').read().split('%') if len(l) < 500]

jerklines = open('plugins/jerk.txt', 'Ur').readlines()
h = HTMLParser.HTMLParser()

goonlines = [l for l in open('plugins/fatgoon.txt', 'Ur').read().split('%') if len(l) < 500]

@hook.command(autohelp=False)
def truth(inp, say=None):
    say(re.sub('\n', '', choice(lines)))
    return

@hook.command
def jerk(inp, say=None):
  say(h.unescape(choice(jerklines)))

@hook.command(autohelp=False)
def fatgoon(inp, say=None):
    say(re.sub('\n', '', choice(goonlines)))
    return

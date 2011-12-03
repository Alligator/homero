from util import hook
from linecache import getline
from random import randint
from random import choice
f = open("plugins/lilpp_list.txt", 'r')
num_lines = len(f.readlines())
f.close()

@hook.command
def lilpp(inp, say=None):
    say("<@LilPP> i hate " + getline("lilpp_list.txt", randint(0, num_lines-1)))
    return

@hook.command
def sponge(inp, say=None):
    spongeList = [
        "crate",
        "menu",
        "shadow",
        "robot man",
        "zombie island",
        "black wrestler"
        ]
    say("<sponge-> i hate " + choice(spongeList))
    return


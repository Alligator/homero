from util import hook
from linecache import getline
from random import randint

f = open("plugins/lilpp_list.txt", 'r')
num_lines = len(f.readlines())
f.close()

@hook.command
def lilpp(inp):
    return "i hate " + getline("lilpp_list.txt", randint(0, num_lines-1))



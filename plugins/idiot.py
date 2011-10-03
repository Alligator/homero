from util import hook

@hook.command
def idiot(inp, say=None):
    say(inp + ' is an idiot')


from util import hook

@hook.regex('weed')
def weed(inp, say=None):
    say('420')
    return
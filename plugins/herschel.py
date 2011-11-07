from util import hook

@hook.regex('weed')
def weed(inp, say=None):
    say('420')
    return

@hook.regex('420')
def fourtwenty(inp, say=None): say('weed')

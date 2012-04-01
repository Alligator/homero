from util import hook

# @hook.regex('w.*e.*e.*d')
def weed(inp, say=None):
    say('420')
    return
# @hook.regex('4.*2.*0|four.*twenty')
def fourtwenty(inp, say=None): say('weed')

@hook.regex('anime')
def anime(inp, say=None):
    say(unicode('I think you mean animé', 'utf-8'))
    return

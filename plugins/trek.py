from util import hook
from treksum import treksum


@hook.command
def trek(inp):
    ".trek <character> <wordcount>. Characters include: Picard, Riker, Data, Worf, Geordi, Barclay, Q, Pulaski, Computer, Guinan, Troi, Beverly and Wesley. "
    characters = ['picard', 'riker', 'data', 'worf', 'geordi', 'barclay', 'q', 'pulaski', 'computer', 'guinan', 'troi', 'beverly', 'wesley']
    if inp.lower().split(' ')[0] in characters:
        count = None
        for x in inp.split():
            try:
                count = int(x)
            except ValueError:
                character = x.lower()
        r = treksum.generate_sentence(word_count=count, character=character)
        return r


@hook.command
def picard(inp):
    return trek('picard %s' % inp)


@hook.command
def riker(inp):
    return trek('riker %s' % inp)


@hook.command
def data(inp):
    return trek('data %s' % inp)


@hook.command
def worf(inp):
    return trek('worf %s' % inp)


@hook.command
def geordi(inp):
    return trek('geordi %s' % inp)


@hook.command
def barclay(inp):
    return trek('barclay %s' % inp)


@hook.command
def q(inp):
    return trek('q %s' % inp)


@hook.command
def pulaski(inp):
    return trek('pulaski %s' % inp)


@hook.command
def computer(inp):
    return trek('computer %s' % inp)


@hook.command
def guinan(inp):
    return trek('guinan %s' % inp)


@hook.command
def troi(inp):
    return trek('troi %s' % inp)


@hook.command
def beverly(inp):
    return trek('beverly %s' % inp)


@hook.command
def wesley(inp):
    return trek('wesley %s' % inp)



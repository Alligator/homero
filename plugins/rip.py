from util import hook, strip_formatting

@hook.command
def rip(inp, say=None):
    inp = inp.encode('utf-8')
    topfiller = str.center('', len(strip_formatting.strip(inp))-3, '-')

    top = '  _.' + topfiller + '-._\n'

    width = len(top)-3

    rip = ' |' + str.center('RIP', width) + '|\n'
    nmr = ' |' + str.center(inp.upper(), width) + '|\n'
    lsr = ' |' + str.center('', width, '_') + '|\n'
    btm = '|' + str.center('', width+2, '_') + '|'

    headstone = [top, rip, nmr, lsr, btm]
    for l in headstone:
        say(l)

@hook.command
def bread(inp, say=None):
    inp = str(inp)
    topfiller = str.center('', len(strip_formatting.strip(inp))-5, '-')

    top = '  .' + topfiller + '-.\n'

    width = len(top)-3

    rip = ' |' + str.center('', width) + '|\n'
    nmr = ' |' + str.center(inp.upper(), width) + '|\n'
    lsr = ' |' + str.center('', width, '_') + '|\n'

    headstone = [top, rip, nmr, lsr]
    for l in headstone:
        say(l)

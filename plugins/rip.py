from util import hook

@hook.command
def rip(inp, say=None):
    inp = str(inp)
    topfiller = str.center('', len(inp)-3, '-')

    top = '  _.' + topfiller + '-._\n'

    width = len(top)-3

    rip = ' |' + str.center('RIP', width) + '|\n'
    nmr = ' |' + str.center(inp.upper(), width) + '|\n'
    lsr = ' |' + str.center('', width, '_') + '|\n'
    btm = '|' + str.center('', width+2, '_') + '|'

    headstone = [top, rip, nmr, lsr, btm]
    for l in headstone:
        say(l)

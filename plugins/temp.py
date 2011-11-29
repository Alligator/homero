from util import hook

@hook.command
def temp(inp):
    ".temp <temp> -- converts <temp> from C to F and F to C"
    try:
        temp = float(inp)
    except:
        #return inp.replace('u', '').replace('s', 'z')
        return 'vinic is a busta'
    if abs(temp) == 420:
        return "SMOKE WEED EVERY DAY DONT GIVE A FUCK"
    if abs(temp) > 150:
        return "2 hot 4 u"
    c = (temp - 32) * (5.0/9.0)
    f = (temp * (9.0/5.0)) + 32
    return "{0:3.1f}F is {1:3.1f}C. {0:3.1f}C is {2:3.1f}F.".format(temp, c ,f)

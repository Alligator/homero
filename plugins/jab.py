from util import hook

fancy = u"\u0B9C\u06E9\u06DE\u06E9\u0B9C"
fill = u"\u25AC"

@hook.command
def jab(inp):
    if len(inp) > 96:
        return
    out = ''
    for c in inp:
        if ord(c) <= 31:
            out += c
            continue
        if ord(c) == 32:
            out += "  "
            continue
        if ord(c) > 176:
            continue
        uni = ord(c) + 65248
        out += unichr(uni)
    return out

@hook.command
def bigjab(inp, say=None):
    s = jab(inp)
    if s == "":
        return
    k = s.replace("  ", " ")
    f = fancy.center(len(k)*2, fill)
    say(f)
    say(s)
    say(f)

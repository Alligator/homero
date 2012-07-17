from util import hook

fancy = u"\u0B9C\u06E9\u06DE\u06E9\u0B9C"
fill = u"\u25AC"

@hook.command
def jab(inp):
    if len(inp) == 0: return
    passchars = [2, 15, 18, 29, 31, 32]
    if len(inp) > 96:
        return
    out = ''
    bold = False
    e = enumerate(inp)
    for i, c in e:
        if ord(c) == 3:
            out += c
            out += inp[i+1]
            if inp[i+2].isdigit():
                out += inp[i+2]
                e.next()
            e.next()
        elif ord(c) in passchars:
            out += c
        elif ord(c) <= 31:
            out += c
        elif ord(c) > 176:
            continue
        else:
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

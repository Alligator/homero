from util import hook
import re

#@hook.regex('butt', re.I)
def butt(inp, msg=None, chan=None):
    if chan != '#butt':
        return
    print inp.groups
    out = '<html>%s</html>' % msg
    f = open(r'C:\Users\Reece\Documents\XAMPP\xampp\htdocs\butt.html', 'w')
    f.write(out)
    return

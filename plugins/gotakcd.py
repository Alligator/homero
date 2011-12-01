from util import hook
import re

xkcd_regex = (r'.*xkcd.com/(.+)/', re.I)

@hook.regex(*xkcd_regex)
def xkcd(match, say=None):
    say('http://goatkcd.com/%s/sfw' % match.group(1))
    return

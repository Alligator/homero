from util import hook
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
import urllib2

@hook.command
def glitch(inp):
    '.glitch url chance amount seed -- http://glitch.goonscape.org/'
    url, chance, amount, seed = inp.split()
    register_openers()
    datagen, headers = multipart_encode({'url': url,
        'chance': chance,
        'datalength': amount,
        'randseend': seed})
    request = urllib2.Request('http://glitch.goonscape.org', datagen, headers)
    conn = urllib2.urlopen(request)
    print conn.read()
    conn.close()

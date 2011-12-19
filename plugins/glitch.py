from util import hook
from poster import encode
from poster.streaminghttp import register_openers
from itertools import izip_longest
import urllib2

@hook.command
def glitch(inp):
    '.glitch url chance amount seed -- http://glitch.goonscape.org/'
    # ok im gonna forget what the heck i was doin here by tomorrow so lets write a proper comment
    # split the params from inp but make them '' if they aren't there!!
    p = izip_longest(('url', 'chance', 'datalength', 'randseed'), inp.split(), fillvalue='')
    params = [a for a in p]

    register_openers()
    boundary = encode.gen_boundary()

    f = encode.MultipartParam('file', '', filename=' ', filetype='application/octet-stream')
    params.insert(0, f)

    datagen, headers = encode.multipart_encode(params, boundary)
    request = urllib2.Request('http://glitch.goonscape.org', datagen, headers)
    return urllib2.urlopen(request).geturl()

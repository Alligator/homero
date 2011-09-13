# alligate
from util import hook
import urllib, httplib

@hook.command
def barbra(inp):
    '.barbra <text> -- gobarbra.com idk'
    params = urllib.urlencode({'glos': 'gb_brian', 'tresc': inp})
    headers = {'Content-type': 'application/x-www-form-urlencoded',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
              }
    conn = httplib.HTTPConnection('gobarbra.com')
    conn.request('POST', '/tworz-hit', params, headers)
    response = conn.getresponse()
    url = response.getheader('location')
    conn.close()
    return 'http://gobarbra.com' + url

# alligator
# actual pigtales stuff by lilpp
from util import hook, http
from collections import defaultdict
from time import time
import httplib
import urllib
import re

try:
    cache
except:
    print "renewed pig cache"
    cache = defaultdict(list)
buffer_max = 10 # max last 10 messages in chan
timeout = 2*60  # 5 minute timeout before cache is cleared

@hook.event('PRIVMSG', ignorebots=False)
def line(paraml, input=None, db=None, bot=None):
    global cache
    #cache[chan][0] = [last_msg_time]
    chan = input['chan']
    nick = input['nick']
    msg = input['msg']

    if msg.startswith('.') or msg.startswith('!'):
        return

    try:
        cache[chan][0]
    except:
        cache[chan] = [time()]

    # cache clear timeout
    diff = time() - cache[chan][0]
    if diff > timeout:
        cache[chan] = [time()]

    # no commands ew gros
    cache[chan].append((nick, msg))

    if len(cache[chan]) > buffer_max:
        cache[chan] = cache[chan][-buffer_max:]
        cache[chan][0] = time()

@hook.command(autohelp=False)
def pig(inp, nick='', chan=''):
    '.pig [channel] -- pigtales.minecraft.net m8'
    if not len(inp) == 0:
        chan = inp
    msgs = [m for n, m in cache[chan][1:]]
    # clear cache
    cache[chan] = []

    if msgs == []:
        return
    return postAndLink(buildParams("im gay","alligate",msgs[:-1],msgs[-1]))

def grabAuth():
    pigtalesPage = urllib.urlopen("http://pigtales.minecraft.net/add")
    pageBuffer = pigtalesPage.read()
    pigtalesPage.close()
    authRegex = re.compile('<input type="hidden" name="authenticity_token" value="([^"]+)"/>')
    authCode = authRegex.search(pageBuffer).group(1)
    del pageBuffer, pigtalesPage, authRegex
    return authCode

def buildParams(title,created,lines,lastline):
    pigParams = urllib.urlencode({'authenticity_token': grabAuth(),'title': title,'created_by': created})
    for i in range(len(lines)):
         #why wont this concat normally, i am very angry!!! >:(
         pigParams += "&"
         pigParams += urllib.urlencode({'lines[%d]' % i: lines[i].encode('utf-8')})
    pigParams += "&"
    pigParams += urllib.urlencode({'last_line': lastline})
    del title,created,lines,lastline
    return pigParams

def postAndLink(params):
    #Build appropriate header for dumb websight
    pigHeaders = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"}
    #connect, build request, post that bitch, smoke a blunt
    pigConnection = httplib.HTTPConnection("pigtales.minecraft.net")
    pigConnection.request("POST","/add",params,pigHeaders)
    pigResponse = pigConnection.getresponse()
    pigData = pigResponse.read()
    #parse me a blunt har har har
    hrefRegex = re.compile('<a href="([^"]+)">')
    pigLink = hrefRegex.search(pigData).group(1)
    del pigHeaders,pigConnection,pigResponse,pigData,hrefRegex
    return pigLink

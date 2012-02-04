import simplejson as json
import random
from util import hook
from util import http

import urllib,urllib2,json

@hook.command
def hitze(inp):
    hitzelist = [
      "ahahaaha",
      "kinda lol",
      "lol",
      "fucking complex",
      "heh",
      "omg.",
      "uugh",
      "why..",
      "lol pcgaming",
      "rip"
    ]

    subreddit = [
    "pics",
    "funny",
    "wtf",
    "minecraft",
    "cars",
    "bitcoin",
    "fffffffuuuuuuuuuuuu",
    "gifs",
    "tf2",
    ]

    noSelf = False
    while noSelf == False:
        jsonData = http.get_json('http://www.reddit.com/r/' + random.choice(subreddit) + '/.json')
        potentialURL = random.choice(jsonData['data']['children'])['data']['url']
        if 'reddit' in potentialURL:
            noSelf = False
        else:
            noSelf = True

    return "<@hitzler> " + potentialURL + " " + random.choice(hitzelist)

def checkURL(url):
    params = urllib.urlencode({'q':'url:' + url})
    url = "http://www.reddit.com/search.json?%s" % params
    jsan = json.load(urllib2.urlopen(url))
    if len(jsan['data']['children']) > 0:
        return True
    return False


#@hook.event('PRIVMSG')
def hitze_event(paraml, say=None, nick=None):
    if 'hitz' in nick.lower() and 'http://' in paraml[1]:
        if checkURL(paraml[1]):
            say('/!\\ REDDIT ALERT /!\\ REDDIT ALERT /!\\ PLEASE DISREGARD THE PREVIOUS MESSAGE. WE APOLOGISE FOR ANY LIBERTARIANS ENCOUNTERED')

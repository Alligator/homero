import simplejson as json
import random
from util import hook
from util import http

@hook.command
def hitze(inp):
    hitzelist = [
      "ahahaaha",
      "rofl, epic",
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
    "terraria",
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
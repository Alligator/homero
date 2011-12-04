from util import hook, http
from urllib2 import HTTPError
import random
import collections

#@hook.command
def imitate(inp):
    ".imitate <account> -- use a markov text generator to imiatate a twitter account"
    url = "http://api.twitter.com/1/statuses/user_timeline/%s.json?count=200" % inp
    try:
        tweets = [t['text'] for t in http.get_json(url)]
    except HTTPError:
        return "/!\\ either you or twitter is dumb but something is wrong and this didnt work sorry!!!! /!\\"

    # learn that text
    # omg markov chains
    suffixes = collections.defaultdict(list)
    w1 = ""
    w2 = ""
    for tweet in tweets:
        for word in tweet.split():
            if '@' in word: break
            if '#' in word: break
            suffixes[(w1, w2)].append(word)
            w1, w2 = w2, word
        w1 = ""
        w2 = ""
    suffixes[(w1, w2)].append("")

    # now make a reply
    w1 = ""
    w2 = ""
    out = ""
    for i in range(20):
        sf = suffixes[(w1, w2)]
        try:
            next = random.choice(sf)
        except IndexError:
            break
        if next is "":
            break
        out += next + " "
        w1, w2 = w2, next

    if out: return out

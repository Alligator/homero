from util import hook, http
from urllib2 import HTTPError, unquote
import random
import collections

@hook.command
def imitate(inp):
    ".imitate <account> -- use a markov text generator to imiatate a twitter account"
    url = "http://api.twitter.com/1/statuses/user_timeline/%s.json?count=100" % inp
    try:
        tweets = [t['text'] for t in http.get_json(url)]
    except HTTPError, e:
        if e.code == 404:
            return "user not found"
        else:
            print e.code
            return

    # learn that text
    # omg markov chains
    suffixes = collections.defaultdict(list)
    w1 = ""
    for tweet in tweets:
        for word in tweet.split():
            word = unquote(word)
            if '@' in word: break
            if '#' in word: break
            suffixes[w1].append(word)
            w1 = word
        w1 = ""
    suffixes[w1].append("")

    # now make a reply
    w1 = ""
    out = ""
    for i in range(20):
        sf = suffixes[(w1)]
        try:
            next = random.choice(sf)
        except IndexError:
            break
        if next is "":
            break
        out += next + " "
        w1 = next

    if out: return out

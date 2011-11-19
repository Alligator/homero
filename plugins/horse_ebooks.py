from util import hook, http
import time

url = "http://api.twitter.com/1/statuses/user_timeline/Horse_ebooks.json?count=1"

last = time.time()
last_tweet = http.get_json(url)[0]['text']

@hook.event('*')
def horse(inp, conn=None):
    global last, url, last_tweet
    print last
    if time.time() - last > 240:
        j = http.get_json(url)
        tweet = j[0]['text']
        if tweet == last_tweet:
            return
        conn.cmd('PRIVMSG #sa-minecraft Horse_ebooks: %s' % tweet)
        last_tweet = tweet
        last = time.time()

@hook.command('horse', autohelp=False)
def horse_cmd(inp, say=None):
    global url, last, last_tweet
    if time.time() - last > 120:
        last = time.time()
        last_tweet = http.get_json(url)[0]['text']
    say('Horse_ebooks: %s' % last_tweet)

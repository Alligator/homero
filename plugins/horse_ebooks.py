from util import hook, http
import time

def get_tweet():
    url = "http://api.twitter.com/1/statuses/user_timeline/Horse_ebooks.json?count=1"
    return http.get_json(url)[0]['text'].replace('\n', ' ')

last = time.time()
last_tweet = get_tweet()

@hook.event('*')
def horse(inp, conn=None):
    global last, url, last_tweet
    if time.time() - last > 240:
        last = time.time()
        tweet = get_tweet()
        if tweet == last_tweet:
            return
        conn.cmd('PRIVMSG #sa-minecraft Horse_ebooks: %s' % tweet)
        last_tweet = tweet

@hook.command('horse', autohelp=False)
def horse_cmd(inp, say=None):
    global url, last, last_tweet
    if time.time() - last > 120:
        last = time.time()
        last_tweet = get_tweet()
    say('Horse_ebooks: %s' % last_tweet)

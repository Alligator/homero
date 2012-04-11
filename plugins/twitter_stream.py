import tweetstream
from util import hook

username = ''
password = ''
#          Horse       Goons      Reddit     Notch
dummies = [174958347, 413248051, 489467009, 63485337]

@hook.event('001')
def stream(inp, conn=None):
    stream = tweetstream.FilterStream(username, password, follow=dummies)
    for tweets in stream:
        if tweets['user']['id'] in dummies:
            conn.cmd('PRIVMSG #sa-minecraft @%s: %s - http://twitter.com/#!/%s/status/%s' % (tweets['user']['screen_name'], tweets['text'], tweets['user']['screen_name'], tweets['id']))
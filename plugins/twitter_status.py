from util import hook, http
from twython import Twython

twitter_re_status = r"(?i)twitter\.com/(?:#!/)?(\S+)/status/(\S+)"
token = None

def init(key, secret):
  global token
  if not token:
    token = Twython(key, secret, oauth_version=2).obtain_access_token()

@hook.regex(twitter_re_status)
def twitter_status(match, bot=None):
  global token
  id = match.group(2)

  init(bot.config['api_keys']['twitter_key'], bot.config['api_keys']['twitter_secret'])
  twitter = Twython(bot.config['api_keys']['twitter_key'], access_token=token)
  result = twitter.show_status(id=id)

  at_name = result['user']['screen_name']
  full_name = result['user']['name']
  tweet_text = result['text'].replace('\n', ' ')

  return "\x02@" + at_name + " \x02(" + full_name + ") - " + tweet_text

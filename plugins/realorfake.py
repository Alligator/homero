import random
from util import hook, http
from twython import Twython
from lxml import html
from time import sleep

token = None

def init(key, secret):
  global token
  if not token:
    token = Twython(key, secret, oauth_version=2).obtain_access_token()

users = {}
current_chan = ''
running = False

@hook.command
def vice(inp, bot=None, db=None, say=None, chan=None):
  def real():
    h = http.get_xml('http://www.vice.com/rss')
    item = random.choice(h.xpath('//item'))
    msg = item.xpath('title')[0].text
    url = item.xpath('link')[0].text
    return msg, url

  def fake():
    global token
    init(bot.config['api_keys']['twitter_key'], bot.config['api_keys']['twitter_secret'])
    twitter = Twython(bot.config['api_keys']['twitter_key'], access_token=token)
    j = twitter.get_user_timeline(screen_name='Vice_Is_Hip', count=100)
    tweet = random.choice(j)
    msg = tweet['text']
    url = 'https://twitter.com/Vice_Is_Hip/status/' + tweet['id_str']
    return msg, url
  realorfake(real, fake, say, db, chan)

def realorfake(real, fake, say, db, chan):
  global current_chan, users, running
  if running: return
  users = {}
  current_chan = chan
  running = True
  if random.random() > 0.5:
    msg, url = real()
    real = True
  else:
    msg, url = fake()
    real = False
  say(msg)
  sleep(20)
  round_end(real, url, say, db)
  running = False

@hook.command
def upworthy(inp, bot=None, db=None, say=None, chan=None):
  def real():
    h = http.get_html('http://www.upworthy.com/random')
    msg = h.xpath('//*[@id="nuggetContent"]/header/h1')[0].text
    url = h.xpath('/html/head/link[6]')[0].attrib['href']
    return msg, url

  def fake():
    global token
    init(bot.config['api_keys']['twitter_key'], bot.config['api_keys']['twitter_secret'])
    twitter = Twython(bot.config['api_keys']['twitter_key'], access_token=token)
    j = twitter.get_user_timeline(screen_name='UpWorthIt', count=100)
    tweet = random.choice(j)
    msg = tweet['text']
    url = 'https://twitter.com/UpWorthIt/status/' + tweet['id_str']
    return msg, url
  realorfake(real, fake, say, db, chan)

def round_end(real, url, say, db):
  global users
  if real: say('that was real ' + url)
  else   : say('that was fake ' + url)
  db.execute("create table if not exists realorfake(nick primary key, tries, wins)")
  correct = []
  for nick, guess in users.iteritems():
    stat = db.execute("select tries, wins from realorfake where nick=lower(?)",
                     (nick,)).fetchone()
    if stat:
      tries, wins = stat
    else:
      tries, wins = 0, 0

    tries += 1
    if guess == real:
      wins += 1
      correct.append(nick + ' (' + str(int(wins/float(tries)*100)) + '%)')
    db.execute("insert or replace into realorfake(nick, tries, wins) values (?,?,?)",
               (nick.lower(), tries, wins))

  db.commit()
  if len(correct) == 0:
    say('no-one got it right, wow')
  else:
    say(', '.join(correct) + ' got it right, gj')

@hook.command
def realstats(inp, db=None, say=None, nick=None):
  me = db.execute("select tries, wins from realorfake where nick=lower(?)", (nick,))
  users = db.execute("select * from realorfake").fetchall()
  if me:
    tries, wins = me.fetchone()
    say('you: ' + nick + ' (' + str(wins) + '/' + str(tries) + ' - ' + str(int(wins/float(tries)*100)) + '%)')
  users.sort(key=lambda x: x[2]/x[1], reverse=True)
  say('top 5 users who have played at least 3 times')
  i = 0
  for (nick, tries, wins) in users:
    if i >= 5: break
    if tries > 3:
      say(str(i+1) + '. ' + nick + ' (' + str(wins) + '/' + str(tries) + ' - ' + str(int(wins/float(tries)*100)) + '%)')
      i += 1

@hook.event('PRIVMSG')
def rof_msg(paraml, nick=None, chan=None):
  global running, current_chan
  if not running or chan != current_chan:
    return
  msg = paraml[1]
  if nick in users: return
  if   msg.lower() == 'fake': users[nick] = False
  elif msg.lower() == 'real': users[nick] = True

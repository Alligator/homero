from util import hook
from fuzzywuzzy import process, fuzz

choices = []
threshold = 65

#@hook.event('PRIVMSG')
def nick_matcher(inp, chan=None, nick=None):
  global choices
  # if chan != '#sa-minecraft': return
  with open('nick_watcher.log', 'a') as f:

    if len(choices) == 0:
      f.write('choices empty, adding {}\n'.format( nick))
      choices.append(nick)
      return

    poss = process.extractOne(nick, choices, scorer=fuzz.QRatio)
    if poss[1] > threshold:
      if poss[1] != 100:
        f.write('{} matched to {} match = ({})\n'.format(nick, poss[0], poss[1]))
    else:
      f.write('{} not matched, added to choices. closest match was {} ({})\n'.format(nick, poss[0], poss[1]))
      choices.append(nick)

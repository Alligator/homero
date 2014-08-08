# alligator
import re
from util import hook

# dub_url = "http://tubedubber.com/#%s:%s:0:100:0:%s:1"
dub_url = "http://lildub.me/?v=%s&vs=0&a=%s&as=0"
whale_url = "http://www.youtube.com/watch?v=ZS_6-IwMPjM"
cow_url = "http://www.youtube.com/watch?v=lXKDu6cdXLI"
lawn_url = "http://www.youtube.com/watch?v=r6FpEjY1fg8"

# sw8 regex by commonwealth bro lilpp
yre = "(?:http|https)://(?:www\.)?(?:youtube\.com/watch\?v=|youtu\.be/)([^&\n]+)"

@hook.command
def lawnmower(inp): return dub(lawn_url + " " + inp)

@hook.command
def whale(inp): return dub(whale_url + " " + inp)

@hook.command
def cow(inp): return dub(cow_url + " " + inp)

@hook.command
def dub(inp):
    '.dub <vid> <audio> [audio start time] -- tubedubber'
    ar = inp.split(" ")
    time = 0
    if len(ar) == 3:
        time = ar[2]
    vid = re.match(yre, ar[0]).group(1)
    audio = re.match(yre, ar[1]).group(1)
    return dub_url % (vid, audio)

@hook.command
def worldstar(inp):
  sp = inp.split(' ')
  if len(sp) > 1:
    vid = re.match(yre, sp[0]).group(1)
    try:
      time = int(sp[1])
    except ValueError:
      return 'that is not a time'
  else:
    vid = re.match(yre, inp).group(1)
    time = 0
  return 'http://www.youdubber.com/index.php?video={}&video_start={}&audio=uEgtNSBa4Zk&audio_start=0'.format(vid, time)

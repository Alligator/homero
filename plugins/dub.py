# alligator
import re
from util import hook

dub_url = "http://tubedubber.com/#%s:%s:0:100:0:%s:1"
whale_url = "http://www.youtube.com/watch?v=ZS_6-IwMPjM"
cow_url = "http://www.youtube.com/watch?v=lXKDu6cdXLI"

# sw8 regex by commonwealth bro lilpp
yre = "http://(?:www\.)?(?:youtube\.com/watch\?v=|youtu\.be/)([^&\n]+)"

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
    return dub_url % (vid, audio, time)

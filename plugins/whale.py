# alligator
import re
from util import hook

vid_url = "http://tubedubber.com/#ZS_6-IwMPjM:%s:0:100:0:%s:1"
s_url = "http://tubedubber.com/#1lKZqqSI9-s:%s:0:100:0:%s:1"
# sw8 regex by commonwealth bro lilpp
yre = "http://(?:www\.)?(?:youtube\.com/watch\?v=|youtu\.be/)([^&\n]+)"

@hook.command
def whale(inp):
    '.whale <youtube video> [audio start time] -- alligator made whale'
    ar = inp.split(" ")
    time = 0
    if len(ar) == 2:
        time = ar[1]
    vid = ""
    m = re.match(yre, ar[0])
    vid = m.group(1)
    return vid_url % (vid, time)

@hook.command('911')
def sept(inp):
    '.911 <youtube video> [audio start time] -- yep'
    ar = inp.split(" ")
    time = 0
    if len(ar) == 2:
        time = ar[1]
    vid = ""
    m = re.match(yre, ar[0])
    vid = m.group(1)
    return s_url % (vid, time)

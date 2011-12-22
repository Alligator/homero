# a bunch of stuff in here is stolen from youtube.py and seen.py
# in the skybot repo. thnx yo.
# https://github.com/rmmh/skybot/tree/master
from util import hook, http
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
import urllib2
import time
import re

youtube_re = (r'(?:youtube.*?(?:v=|/v/)|youtu\.be/|yooouuutuuube.*?id=)'
                      '([-_a-z0-9]+)', re.I)
url = 'http://gdata.youtube.com/feeds/api/videos/%s?v=2&alt=jsonc'
video_url = "http://youtu.be/%s"

# nicked from youtube.py
def get_video_title(vid_id):
    j = http.get_json(url % vid_id)

    if j.get('error'):
        return

    j = j['data']

    return j['title']

def format_vid(vidin, bold):
    vid     = video_url % vidin[0]
    title   = vidin[1]
    user    = vidin[2]
    ti      = time.ctime(vidin[3])
    if bold:
        out = '\x02%s - %s\x02 posted by %s on %s' % (vid, title, user, ti)
    else:
        out = '%s - %s posted by %s on %s' % (vid, title, user, ti)
    return out

def db_init(db):
    db.execute('create table if not exists ytmemory(vid, title, user, time, chan,'
               'primary key(vid, chan))')
    db.commit()

@hook.regex(*youtube_re)
def seeninput(match, input=None, db=None, say=None):
    db_init(db)
    vid = match.group(1)
    db.execute('insert or ignore into ytmemory(vid, title, user, time, chan)'
               'values(?,?,?,?,?)', (vid, get_video_title(vid),
                input.nick.lower(), time.time(), input.chan))
    db.commit()

@hook.command
def yt(inp, nick=None, chan=None, db=None):
    '.yt query|hh -- searches youtube links posted in channel. matches usernames and video titles'
    db_init(db)

    try:
        # we got a time
        int(inp)
        # q is a time in hours. we need dis in seconds
        q = time.time() - (int(inp) * 60 * 60)
        vids = db.execute("select vid, title, user, time from ytmemory"
                " where time > ? and chan=?",
                (q, chan))
    except:
        # we got a query
        q = '%' + inp + '%'
        vids = db.execute("select vid, title, user, time from ytmemory"
                " where (title like ? or user like ?) and chan = ?",
                (q, q, chan))

    if vids:
        vid_list = vids.fetchall()
    else:
        return 'no matches'

    if not vid_list:
        return 'no matches'

    if len(vid_list) > 1:
        out = ''
        for v in vid_list: out += format_vid(v, False) + '\n'

        register_openers()
        datagen, headers = multipart_encode({'sprunge': out})
        request = urllib2.Request('http://sprunge.us', datagen, headers)
        return urllib2.urlopen(request).read()
    else:
        return format_vid(vid_list[0], True)

from util import hook
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
import urllib2

def db_init(db):
    db.execute('create table if not exists topichistory(topic, channel,'
               'primary key(topic, channel))')
    db.commit()

# get the topic on join and change
@hook.event('TOPIC 332')
def addtopic(paraml, nick=None, chan=None, db=None):
    topic = "%s changed the topic to %s" %(nick, paraml[-1])
    db_init(db)
    db.execute('insert or replace into topichistory(topic, channel)'
               'values(?,?)', (topic, chan))
    db.commit()

@hook.command(autohelp=False)
def topic(inp, chan=None, db=None):
    db_init(db)
    if len(inp) > 0:
        chan = inp
    topics = db.execute('select topic from topichistory'
                        ' where channel=?', (chan,))

    t = topics.fetchall()
    if not t:
        return "no previous topics found"

    t = [topic[0] for topic in t]
    t.reverse()
    out = '\n\n'.join(t)

    register_openers()
    datagen, headers = multipart_encode({'sprunge': out})
    request = urllib2.Request('http://sprunge.us', datagen, headers)
    return urllib2.urlopen(request).read()

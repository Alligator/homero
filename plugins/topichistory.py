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
def addtopic(paraml, chan=None, db=None):
    topic = paraml[-1]
    db_init(db)
    db.execute('insert or replace into topichistory(topic, channel)'
               'values(?,?)', (topic, chan))
    db.commit()

@hook.command(autohelp=False)
def topic(inp, chan=None, db=None):
    topics = db.execute('select topic from topichistory'
                        ' where channel=?', (chan,))
    if not topics:
        return 'no previous topics saved'

    t = topics.fetchall()
    out = ""
    for topic in t:
        out += topic[0] + '\n'

    register_openers()
    datagen, headers = multipart_encode({'sprunge': out})
    request = urllib2.Request('http://sprunge.us', datagen, headers)
    return urllib2.urlopen(request).read()

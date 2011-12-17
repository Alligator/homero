# yeah it's bad but fuck you it works and you prob wont be able to do it any better (owned)
# specify first argument of bot.py to be the port number u want

import web
import thread
import json
import pprint
from util import hook, http

webSql = web.database(dbn='sqlite',db='./persist/homero.irc.synirc.net.db')
urls = (
    '/ythistory', 'ythistory',
    )
app = web.application(urls, globals())

class ythistory:
    def GET(self):
    	data = web.input(q="")

        q = '%' + data.q + '%'

        if data.q:
            result = webSql.select('ytmemory', where='title like $q or user like $q or chan like $q order by time desc', vars={'q':q})
        else:
            result = webSql.select('ytmemory')

        return json.dumps([i for i in result])
    	

def runServer():
	app.run()

thread.start_new_thread(runServer, ())

# yeah it's bad but fuck you it works and you prob wont be able to do it any better (owned)
# specify first argument of bot.py to be the port number u want

import web
import thread
import json
import pprint
from util import hook, http

webSql = web.database(dbn='sqlite',db='./persist/homero2.irc.synirc.net.db')
urls = (
    '/ythistory', 'ythistory',
    )
app = web.application(urls, globals())

class ythistory:
    def GET(self):
    	data = web.input(channel="",username="")
    	# ugly, u do it better tho bitch??
    	query = ''
    	if data.channel:
    		query += ' chan = $channel '
    	if data.username:
    		if data.channel:
    			query += ' AND user = $user'
    		else:
    			query += ' user = $user'

    	if query:
    		result = webSql.select('ytmemory',order="time DESC",vars={'channel': '#' + data.channel,'user':data.username},where=query)
    	else:
    		result = webSql.select('ytmemory',order="time DESC")

        return json.dumps([i for i in result])
    	

def runServer():
	app.run()

thread.start_new_thread(runServer, ())

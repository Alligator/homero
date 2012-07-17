from util import hook, http
import random

@hook.command
def openbook(inp, say=None):
	''' .openbook <term> -- Returns a random openbook post for the term. '''
	url = 'https://graph.facebook.com/search'
	results = http.get_json( url, q=inp, type="post" )
	results = results["data"]
	result = random.choice(results)
	if result.has_key("message"):
		name = result["from"]["name"].encode("utf8", "ignore")
		message =  result["message"].encode("utf8", "ignore")
		profile_link = result["from"]["id"].encode("utf8", "ignore")
		say("\x0307%s\x0F: %s" % (name.encode('ascii' ,'ignore'), message.encode('ascii', 'ignore')))
		say("\x0309Profile Link\x0F: http://facebook.com/profile.php?id=%s&v=wall" % (profile_link))

if __name__ == "__main__":
	print openbook("gay")
	print openbook("queef")

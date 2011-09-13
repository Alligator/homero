# alligator
import random
from util import hook, http

search_url = "https://gdata.youtube.com/feeds/api/videos?v=2&alt=jsonc&category=los%2Csimpsons&max-results=1&start-index="
yt_url = "http://youtu.be/%s/"

@hook.command(autohelp=False)
def homero(inp):
    '.homero <query> -- los simpsons?'
    start = random.randint(1, 20)
    j = http.get_json(search_url + str(start))

    if j['data']['totalItems'] == 0:
        return 'no results found'

    title = j['data']['items'][0]['title']
    vid = j['data']['items'][0]['id']
    return title + ' - ' + yt_url % vid

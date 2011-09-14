import simplejson as json
import random
import http

@hook.command
def hitze(inp):
    hitzelist = [
      "ahahaaha",
      "rofl, epic",
      "omg.",
      "uugh",
      "why..",
      "lol pcgaming",
      "rip"
    ]

    jsonData = http.get_json('http://www.reddit.com/r/funny+pics+cars+cartalk+geek+xbox+gaming+minecraft+terraria/.json')

    return "<@hitzler> " + random.choice(jsonData['data']['children'])['data']['url'] + " " + random.choice(hitzelist)
from util import hook
import requests
import json

@hook.command
def clojure(inp):
  result = json.loads(requests.get('http://www.tryclj.com/eval.json', params={'expr': inp}).text)
  if 'error' in result:
    return '\x0305' + result['message']
  else:
    return result['result']

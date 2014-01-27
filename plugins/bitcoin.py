from util import http, hook
import math

prev = []
def get_bitcoin():
  data = http.get_json("https://www.bitstamp.net/api/ticker/")
  t = {
    'low':  float(data['low']),
    'high': float(data['high']),
    'avg':  float(data['last']),
  }
  return t

@hook.event('*', limit=5)
def bit_event(paraml):
  global prev
  t = get_bitcoin()
  prev.append(t['avg'])
  if len(prev) > 12:
    prev = prev[-12:]
  print prev

@hook.command(autohelp=False)
@hook.command('bit', autohelp=False)
def bitcoin(inp, say=None):
    ".bitcoin -- gets current exchange rate for bitcoins from bitstamp"
    # https://github.com/1stvamp/py-sparkblocks
    mx = max(prev)
    mn = min(prev)
    rn = mx-mn
    out = []
    for num in prev:
      # n = num['avg']
      n = float(num)
      if (n - mn) != 0 and rn != 0:
        s = (n - mn) / rn
      else:
        s = 0
      s = math.floor(min([6, (s * 7)]))
      out.append(unichr(int(9601 + s)))
    t = get_bitcoin()
    t['graph'] = ''.join(out)
    say(u"Current: \x0307${avg:2.2f}\x0f - High: \x0307${high:2.2f}\x0f"
        " - Low: \x0307${low:2.2f}\x0f - Graph: {graph}".format(**t))

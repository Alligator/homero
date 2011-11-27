from util import hook, http
import re

reg = re.compile(r"(\d+\.?\d*?)\s*?([A-Za-z]{3})\s*?([A-Za-z]{3})", re.I)

@hook.command
def convert(inp, say=None):
    m = reg.findall(inp)
    v1, c1, c2 = m[0]
    j = http.get_json('https://raw.github.com/currencybot/open-exchange-rates/master/latest.json')
    r1 = j['rates'][c1.upper()]
    r2 = j['rates'][c2.upper()]
    rate = r2/r1
    return float(rate) * float(v1)

from util import hook, http
import re

reg = re.compile(r"(\d+\.?\d*?)\s*?([A-Za-z]{3})\s*?([A-Za-z]{3})", re.I)
greg = re.compile(r"(?:l|r)hs: \"([^\"]*)")

@hook.command
def convert(inp, say=None):
    m = reg.findall(inp)
    v1, c1, c2 = m[0]
    j = http.get('http://www.google.com/ig/calculator?hl=en&q={0}{1}=?{2}'.format(v1, c1, c2))
    g = greg.findall(j.decode('utf-8', errors='ignore'))
    if j:
      return '{0} = {1}'.format(*g)

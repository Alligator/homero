from util import hook
from urllib import quote

urls = {
    'item': 'http://larzm42.github.io/dom4inspector/?page=item&itemq={}&showmoddinginfo=1&showids=1',
    'spell': 'http://larzm42.github.io/dom4inspector/?page=spell&spellq={}&showmoddinginfo=1&showids=1',
    'unit': 'http://larzm42.github.io/dom4inspector/?page=unit&unitq={}&showmoddinginfo=1&showids=1',
    'site': 'http://larzm42.github.io/dom4inspector/?page=site&siteq={}&showmoddinginfo=1&showids=1',
    'weapon': 'http://larzm42.github.io/dom4inspector/?page=wpn&wpnq={}&showmoddinginfo=1&showids=1',
    'armor': 'http://larzm42.github.io/dom4inspector/?page=armor&armorq={}&showmoddinginfo=1&showids=1'
}

@hook.command
def dom4(inp):
  ".dom4 [item|spell|unit|site|weapon|armor] query"
  kind, term = inp.split(' ', 1)
  return urls[kind].format(quote(term))

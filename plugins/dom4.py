from util import hook
from urllib import quote

urls = {
    'item':  'http://larzm42.github.io/dom4inspector/?page=item&itemq={}&showmoddinginfo=1&showids=1&loadEvents=1',
    'hat':   'http://larzm42.github.io/dom4inspector/?page=item&itemq={}&showmoddinginfo=1&showids=1&loadEvents=1',
    'spell': 'http://larzm42.github.io/dom4inspector/?page=spell&spellq={}&showmoddinginfo=1&showids=1&loadEvents=1',
    'unit':  'http://larzm42.github.io/dom4inspector/?page=unit&unitq={}&showmoddinginfo=1&showids=1&loadEvents=1',
    'site':  'http://larzm42.github.io/dom4inspector/?page=site&siteq={}&showmoddinginfo=1&showids=1&loadEvents=1',
    'weapon':'http://larzm42.github.io/dom4inspector/?page=wpn&wpnq={}&showmoddinginfo=1&showids=1&loadEvents=1',
    'armor': 'http://larzm42.github.io/dom4inspector/?page=armor&armorq={}&showmoddinginfo=1&showids=1&loadEvents=1',
    'merc':  'http://larzm42.github.io/dom4inspector/?page=merc&mercq={}&showmoddinginfo=1&showids=1&loadEvents=1',
    'event':  'http://larzm42.github.io/dom4inspector/?page=event&eventq={}&showmoddinginfo=1&showids=1&loadEvents=1'
}

@hook.command
def dom4(inp):
  try:
    kind, term = inp.split(' ', 1)
  except ValueError,e :
    return dom4.__doc__

  if kind not in urls:
    return dom4.__doc__
  return urls[kind].format(quote(term))

dom4.__doc__ = '.dom4 [' + '|'.join(k for k in sorted(urls.keys())) + '] query'

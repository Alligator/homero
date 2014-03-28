from util import hook
import requests
import lxml.html

def get(inp):
  inp = inp.encode('utf-8').strip()
  params = {'teng': inp}
  resp = requests.post('http://japanesetransliteration.com/', data=params)
  h = lxml.html.fromstring(resp.text)
  x = h.xpath('//span[@class="txt_title"]')
  rmj = x[1].text.replace('\r', '')
  ktk = x[4].text.replace('\r', '')
  hir = x[5].text.replace('\r', '')
  return [rmj, ktk.encode('ISO-8859-1').decode('utf-8'), hir.encode('ISO-8859-1').decode('utf-8')]

@hook.command
def jap(inp):
  ".jap text -- transliterate text to katakana and back to english"
  n = get(inp)
  return n[0]

@hook.command
def katakana(inp):
  ".jap text -- transliterate text to katakana"
  n = get(inp)
  return n[1] + ' '+ n[0]

@hook.command
def hiragana(inp):
  ".jap text -- transliterate text to hiragana"
  n = get(inp)
  return n[2] + ' '+ n[0]

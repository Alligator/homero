from util import hook

key = {
  "a":"а",
  "b":"б",
  "v":"в",
  "g":"г",
  "d":"д",
  "ye":"е",
  "yo":"ё",
  "j":"ж",
  "z":"з",
  "i":"и",
  "y":"й",
  "k":"к",
  "l":"л",
  "m":"м",
  "n":"н",
  "o":"о",
  "p":"п",
  "r":"р",
  "s":"с",
  "t":"т",
  "u":"у",
  "f":"ф",
  "h":"х",
  "c":"к",
  "ts":"ц",
  "ch":"ч",
  "sh":"ш",
  "sch":"щ",
  "y":"ы",
  "e":"э",
  "yu":"ю",
  "ya":"я",
}

@hook.command
def russify(inp):
  inp = inp.lower()
  if isinstance(inp, unicode):
    txt = list(inp)
  else:
    txt = list(unicode(inp, 'utf-8', 'replace'))
  txt.reverse()
  out = ''
  while txt:
    if len(txt) >= 3:
      w = txt.pop() + txt.pop() + txt.pop()
      if w in key:
        out += key[w]
        continue
      else:
        [txt.append(l) for l in w[::-1]]
    if len(txt) >= 2:
      w = txt.pop() + txt.pop()
      if w in key:
        out += key[w]
        continue
      else:
        [txt.append(l) for l in w[::-1]]
    if len(txt) >= 1:
      w = txt.pop()
      if w in key:
        out += key[w]
        continue
      else:
        out += w.encode('utf-8')
  return out.decode('utf-8')

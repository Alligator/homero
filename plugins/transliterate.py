# -*- coding: utf-8 -*-
from util import hook
import re

@hook.command
def greekify(inp):
  table = {
    'multi': [
      (u'cks', u'ξ'),
      (u'Cks', u'Ξ'),
      (u'CKS', u'Ξ'),
      (u'ps' , u'ψ'),
      (u'ph' , u'φ'),
      (u'th' , u'θ'),
      (u'ch' , u'χ'),
      (u'kh' , u'χ'),
      (u'ks' , u'ξ'),
      (u'ck' , u'κ'),
      (u'Ps' , u'Ψ'),
      (u'Ph' , u'Φ'),
      (u'Th' , u'Θ'),
      (u'Ch' , u'Χ'),
      (u'Kh' , u'Χ'),
      (u'Ks' , u'Ξ'),
      (u'Ck' , u'Κ'),
      (u'PS' , u'Ψ'),
      (u'PH' , u'Φ'),
      (u'TH' , u'Θ'),
      (u'CH' , u'Χ'),
      (u'KH' , u'Χ'),
      (u'KS' , u'Ξ'),
      (u'CK' , u'Κ'),
      (u'aw' , u'ω'),
      (u'Aw' , u'Ω'),
      (u'AW' , u'Ω'),
      (u'ce' , u'σε'),
      (u'CE' , u'ΣΕ'),
      (u'Ce' , u'Σε'),
      (u'ci' , u'σι'),
      (u'CI' , u'ΣΙ'),
      (u'Ci' , u'Σι'),
      (u'cy' , u'συ'),
      (u'CY' , u'ΣΥ'),
      (u'Cy' , u'Συ'),
      (u's([^\w])', u'ς\g<1>'),
    ],
    'single': [
      u'abcdefghijklmnopqrstuvwxyz'+
      u'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
      u'αβκδεφγηιικλμνοπκρστυβυξυζ'+
      u'ΑΒΚΔΕΦΓΗΙΙΚΛΜΝΟΠΚΡΣΤΥΒΥΞΥΖ'
    ]
  }
  return transliterate(table, inp)

@hook.command
def russify(inp):
  table = {
    'multi': [
      (u'the', u'зе'),
      (u'ye',u'е'),
      (u'yo',u'ё'),
      (u'yu',u'ю'),
      (u'ya',u'я'),
      (u'ts',u'ц'),
      (u'ch',u'ч'),
      (u'sh',u'ш'),
      (u'sch',u'щ'),
      (u'th',u'ф'),
      (u'q',u'кв'),
      (u'x',u'кс'),
      (u'q',u'кв'),
      (u'x',u'кс'),
      (u'ph',u'ф'),
      (u'oo',u'у'),
      (u'ce([^\w])', u'с\g<1>'),
      (u'ck([^\w])', u'к\g<1>'),
      (u'ff([^\w])', u'ф\g<1>'),
      (u'ly([^\w])', u'ли\g<1>'),
      (u'iy([^\w])', u'ий\g<1>'),
      (u'ij([^\w])', u'ий\g<1>'),
      (u'([^\w])sc', u'\g<1>с'),
    ],
    'single': [
      u'abcdefghijklmnopqrstuvwxyz',
      u'абкдэфгхижклмноп рстувв из',
    ]
  }
  return transliterate(table, inp.lower())

@hook.command
def georgify(inp):
  table = {
    'multi': [
      (u"ts'", u'წ'),
      (u"ch'", u'ჭ'),
      (u"k'", u'ქ'),
      (u"t'", u'თ'),
      (u"p'", u'ფ'),
      (u"sh", u'შ'),
      (u"ch", u'ჩ'),
      (u"zh", u'ჟ'),
      (u"ts", u'ც'),
      (u"dz", u'ძ'),
      (u"kh", u'ხ'),
      (u"ce", u'სე'),
      (u"ci", u'სი'),
      (u"cy", u'სი'),
      (u"ck", u'კ'),
      (u"x",  u"კს")
    ],
    'single': [
      u'abcdefghijklmnopqrstuvwxyz',
      u'აბკდეჶგჰიჯკლმნოპყრსტუვუ იზ'
    ]
  }
  return transliterate(table, inp.lower())

@hook.command
def bopomofo(inp):
  table = {
    'multi': [
      (u'ang', u'ㄤ'),
      (u'eng', u'ㄥ'),
      (u'ch',  u'ㄔ'),
      (u'zh',  u'ㄓ'),
      (u'sh',  u'ㄕ'),
      (u'ai',  u'ㄞ'),
      (u'ei',  u'ㄟ'),
      (u'ao',  u'ㄠ'),
      (u'ou',  u'ㄡ'),
      (u'an',  u'ㄢ'),
      (u'en',  u'ㄣ'),
      (u'er',  u'ㄦ'),
      (u'yu',  u'ㄩ')
    ],
    'single': [
      u'abcdeêfghijklmnopqrstuüvwxyz',
      u'ㄚㄅㄘㄉㄜㄝㄈㄍㄏㄧㄐㄎㄌㄇㄋㄛㄆㄑㄖㄙㄊㄨㄩㄩㄨㄒㄧㄗ'
    ]
  }
  return transliterate(table, inp.lower())

@hook.command
def wadegiles(inp):
  table = {
    'multi': {
      u'z':  u'ts',
      u'c':  u"ts'",
      u'j':  u'ch',
      u'k':  u"k'",
      u'x':  u'hs',
      u't':  u"t'",
      u'p':  u"p'",
      u'q':  u"ch'",
      u'ie': u'ieh',
      u'ch':  u"ch'",
      u'qu':  u"ch'ü",
      u'ju':  u'chü',
      u'xu':  u'hsü',
      u'yu':  u'yü',
      u'uo':  u'o',
      u'üe':  u'üeh',
      u'er':  u'erh',
      u'ge':  u'ko',
      u'he':  u'ho',
      u'ke':  u"k'o",
      u'zh':  u'ch',
      u'ri':  u'jih',
      u'zi':  u'tsû',
      u'ci':  u"ts'û",
      u'si':  u'ssû',
      u'yi':  u'i',
      u'ian': u'ien',
      u'ing': u'ing',
      u'ong': u'ung',
      u'ang': u'ang',
      u'eng': u'êng',
      u'zhi':  u'chih',
      u'chi':  u"ch'ih",
      u'shi':  u'shih',
      u'yin':  u'yin',
      u'you':  u'yu',
      u'ying':  u'ying',
    },
    'single': [
      u'abdeêfghilmnorsuüvwy',
      u'apteêfkhilmnojsuüüwy'
    ]
  }
  return transliterate(table, inp.lower())

def transliterate(key, inp):
  inp = unicode(inp + '\n')
  # multi-letter replacements
  for (phrase, letter) in key['multi']:
    inp = re.sub(phrase, letter, inp)

  # single letter replacements
  table = { ord(a): ord(b) for a, b in zip(*key['single']) }
  inp = inp.translate(table)
  return inp.strip()

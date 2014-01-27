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
      (u'(?:s|c)([^\w])', u'ς\g<1>'),
      (u'ct' , u'кt'),
    ],
    'single': [
      u'abcdefghijklmnopqrstuvwxyz'+
      u'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
      u'αβσδεφγηιικλμνοπκρστυβυξυζ'+
      u'ΑΒΣΔΕΦΓΗΙΙΚΛΜΝΟΠΚΡΣΤΥΒΥΞΥΖ'
    ]
  }
  return transliterate(table, inp)

@hook.command
def russify(inp):
  table = {
    'multi': [
      (u'ye',u'е'), (u'ye',u'е'),
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
    ],
    'single': [
      u'abcdefghijklmnopqrstuvwxyz',
      u'абкдэфгхижклмноп рстувб ыз',
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

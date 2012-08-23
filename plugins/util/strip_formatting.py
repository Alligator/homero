import re

regex = re.compile("(\x03|\x02|\x1f)(?:,?\d{1,2}(?:,\d{1,2})?)?", re.UNICODE)

def strip(text):
  print repr(text)
  return regex.sub('', text)

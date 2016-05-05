from util import hook
import shlex
import subprocess
from itertools import izip_longest
import sys

@hook.command
def piss(inp, say=None):
  dil = [
    "  |%\%-,_          \x0308",             
    "/%\\\\.    '-,_      \x0308",             
    "%|\%/        '-,_  \x0308",             
    "/%\\  --,__    ( \\`\x0308/",             
    "%(%  ;  %)%'-,_\__/\x0308",             
    "  /%   ,%/%        \x0308",             
    "    '%--'          "              
  ]
  # inp = inp.replace('"', '\\"').replace("'", "\\'")
  try:
    text = subprocess.check_output(shlex.split('/usr/bin/figlet -f smscript -w 160 "' + inp.encode('utf-8') + '"')).split('\n')
    # text.insert(0, None)
    for dil, line in izip_longest(dil, text):
      print line
      say(dil + (line if line else ''))
  except OSError, e:
    if e.errno == 12:
      # outta memory, bail
      sys.exit(0)

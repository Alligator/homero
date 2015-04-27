from util import hook
import shlex
import subprocess
from itertools import izip_longest

@hook.command
def piss(inp, say=None):
  print repr(inp)
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
  text = subprocess.check_output(shlex.split('/usr/bin/figlet -f smscript -w 160 "' + inp.encode('utf-8') + '"')).split('\n')
  # text.insert(0, None)
  for dil, line in izip_longest(dil, text):
    print line
    say(dil + (line if line else ''))

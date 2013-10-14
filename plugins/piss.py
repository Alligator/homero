from util import hook
import shlex
import subprocess
from itertools import izip_longest

@hook.command
def piss(inp, say=None):
  dil = [
    "  |%\%-,_          \x0308",             
    "/%\\\\.    '-,_      \x0308",             
    "%|\%/        '-,_  \x0308",             
    "/%\  --,__    ( \`\x0308/",             
    "%(%  ;  %)%'-,_\__/\x0308",             
    "  /%   ,%/%        \x0308",             
    "    '%--'          "              
  ]
  text = subprocess.check_output(shlex.split('figlet -f smscript "' + inp + '"')).strip().split('\n')
  text.insert(0, None)
  for dil, line in izip_longest(dil, text):
    say(dil + (line if line else ''))

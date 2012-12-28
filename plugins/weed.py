from util import hook
from time import time

last = 0

@hook.command(autohelp=False)
def weed(inp, say=None):
  global last
  if (time() - last) > 60 or last == 0:
    last = time()
    say(r'                  |')
    say(r'                 |.|')
    say(r'                 |.|')
    say(r'                |\./|')
    say(r'                |\./|')
    say(r'.               |\./|               .')
    say(r' \^.\          |\\.//|          /.^/')
    say(r'  \--.|\       |\\.//|       /|.--/')
    say(r'    \--.| \    |\\.//|    / |.--/')
    say(r'     \---.|\    |\./|    /|.---/')
    say(r'        \--.|\  |\./|  /|.--/')
    say(r'           \ .\  |.|  /. /')
    say(r' _ -_^_^_^_-  \ \\ // /  -_^_^_^_- _')
    say(r'   - -/_/_/- ^ ^  |  ^ ^ -\_\_\- -')

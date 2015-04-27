from util import hook
import re
import subprocess

reg = re.compile(r'(.*) in (.*)')

@hook.command
def units(inp):
  ".units <thing> in <thing> - converts unit, in is not optional"
  m = reg.findall(inp)[0]
  out = subprocess.check_output(['/usr/bin/units', '-t',  m[0], m[1]]).strip()
  return '{} = {} {}'.format(m[0], out, m[1])

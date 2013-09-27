from util import hook
import os
import time
import re
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
import urllib2

ignore = [
    'save', 'restore', 'quit', '\\'
]
op = open('/home/alligator/if/out', 'r')
pos = op.tell()

status_re = re.compile(r'(.*)\s+Score: (\d+)\s*Moves: (\d+)')

@hook.command
def iflog(inp):
  global pos
  op.seek(0)
  out = op.read()
  op.seek(pos)

  register_openers()
  datagen, headers = multipart_encode({'sprunge': out})
  request = urllib2.Request('http://sprunge.us', datagen, headers)
  return urllib2.urlopen(request).read()

@hook.command(adminonly=True)
def ifsave(inp, conn=None):
  ip = os.open('/home/alligator/if/inp', os.O_WRONLY)
  os.write(ip, 'save\nhomero\n')
  ifsend('', conn=conn)

@hook.command(adminonly=True)
def ifrestore(inp, conn=None):
  ip = os.open('/home/alligator/if/inp', os.O_WRONLY)
  os.write(ip, 'restore\nhomero\n')
  ifsend('', conn=conn)

@hook.command()
@hook.command('ifs')
def ifsend(inp, conn=None):
  global pos, op

  # check if we're at the start of the file but theres more to read
  if op.tell() == 0:
    op.seek(0, 2)
    if op.tell() > 0:
      pos = op.tell()
    else:
      pos = 0

  if inp and not any(n in inp for n in ignore):
    ip = os.open('/home/alligator/if/inp', os.O_WRONLY)
    os.write(ip, inp + '\n')
  time.sleep(0.5)
  op.seek(pos)
  lines = op.read().split('\n')
  pos = op.tell()
  for line in lines:
    if line:
      match = status_re.match(line)
      if match:
        conn.cmd('PRIVMSG #zrk \x0309%s' % line)
      else:
        conn.cmd('PRIVMSG #zrk %s' % line)

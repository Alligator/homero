from util import hook
import shlex
import subprocess32 as subprocess
import requests
import json

@hook.command()
def sam(inp):
  try:
    wav = subprocess.check_output(shlex.split(
      '/home/alligator/dev/SAM/sam -wav a "' + inp.encode('utf-8') + '"'
    ), timeout=10)
    print 'sam: got wav'
    resp = requests.post('https://upload.clyp.it/upload', files={'audioFile': ('homero.wav', wav, 'audio/wav')})
    j = json.loads(resp.text)
    if j['Successful']:
      return j['Url']
    else:
      return 'error:' + j['Message']
  except subprocess.CalledProcessError, e:
    print e.cmd

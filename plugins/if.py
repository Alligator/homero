#import os
#import pexpect
#import re
#from util import hook
#
#child = None
#go = False
#m = re.compile('.*\>', re.MULTILINE)
#ignore = [
#        'quit',
#        'script',
#        '.',
#        'save',
#        'restore'
#        ]
#
#ignore_out = [
#        '',
#        'I don\'t know',
#        'There was no verb in that sentence!'
#        ]
#
#def if_next(say):
#    c = child.expect(m)
#    for line in (child.before.split('\r\n'))[1:]:
#        if line not in ignore_out:
#            say(line)
#
#def if_send(inp, say):
#    if child:
#        child.sendline(inp)
#        return if_next(say)
#
#@hook.event('PRIVMSG')
#def seen(paraml, say=None, input=None):
#    if input.msg in ignore:
#       return
#    return if_send(input.msg, say)
#
#@hook.command('zork', autohelp=False)
#def i_f(inp, say=None):
#    global go, child
#    if not go:
#        go = True
#        child = pexpect.spawn('dfrotz -w 120 /home/alligator/if/zork1.z5')
#        if_next(say)
#        return
#
#@hook.command
#def if_kill(inp, nick=None):
#    global go, child
#    if nick == 'alligator' or 'sponge' in nick:
#        child.close(force=True)
#        go = False
#        return 'if killed'

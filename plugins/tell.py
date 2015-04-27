" tell.py: written by sklnd in July 2009"
"       2010.01.25 - modified by Scaevolus"

import time

from util import hook, timesince


def db_init(db):
    "check to see that our db has the tell table and return a dbection."
    db.execute("create table if not exists tell"
                "(user_to, user_from, message, chan, time,"
                "primary key(user_to, message))")
    db.commit()

    return db


def get_tells(db, user_to):
    return db.execute("select user_from, message, time, chan from tell where"
                         " user_to=lower(?) order by time",
                         (user_to.lower(),)).fetchall()


@hook.singlethread
@hook.event('PRIVMSG')
def tellinput(paraml, input=None, db=None, bot=None):
    if 'showtells' in input.msg.lower():
        return

    db_init(db)

    tells = get_tells(db, input.nick)

    if tells:
        user_from, message, time, chan = tells[0]
        reltime = timesince.timesince(time)

        reply = "%s said %s ago in %s: %s" % (user_from, reltime, chan,
                                              message)
        if len(tells) > 1:
            reply += " (+%d more, .showtells to view)" % (len(tells) - 1)

        db.execute("delete from tell where user_to=lower(?) and message=?",
                     (input.nick, message))
        db.commit()
        input.notice(reply)


@hook.command(autohelp=False)
def showtells(inp, nick='', chan='', notice=None, db=None):
    ".showtells -- view all pending tell messages (sent in PM)."

    db_init(db)

    tells = get_tells(db, nick)

    if not tells:
        notice("You have no pending tells.")
        return

    for tell in tells:
        user_from, message, time, chan = tell
        past = timesince.timesince(time)
        notice("%s said %s ago in %s: %s" % (user_from, past, chan, message))

    db.execute("delete from tell where user_to=lower(?)",
                  (nick,))
    db.commit()


@hook.command
def tell(inp, nick='', chan='', db=None):
    ".tell <nick> <message> -- relay <message> to <nick> when <nick> is around"

    query = inp.split(' ', 1)

    if len(query) != 2:
        return tell.__doc__

    user_to = query[0].lower()
    message = query[1].strip()
    user_from = nick

    if chan.lower() == user_from.lower():
        chan = 'a pm'

    if user_to == user_from.lower():
        return "No."

    db_init(db)

    if db.execute("select count() from tell where user_to=?",
                    (user_to,)).fetchone()[0] >= 10:
        return "That person has too many things queued."

    try:
        db.execute("insert into tell(user_to, user_from, message, chan,"
                     "time) values(?,?,?,?,?)", (user_to, user_from, message,
                     chan, time.time()))
        db.commit()
    except db.IntegrityError:
        return "Message has already been queued."

    return "I'll pass that along."

@hook.command
def tellgroup(inp, nick=None, chan=None, db=None, reply=None):
  inp = inp.split(' ', 1)
  if len(inp) != 2:
    return 'no mate'
  inp, msg = inp

  try:
    users = db.execute('select users from tellgroup where name=?',
      (inp,)).fetchone()
  except db.OperationalError:
    return 'no groups are defined'

  if not users:
    return 'group not found'

  users = users[0].split(' ')
  sent = []
  for user in users:
    if user == nick: continue
    ret = tell(user + ' ' + msg, nick=nick, chan=chan, db=db)
    if ret != "I'll pass that along.":
      reply('error telling ' + user + ': ' + ret)
    else:
      sent.append(user)

@hook.command
def joingroup(inp, nick=None, chan=None, db=None):
  db.execute("create table if not exists tellgroup"
              "(name, chan, users, primary key(name, chan))")
  db.commit()

  inp = inp.split(' ')[0]

  users = db.execute('select users from tellgroup where name=? and chan=?',
              (inp, chan)).fetchone()

  users = set(users[0].split(' ')) if users else set()
  if nick in users:
    return 'you are already in that group'
  users.add(nick)

  db.execute('insert or replace into tellgroup(name, chan, users) values(?,?,?)',
              (inp, chan, ' '.join(users)))
  db.commit()

  return 'joined ' + inp

@hook.command
def leavegroup(inp, nick=None, chan=None, db=None):
  try:
    inp = inp.split(' ')[0]
    users = db.execute('select users from tellgroup where name=? and chan=?',
      (inp, chan)).fetchone()
  except db.operationalerror:
    return 'no groups are defined'

  if users:
    users = set(users[0].split(' '))

    if nick not in users:
      return 'you are not in that group'

    users.remove(nick)

    if len(users) == 0:
      db.execute('delete from tellgroup where name=? and chan=?', (inp, chan))
      db.commit()
      return 'removed from ' + inp + ' and deleted the group as it is empty'
    else:
      db.execute('insert or replace into tellgroup(name, chan, users) values(?,?,?)',
          (inp, chan, ' '.join(users)))
      db.commit()
      return 'removed from ' + inp
  else:
    return 'group not found'

@hook.command
def groups(inp, nick=None, chan=None, db=None):
  try:
    groups = db.execute('select name from tellgroup where users like ?',
        ('%' + nick + '%',)).fetchall()
  except db.OperationalError, e:
    return 'no groups are defined'

  if groups:
    groups = zip(*groups)[0]
    return 'for the channel {} you are in: {}'.format(chan, ', '.join(groups))
  else:
    return 'you are in no groups for {}'.format(chan)

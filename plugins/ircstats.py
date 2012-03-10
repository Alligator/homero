from util import hook
import datetime
import jinja2
import cPickle as pickle
import os

posters = {}
total = 0

@hook.singlethread
@hook.event('PRIVMSG')
def ircstats(paraml, input=None, bot=None):
    if not input['chan'] == '#sa-minecraft':
        return

    global posters
    global total

    # we gotsa ta unpickle
    if not posters:
        try:
            f = open(os.path.join(bot.persist_dir, 'ircstats.pkl'), 'rb')
            posters = pickle.load(f)
            total = pickle.load(f)
            f.close()
        except Exception, e:
            # im so sorry
            pass

    now = datetime.datetime.today()
    past = datetime.datetime.today() - datetime.timedelta(hours=24)

    # put the data in the dict
    nick = input['nick']
    posters.setdefault(nick, {"total_posts": 0, "hours_active": []})
    posters[nick]['total_posts'] += 1
    posters[nick]['hours_active'].append(now)

    total += 1

    # trim the old values
    for i, time in enumerate(posters[nick]['hours_active']):
        if time < past:
            del posters[nick]['hours_active'][i]
            posters[nick]['total_posts'] -= 1
            total -= 1

    # convert the data to the format we want for the template
    posters_out = {}

    for p in posters.keys():
        posters_out.setdefault(p, {"total_posts": 0, "hours_active": []})
        posters_out[p]['total_posts'] = posters[p]['total_posts']
        for i in range(24):
            posters_out[p]['hours_active'].append([x.hour for x in posters[p]['hours_active']].count(i))

    sort = {'posters': sorted(posters_out.iteritems(), key=lambda x: x[1]['total_posts'], reverse=True)[:10], 'total': total}

    # make a template
    env = jinja2.Environment(loader=jinja2.FileSystemLoader('/var/www/ircstats/templates'))
    temp = env.get_template('index.html')
    f = open('/var/www/ircstats/index.html', 'w')
    f.write(temp.render(**sort))

    # pickle the dict
    f = open(os.path.join(bot.persist_dir, 'ircstats.pkl'), 'wb')
    pickle.dump(posters, f)
    pickle.dump(total, f)
    f.close()

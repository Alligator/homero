from util import hook
import os
from random import shuffle
import random
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime

mcache = {}
savepath = '/var/www/homero'

@hook.event('PRIVMSG')
def comic_msg(paraml, input=None, bot=None):
  key = (input.chan, input.conn)

  if key not in mcache:
    mcache[key] = []

  value = (datetime.now(), input.nick, input.msg)

  if not input.msg.startswith('.') and not input.msg.startswith('!'):
    mcache[key].append(value)
    if 'buffer_size' not in bot.config:
      bot.config['buffer_size'] = 30

    mcache[key] = mcache[key][-1*bot.config['buffer_size']:]

@hook.command("comic")
def comic(paraml, input=None, db=None, bot=None, conn=None):
    #print os.getcwd()
    title = paraml
    paraml = input.chan
    msgs = mcache[(paraml,conn)]
    sp = 0
    chars = set()

    for i in xrange(len(msgs)-1, 0, -1):
        sp += 1
        diff = msgs[i][0] - msgs[i-1][0]
        chars.add(msgs[i][1])
        if sp > 10 or diff.total_seconds() > 120 or len(chars) > 5:
            break

    msgs = msgs[-1*sp:]

    panels = []
    panel = []

    for (d, char, msg) in msgs:
        if len(panel) == 2 or len(panel) == 1 and panel[0][0] == char:
            panels.append(panel)
            panel = []
        panel.append((char, msg))
    panels.append(panel)

    # fname = ''.join([random.choice("fartpoo42069") for i in range(16)]) + ".jpg"
    fname = datetime.now().isoformat().split('.')[0] + '-' + input.chan.replace('#', '') + '.jpg'

    if len(title) > 0:
      make_comic(chars, panels, title).save(os.path.join(savepath, fname), quality=86)
    else:
      make_comic(chars, panels).save(os.path.join(savepath, fname), quality=86)
    return "http://irc.alligatr.co.uk/homero/" + fname

def wrap(st, font, draw, width):
    #print "\n\n\n"
    st = st.split()
    mw = 0
    mh = 0
    ret = []

    while len(st) > 0:
        s = 1
        #print st
        #import pdb; pdb.set_trace()
        while True and s < len(st):
            w, h = draw.textsize(" ".join(st[:s]), font=font)
            if w > width:
                s -= 1
                break
            else:
                s += 1

        if s == 0 and len(st) > 0: # we've hit a case where the current line is wider than the screen
            s = 1

        w, h = draw.textsize(" ".join(st[:s]), font=font)
        mw = max(mw, w)
        mh += h
        ret.append(" ".join(st[:s]))
        #print st[:s]
        #print
        st = st[s:]

    return (ret, (mw, mh))

def rendertext(st, font, draw, pos):
    ch = pos[1]
    for s in st:
        s = unicode(s)
        w, h = draw.textsize(s, font=font)
        for i in range(1,2):
          draw.text((pos[0]-i, ch-i), s, font=font, fill=(0x0,0x0,0x0,0x0))
          draw.text((pos[0]-i, ch+i), s, font=font, fill=(0x0,0x0,0x0,0x0))
          draw.text((pos[0]+i, ch-i), s, font=font, fill=(0x0,0x0,0x0,0x0))
          draw.text((pos[0]+i, ch+i), s, font=font, fill=(0x0,0x0,0x0,0x0))
        draw.text((pos[0], ch), s, font=font, fill=(0xff,0xff,0xff,0xff))
        ch += h

def rendertitle(st, font, draw, pos):
    w, h = draw.textsize(st[0], font=font)
    ch = (300 - (h * len(st)))/2
    for s in st:
        s = unicode(s)
        w, h = draw.textsize(s, font=font)
        x = (450 - w)/2
        for i in range(1,2):
          draw.text((x-i, ch-i), s, font=font, fill=(0x0,0x0,0x0,0x0))
          draw.text((x-i, ch+i), s, font=font, fill=(0x0,0x0,0x0,0x0))
          draw.text((x+i, ch-i), s, font=font, fill=(0x0,0x0,0x0,0x0))
          draw.text((x+i, ch+i), s, font=font, fill=(0x0,0x0,0x0,0x0))
        draw.text((x, ch), s, font=font, fill=(0xff,0xff,0xff,0xff))
        ch += h

def fitimg(img, (width, height)):
    scale1 = float(width) / img.size[0]
    scale2 = float(height) / img.size[1]

    l1 = (img.size[0] * scale1, img.size[1] * scale1)
    l2 = (img.size[0] * scale2, img.size[1] * scale2)

    if l1[0] > width or l1[1] > height:
        l = l2
    else:
        l = l1

    return img.resize((int(l[0]), int(l[1])), Image.ANTIALIAS)

def make_comic(chars, panels, title=False):
    #filenames = os.listdir(os.path.join(os.getcwd(), 'chars'))

    panelheight = 300
    panelwidth = 450

    filenames = os.listdir('comic/chars/')
    shuffle(filenames)
    filenames = map(lambda x: os.path.join('comic/chars', x), filenames[:len(chars)])
    chars = list(chars)
    chars = zip(chars, filenames)
    charmap = dict()
    for ch, f in chars:
        if os.path.isdir(f):
          charmap[ch] = []
          for fi in os.listdir(f):
            charmap[ch].append(Image.open(os.path.join(f, fi)))
        else:
          charmap[ch] = [Image.open(f)]

    imgwidth = panelwidth
    imgheight = panelheight * len(panels)
    if title:
      imgheight += panelheight

    bg = Image.open(os.path.join('comic/backgrounds', random.choice(os.listdir('comic/backgrounds'))))

    im = Image.new("RGBA", (imgwidth, imgheight), (0xff, 0xff, 0xff, 0xff))
    font = ImageFont.truetype("comic/COMICBD.TTF", 14)
    titlefont = ImageFont.truetype("comic/COMICBD.TTF", 20)

    if title:
        pim = Image.new("RGBA", (panelwidth, panelheight), (0xff, 0xff, 0xff, 0xff))
        pim.paste(bg, (0, 0))
        draw = ImageDraw.Draw(pim)
        st1w = 0; st1h = 0; st2w = 0; st2h = 0
        (st1, (st1w, st1h)) = wrap(title, titlefont, draw, 2*panelwidth/3.0)
        rendertitle(st1, titlefont, draw, (10, 10))

        draw.line([(0, 0), (0, panelheight-1), (panelwidth-1, panelheight-1), (panelwidth-1, 0), (0, 0)], (0, 0, 0, 0xff))
        del draw
        im.paste(pim, (0, 0))

    for i in xrange(len(panels)):
        pim = Image.new("RGBA", (panelwidth, panelheight), (0xff, 0xff, 0xff, 0xff))
        pim.paste(bg, (0, 0))
        draw = ImageDraw.Draw(pim)

        st1w = 0; st1h = 0; st2w = 0; st2h = 0
        (st1, (st1w, st1h)) = wrap(panels[i][0][1], font, draw, 2*panelwidth/3.0)
        rendertext(st1, font, draw, (10, 10))
        if len(panels[i]) == 2:
            (st2, (st2w, st2h)) = wrap(panels[i][1][1], font, draw, 2*panelwidth/3.0)
            rendertext(st2, font, draw, (panelwidth-10-st2w, st1h + 10))

        texth = st1h + 10
        if st2h > 0:
            texth += st2h + 10 + 5

        maxch = panelheight - texth
        im1 = fitimg(random.choice(charmap[panels[i][0][0]]), (2*panelwidth/5.0-10, maxch))
        try:
          pim.paste(im1, (10, panelheight-im1.size[1]), im1)
        except Exception, e:
          print e, st2

        if len(panels[i]) == 2:
            im2 = fitimg(random.choice(charmap[panels[i][1][0]]), (2*panelwidth/5.0-10, maxch))
            im2 = im2.transpose(Image.FLIP_LEFT_RIGHT)
            pim.paste(im2, (panelwidth-im2.size[0]-10, panelheight-im2.size[1]), im2)

        draw.line([(0, 0), (0, panelheight-1), (panelwidth-1, panelheight-1), (panelwidth-1, 0), (0, 0)], (0, 0, 0, 0xff))
        del draw
        if title:
          im.paste(pim, (0, panelheight * (i+1)))
        else:
          im.paste(pim, (0, panelheight * i))

    return im

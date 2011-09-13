from util import hook, http
import re

tfw_url = 'http://thefuckingweather.com/?zipcode=%s'
r_loc = '<span class\="small">([^<]+)</span></div>'
r_tmp = '<div class\="large" >(\d{1,3})'
r_dsc = '<br />(.+)</div>'

@hook.command
def tfw(inp):
    '.tfw [zip|postcode] -- THE FUCKING WEATHER'
    src = http.get(tfw_url % inp)
    location = re.search(r_loc, src).group(1)
    temp = re.search(r_tmp, src).group(1)
    desc = re.search(r_dsc, src).group(1).replace("<br />", ". ")
    c = int((int(temp) - 32) * (5.0/9.0))
    return "%s. %sF/%sC. %s" % (location, temp, c, desc)


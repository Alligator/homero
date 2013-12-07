from util import hook, http

@hook.command(autohelp=False)
def aus(inp):
    html = http.get_html("http://www.boganipsum.com/")
    n = html.xpath('//div[@class="bogan-ipsum"]/p')[0].text
    return n

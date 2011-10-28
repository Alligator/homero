from util import hook, http

@hook.command(autohelp=False)
def aus(inp):
    html = http.get_html("http://www.boganipsum.com/")
    txt = html.cssselect('div.bogan-ipsum p')[0].text_content()[0:300]
    return txt[0:txt.rfind('.')+1]



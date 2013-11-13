from util import hook, http
import re

reg = re.compile(r"(\d+\.?\d*?)\s*?([A-Za-z]{3})\s*?([A-Za-z]{3})", re.I)
greg = re.compile(r"(?:l|r)hs: \"([^\"]*)")

@hook.command
def convert(inp, say=None):
    m = reg.findall(inp)
    v1, c1, c2 = m[0]
    h = http.get_html('https://www.google.co.uk/finance/converter?a={0}&from={1}&to={2}'.format(v1, c1, c2))
    return h.xpath(r'//*[@id="currency_converter_result"]')[0].text_content()

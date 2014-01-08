from util import http, hook

@hook.command(autohelp=False)
@hook.command('bit', autohelp=False)
def bitcoin(inp, say=None):
    ".bitcoin -- gets current exchange rate for bitcoins from mtgox"
    data = http.get_json("https://data.mtgox.com//api//2//BTCUSD//money//ticker")
    ticker = data['data']
    t = {
      'low':  float(ticker['low']['value']),
      'high': float(ticker['high']['value']),
      'avg':  float(ticker['last']['value']),
      'vol':  float(ticker['vol']['value'])
    }
    say("Current: \x0307$%(avg).2f\x0f - High: \x0307$%(high).2f\x0f"
        " - Low: \x0307$%(low).2f\x0f - Volume: %(vol)s" % t)

'''
Created on 13 Nov 2014

@author: mariaz
'''

import json
import string
import telnetlib

class BCX():
    
    def __init__(self, af):
        self.af = af
        
    def run(self):
        
        tn = telnetlib.Telnet("api.bitcoincharts.com", 27007)
        
        while 1:
            s = tn.read_until("\n")
            d = json.loads(s)
            xid = d[u'id']
            vol = d[u'volume']
            symbol = d[u'symbol']
            currency = ''.join([c for c in symbol if c in string.uppercase])
            exchange = ''.join([c for c in symbol if c in string.lowercase])
            price = d[u'price']
            
#             print "BTC", s.strip(), d
#             print xid, vol, price, currency, exchange
            self.af.updateBC(currency, price, exchange)


if __name__ == '__main__':
    BCX().run()

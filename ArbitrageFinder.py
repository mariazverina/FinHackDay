'''
Created on 13 Nov 2014

@author: mariaz
'''

import main

import threading
from _collections import defaultdict

class ArbitrageFinder(object):
    @staticmethod
    def instance():
        return _instance

    def __init__(self):
#         self.lock = threading.Lock()
        self.bcRates = {}
        self.fxData = defaultdict(dict)
        pass

    def updateFX(self, fx_data):
        self.fxData.update(fx_data)
        print "updated FX_data to", len(self.fxData)
    
    def updateBC(self, fromCurrency, price, exchange):
        print "FX_data_len", len(self.fxData)
        print "AF::updateBC"
        self.bcRates[fromCurrency] = price
        
        if not self.fxData:
            print "no fx data"
            return 
        
        for targetCurrency in self.bcRates:
            if targetCurrency == fromCurrency:
                continue
            try:
                leg1 = self.bcRates[fromCurrency]
                leg2 = self.bcRates[targetCurrency]
                leg3 = self.fxData[fromCurrency][targetCurrency]
                product = leg1 / leg2 * leg3
                print leg1, leg2, leg3, product
                
                if abs(1-product) > 0.01:
                    print "Arbitrage??: ", fromCurrency, targetCurrency, exchange
            except(KeyError):
                pass
            
    
_instance = ArbitrageFinder()
#     
# if __name__ == '__main__':
#     main.runMain()

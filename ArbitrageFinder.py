'''
Created on 13 Nov 2014

@author: mariaz
'''

import main

import threading

class ArbitrageFinder(object):
    @staticmethod
    def instance():
        return _instance

    def __init__(self):
#         self.lock = threading.Lock()
        self.bcRates ={}
        pass

    def updateFX(self, fx_data):
        print "AF::updateFX"
        self.fxData = fx_data
    
    def updateBC(self, currency, price):
#         print "AF::updateBC"
        self.bcRates[currency] = price
        
        for curr in self.bcRates:
            if curr == currency:
                continue
            
    
_instance = ArbitrageFinder()
#     
# if __name__ == '__main__':
#     main.runMain()

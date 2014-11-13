'''
Created on 13 Nov 2014

@author: mariaz


'''

import BitCoinExchange as BCX
import FXRBSFeed as FX
import TwitterData as TW
import ArbitrageFinder as AF
from threading import Thread


if __name__ == '__main__':
#     tp = Process(target=TW.runTW)
#     tp.start()
    af = AF.ArbitrageFinder()
    fx = FX.FXFeed(af)
    bcx = BCX.BCX(af)
    bp = Thread(target=bcx.run)
    bp.start()
    fxp = Thread(target=fx.run)
    fxp.start()
    fxp.join()

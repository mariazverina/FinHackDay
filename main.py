'''
Created on 13 Nov 2014

@author: mariaz
'''

import BitCoinExchange as BCX
import FXRBSFeed as FX
import TwitterData as TW
from multiprocessing import Process


if __name__ == '__main__':
#     fx = Process(target=FX.runFX())
#     fx.start()
    tp = Process(target=TW.runTW)
    tp.start()
    bp = Process(target=BCX.runBCX())
    bp.start()
    tp.join()
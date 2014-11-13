'''
Created on 13 Nov 2014

@author: mariaz
'''
import unittest
from collections import defaultdict

def parse(data, direction):
    if direction in ['buy', 'sell']:
        return parseSimple(data, direction)
    
    if direction != "mid":
        raise ValueError("only direction available are buy/sell/mid")
    
    fxBuyTable = parse(data, "buy")
    fxSellTable = parse(data, "sell")
    
    for src, targets in fxSellTable.items():
        for dst in targets:
            fxBuyTable[src][dst] = (fxBuyTable[src][dst] + fxSellTable[src][dst]) / 2.0
            fxBuyTable[dst][src] = 1.0 / fxBuyTable[src][dst]
    return fxBuyTable

def parseSimple(data, direction):
    d = data['fx']
    result = defaultdict(dict) #lambda:defaultdict(int))
    for pair, rates in d.items():
        for rate, value in rates.items():
            if direction == rate:
                (src, dest) = pair.split('/')
                result[src][dest] = value 
    return result
    

class Test(unittest.TestCase):


    def testFrameParsing(self):
        data = {u'fx': {u'EUR/CAD': {u'sell': 1.4363, u'buy': 1.3932}, u'GBP/BRL': {u'sell': 4.0301, u'buy': 3.9064}, u'GBP/CAD': {u'sell': 1.8122, u'buy': 1.7577}, u'INR/JPY': {u'sell': 1.9131, u'buy': 1.8548}, u'USD/CAD': {u'sell': 1.1518, u'buy': 1.1172}, u'USD/JPY': {u'sell': 117.56, u'buy': 114.04}, u'USD/INR': {u'sell': 62.395, u'buy': 60.531}, u'HKD/RUB': {u'sell': 6.0994, u'buy': 5.9126}, u'CAD/CNY': {u'sell': 5.5083, u'buy': 5.3445}, u'GBP/HKD': {u'sell': 12.418, u'buy': 12.045}, u'HKD/JPY': {u'sell': 15.158, u'buy': 14.704}, u'USD/RUB': {u'sell': 47.261, u'buy': 45.821}, u'CNY/RUB': {u'sell': 7.6559, u'buy': 7.3843}, u'EUR/HKD': {u'sell': 9.8189, u'buy': 9.525}, u'GBP/JPY': {u'sell': 184.94, u'buy': 179.41}, u'CAD/INR': {u'sell': 55.023, u'buy': 53.355}, u'GBP/RUB': {u'sell': 74.426, u'buy': 72.14}, u'EUR/BRL': {u'sell': 3.1488, u'buy': 3.052}, u'USD/CNY': {u'sell': 6.2496, u'buy': 6.0633}, u'EUR/RUB': {u'sell': 58.953, u'buy': 57.134}, u'USD/BRL': {u'sell': 2.5984, u'buy': 2.5198}, u'CNY/INR': {u'sell': 10.166, u'buy': 9.8613}, u'CAD/JPY': {u'sell': 103.65, u'buy': 100.51}, u'EUR/USD': {u'sell': 1.266, u'buy': 1.2281}, u'BRL/HKD': {u'sell': 3.1557, u'buy': 3.0586}, u'RUB/INR': {u'sell': 1.3405, u'buy': 1.2993}, u'BRL/JPY': {u'sell': 46.699, u'buy': 45.263}, u'BRL/CNY': {u'sell': 2.4415, u'buy': 2.3675}, u'GBP/EUR': {u'sell': 1.2809, u'buy': 1.2427}, u'GBP/USD': {u'sell': 1.5972, u'buy': 1.5495}, u'BRL/RUB': {u'sell': 18.539, u'buy': 17.963}, u'USD/HKD': {u'sell': 7.8737, u'buy': 7.6398}, u'BRL/INR': {u'sell': 24.492, u'buy': 23.74}, u'EUR/CNY': {u'sell': 7.7911, u'buy': 7.5595}, u'GBP/CNY': {u'sell': 9.837, u'buy': 9.5378}, u'CAD/HKD': {u'sell': 6.9409, u'buy': 6.7341}, u'EUR/INR': {u'sell': 77.791, u'buy': 75.468}, u'CAD/BRL': {u'sell': 2.2233, u'buy': 2.1553}, u'CNY/JPY': {u'sell': 19.099, u'buy': 18.519}, u'RUB/JPY': {u'sell': 2.5253, u'buy': 2.4475}, u'CAD/RUB': {u'sell': 41.674, u'buy': 40.386}, u'HKD/INR': {u'sell': 8.046, u'buy': 7.8046}, u'CNY/HKD': {u'sell': 1.2792, u'buy': 1.241}, u'GBP/INR': {u'sell': 98.18, u'buy': 95.223}, u'EUR/JPY': {u'sell': 101.11, u'buy': 98.091}}, u'expiryDateTime': u'2014-11-13T21:05:46.000Z'}
        fxBuyTable = parse(data, "buy")
        print fxBuyTable
        self.assertAlmostEqual(fxBuyTable["EUR"]["CAD"], 1.3932, 8)

    def testMidRate(self):
        data = {u'fx': {u'EUR/CAD': {u'sell': 1.4363, u'buy': 1.3932}, u'GBP/BRL': {u'sell': 4.0301, u'buy': 3.9064}, u'GBP/CAD': {u'sell': 1.8122, u'buy': 1.7577}, u'INR/JPY': {u'sell': 1.9131, u'buy': 1.8548}, u'USD/CAD': {u'sell': 1.1518, u'buy': 1.1172}, u'USD/JPY': {u'sell': 117.56, u'buy': 114.04}, u'USD/INR': {u'sell': 62.395, u'buy': 60.531}, u'HKD/RUB': {u'sell': 6.0994, u'buy': 5.9126}, u'CAD/CNY': {u'sell': 5.5083, u'buy': 5.3445}, u'GBP/HKD': {u'sell': 12.418, u'buy': 12.045}, u'HKD/JPY': {u'sell': 15.158, u'buy': 14.704}, u'USD/RUB': {u'sell': 47.261, u'buy': 45.821}, u'CNY/RUB': {u'sell': 7.6559, u'buy': 7.3843}, u'EUR/HKD': {u'sell': 9.8189, u'buy': 9.525}, u'GBP/JPY': {u'sell': 184.94, u'buy': 179.41}, u'CAD/INR': {u'sell': 55.023, u'buy': 53.355}, u'GBP/RUB': {u'sell': 74.426, u'buy': 72.14}, u'EUR/BRL': {u'sell': 3.1488, u'buy': 3.052}, u'USD/CNY': {u'sell': 6.2496, u'buy': 6.0633}, u'EUR/RUB': {u'sell': 58.953, u'buy': 57.134}, u'USD/BRL': {u'sell': 2.5984, u'buy': 2.5198}, u'CNY/INR': {u'sell': 10.166, u'buy': 9.8613}, u'CAD/JPY': {u'sell': 103.65, u'buy': 100.51}, u'EUR/USD': {u'sell': 1.266, u'buy': 1.2281}, u'BRL/HKD': {u'sell': 3.1557, u'buy': 3.0586}, u'RUB/INR': {u'sell': 1.3405, u'buy': 1.2993}, u'BRL/JPY': {u'sell': 46.699, u'buy': 45.263}, u'BRL/CNY': {u'sell': 2.4415, u'buy': 2.3675}, u'GBP/EUR': {u'sell': 1.2809, u'buy': 1.2427}, u'GBP/USD': {u'sell': 1.5972, u'buy': 1.5495}, u'BRL/RUB': {u'sell': 18.539, u'buy': 17.963}, u'USD/HKD': {u'sell': 7.8737, u'buy': 7.6398}, u'BRL/INR': {u'sell': 24.492, u'buy': 23.74}, u'EUR/CNY': {u'sell': 7.7911, u'buy': 7.5595}, u'GBP/CNY': {u'sell': 9.837, u'buy': 9.5378}, u'CAD/HKD': {u'sell': 6.9409, u'buy': 6.7341}, u'EUR/INR': {u'sell': 77.791, u'buy': 75.468}, u'CAD/BRL': {u'sell': 2.2233, u'buy': 2.1553}, u'CNY/JPY': {u'sell': 19.099, u'buy': 18.519}, u'RUB/JPY': {u'sell': 2.5253, u'buy': 2.4475}, u'CAD/RUB': {u'sell': 41.674, u'buy': 40.386}, u'HKD/INR': {u'sell': 8.046, u'buy': 7.8046}, u'CNY/HKD': {u'sell': 1.2792, u'buy': 1.241}, u'GBP/INR': {u'sell': 98.18, u'buy': 95.223}, u'EUR/JPY': {u'sell': 101.11, u'buy': 98.091}}, u'expiryDateTime': u'2014-11-13T21:05:46.000Z'}
        fxMidTable = parse(data, "mid")
        print fxMidTable
        self.assertAlmostEqual(fxMidTable["EUR"]["CAD"], 1.41475, 8)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
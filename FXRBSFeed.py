#!/usr/bin/env python

import sys
import time
import pusherclient
import json
import FXParse
import ArbitrageFinder as af

global pusher

def print_usage(filename):
    print("Usage: python %s <appkey>" % filename)

def channel_callback(data):
    print "callback"
    raw_dict = json.loads(data)
    fx_block = FXParse.parse(raw_dict, "mid")
#     af = af.ArbitrageFinder.instance()
#     af.updateFX(fx_block)
    print "FX: ", fx_block

def connect_handler(data):
    channel = pusher.subscribe("fxRateStream")
    channel.bind('fxEvent', channel_callback)

def runFX():
    pusher.connection.bind('pusher:connection_established', connect_handler)
    pusher.connect()
    
    while True:
        time.sleep(1)

appkey = 'ec68fe8cadf14e52b659'
pusher = pusherclient.Pusher(appkey)

if __name__ == '__main__':
    runFX()





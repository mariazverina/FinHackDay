#!/usr/bin/env python

import sys
import time
import pusherclient
import json

global pusher

def print_usage(filename):
    print("Usage: python %s <appkey>" % filename)

def channel_callback(data):
    d = json.loads(data)
    print "Channel Callback: %s" % data
    print "FX: ", d

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





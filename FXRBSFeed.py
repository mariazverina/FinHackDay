#!/usr/bin/env python

import sys
import time
import pusherclient
import json
import FXParse

# global pusher

class FXFeed():
    def __init__(self, af):
        self.af = af
        
    def channel_callback(self, data):
        print "callback"
        raw_dict = json.loads(data)
        fx_block = FXParse.parse(raw_dict, "mid")
        self.af.updateFX(fx_block)
        print "FX: ", fx_block
    
    def connect_handler(self, data):
        channel = pusher.subscribe("fxRateStream")
        channel.bind('fxEvent', self.channel_callback)
    
    def run(self):
        pusher.connection.bind('pusher:connection_established', self.connect_handler)
        pusher.connect()
        
        while True:
            time.sleep(1)

appkey = 'ec68fe8cadf14e52b659'
pusher = pusherclient.Pusher(appkey)

if __name__ == '__main__':
    FXFeed(None).run()





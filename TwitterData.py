'''
Created on 13 Nov 2014

@author: mariaz
'''

import sys
import tweepy

def runTW():
    consumer_key="nrnMpQy1ggTVlkiN01ArAN73T"
    consumer_secret="EaYgvEMfSNIFgbkID6B8reVob0XDn0F8kWrqGzHa01uYXB5iWb"
    access_key = "31118185-Mc7FU5KLvatCVvgFZTB7WxrYPg1vHA47vnz4L1LIg"
    access_secret = "rImwmxUEBQRNre2PN5BPegpfzK4WitnXxoN4qu5Tgw4a7" 
    
    
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    
    class CustomStreamListener(tweepy.StreamListener):
        def on_status(self, status):
            print "TW", status.text
    
        def on_error(self, status_code):
            print >> sys.stderr, 'Encountered error with status code:', status_code
            return True # Don't kill the stream
    
        def on_timeout(self):
            print >> sys.stderr, 'Timeout...'
            return True # Don't kill the stream
    
    sapi = tweepy.streaming.Stream(auth, CustomStreamListener())
    sapi.filter(track=['bitcoin'])

if __name__ == '__main__':
    runTW()

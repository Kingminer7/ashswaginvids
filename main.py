import tweepy
import os
import re

alphaLower = "abcdefghijklmnopqrstuvwxyz"
alphaUpper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def cipher(str):
  str = re.sub(r"(?:\@|https?\://)\S+", "", str)
  new = ""
  for val in [*str]:
    print(val)
    changed = False
    for x in range(25):
      if changed == False:
        if([*alphaLower][x] == val):
          n = x + 13
          if n > 25:
            n -= 26
          new += [*alphaLower][n]
          changed = True
      if changed == False:
        if([*alphaUpper][x] == val):
          n = x + 13
          if n > 25:
            n -= 26
          new += [*alphaUpper][n]
          changed = True
    if changed == False:
      new += val
  return new

consumer_key = os.environ['consumer_key']
consumer_secret = os.environ['consumer_secret']
access_token = os.environ['access_token']
access_token_secret = os.environ['access_token_secret']
bearer_token = os.environ['bearer_token']


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)

class TStream(tweepy.StreamingClient):
    # This function gets called when the stream is working
    def on_connect(self):
        print("Connected")

    def on_tweet(self, tweet):
       print(tweet.data) 
       api.update_status(status=cipher(tweet.text), in_reply_to_status_id=tweet.id, auto_populate_reply_metadata=True)
       return

stream = TStream(bearer_token)
stream.filter() #runs the stream
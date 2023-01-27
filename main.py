<<<<<<< HEAD
import json
  
# Opening JSON file
f = open('config.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)
=======
>>>>>>> f3f629b6a693d4288c979ce260761832442a9036

<<<<<<< HEAD
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

consumer_key = data['consumer_key']
consumer_secret = data['consumer_secret']
access_token = data['access_token']
access_token_secret = data['access_token_secret']
bearer_token = data['bearer_token']


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)

class TStream(tweepy.StreamingClient):
    # This function gets called when the stream is working
    def on_connect(self):
        print("Connected to Twitter.")

    def on_tweet(self, tweet):
       api.update_status(status=cipher(tweet.text), in_reply_to_status_id=tweet.id, auto_populate_reply_metadata=True)
       return

stream = TStream(bearer_token)
stream.add_rules(tweepy.StreamRule("from:ashswagin OR from:altswag OR from:km7devalt"))
stream.filter() #runs the stream
=======
app = Flask('')

@app.route('/')
def main():
  return "Your Bot Is Ready"

def run():
  app.run(host="0.0.0.0", port=8000)

def keep_alive():
  server = Thread(target=run)
  server.start()

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
stream.add_rules(tweepy.StreamRule("from:ashswagin OR from:altswag"))
stream.filter() #runs the stream
>>>>>>> f3f629b6a693d4288c979ce260761832442a9036
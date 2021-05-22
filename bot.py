import tweepy
import random
import time
from quoteList import edgeworthQuotes

consumer_key = 'CONSUMER KEY'
consumer_secret = 'CONSUMER SECRET'

key = 'KEY'
secret = 'SECRET'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)

while True:
    # Main Loop - tweeting indefinitely
    api.update_status(random.choice(edgeworthQuotes))
    time.sleep(random.randint(7200, 21600))

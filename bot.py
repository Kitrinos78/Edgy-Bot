import tweepy
import random
import time
from quoteList import edgeworthQuotes
from auth import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)

while True:
    # Main Loop - tweeting indefinitely
    api.update_status(random.choice(edgeworthQuotes))
    time.sleep(random.randint(7200, 21600))

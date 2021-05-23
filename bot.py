import tweepy
import random
import time
from quoteList import edgeworthQuotes
from auth import *

# Tweepy Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)

while True:
    # Main Loop - tweeting indefinitely
    api.update_status(random.choice(edgeworthQuotes))  # Update Twitter status
    time.sleep(random.randint(7200, 21600))  # Sleep randomly for 2-6 hours

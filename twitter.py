# twitter.py
# Authors: Joel Peckham, Andrew Hansbury, Marc Guarino
# Date: 1/19/2022

# This is a class which wrapps the twitter API for our project.
# It has one publicly facing method to post a tweet.

import json, tweepy
from time import strftime
from datetime import datetime as dt
from dateutil import tz

class Twitter:
    def __init__(self, keyFile = "twitterKeys.json"):
        with open(keyFile) as f:
            keys = json.load(f)
        self.auth = tweepy.OAuthHandler(keys["consumer_key"], keys["consumer_secret"])
        self.auth.set_access_token(keys["access_token"], keys["access_token_secret"])
        self.api = tweepy.API(self.auth)
        
    def post(self, location, date):
        dateObj = dt.fromtimestamp(date)
        from_zone = tz.gettz('UTC')
        to_zone = tz.gettz('America/New_York')
        dateObj = dateObj.replace(tzinfo=from_zone)
        east = dateObj.astimezone(to_zone)

        locationName = location["title"]
        lat,lon = location["latitude"], location["longitude"]
        link = f'https://www.google.com/maps/search/?api=1&query={float(lat)},{float(lon)}'
        tweet = f"The {locationName} crossing became blocked at {strftime(east.strftime('%I:%M %p'))} on {east.strftime('%m/%d/%Y')}.\n{link}"
        self.api.update_status(tweet)

if __name__ == "__main__":
    twitter = Twitter()
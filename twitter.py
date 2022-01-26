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
        self.consumer_key = keys["consumer_key"]
        self.consumer_secret = keys["consumer_secret"]
        self.access_token = keys["access_token"]
        self.access_token_secret = keys["access_token_secret"]
        self.auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        self.auth.set_access_token(self.access_token, self.access_token_secret)
        self.api = tweepy.API(self.auth)
        
    def post(self, location, date):
        dateObj = dt(date['year'], date['month'], date['day'], date['hour'], date['minute'])
        from_zone = tz.gettz('UTC')
        to_zone = tz.gettz('America/New_York')
        dateObj = dateObj.replace(tzinfo=from_zone)
        east = dateObj.astimezone(to_zone)

        locationName = location["id"]
        lat,lon = location["latitude"], location["longitude"]
        link = f'https://www.google.com/maps/search/?api=1&query={float(lat)},{float(lon)}'
        tweet = f"Station {locationName} became blocked at {strftime(east.strftime('%I:%M %p'))} on {east.strftime('%m/%d/%Y')}.\n{link}"
        self.api.update_status(tweet)

if __name__ == "__main__":
    twitter = Twitter()
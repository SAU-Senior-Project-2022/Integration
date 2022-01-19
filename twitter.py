# twitter.py
# Authors: Joel Peckham, Andrew Hansbury, Marc Guarino
# Date: 1/19/2022

# This is a class which wrapps the twitter API for our project.
# It has one publicly facing method to post a tweet.

import json, tweepy
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
        
    def post(self, trainData):
        locationName = trainData["locationName"]
        lat,lon = trainData["lat"], trainData["lon"]
        link = f'https://www.google.com/maps/search/?api=1&query={float(lat)},{float(lon)}'
        tweet = f"{locationName} is at {lat},{lon} {link}"
        self.api.update_status(tweet)

if __name__ == "__main__":
    twitter = Twitter()
    twitter.post({"locationName": "Test Location", "lat": "35.0504969", "lon": "-85.0809819"})
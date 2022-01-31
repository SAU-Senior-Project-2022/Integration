# Integration
Twitter Integration for Train App. 

# Requirements
- Post a tweet within 60 seconds of a new blockage being reported to the database.
- Tweet should clearly state the location and time of detection.
- Tweet should include a link to a Google Maps pin with the coordinates of the blockage.
- Elegantly reporting clearings is out of scope for this sprint.

# Live Link
https://twitter.com/TrainCrossings

# Deployment Requirements
- Api Keys from [Twitter API](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/v2)
    - These should be placed in a file called `twitterKeys.json` alongside `main.py`
    - Example structure: `{"consumer_key" : "", "consumer_secret" : "", "access_token" : "", "access_token_secret" : ""}`
- [Tweepy Python Library](https://docs.tweepy.org/en/stable/)
- [Dateutil Python Library](https://dateutil.readthedocs.io/en/stable/)
- Add `cronjob.sh` to your crontab with * * * * * to run every minute.
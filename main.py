# main.py
# Authors: Joel Peckham, Andrew Hansbury, Marc Guarino
# Date: 1/19/2022

from twitter import Twitter
import json, requests

# This script will be run every 30 seconds by a cron job.
# It will post a tweet if a train is currently blocking a road.


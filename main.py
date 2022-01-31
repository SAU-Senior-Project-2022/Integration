# main.py
# Authors: Joel Peckham, Andrew Hansbury, Marc Guarino
# Date: 1/19/2022

from twitter import Twitter
from trainAPI import TrainAPI
import os, json

# This script will be run every 30 seconds by a cron job.
# It will post a tweet if a train is currently blocking a road.

api = TrainAPI()
twitter = Twitter()

stationIds = api.getLocationIds()
stationStates = [api.getState(i) for i in stationIds]

# If the stateHistory.json file doesn't exist, create it.
if not os.path.exists("stateHistory.json"):
    with open("stateHistory.json", "w") as f:
        f.write("{}")

# Get state history from file.
with open("stateHistory.json", 'r') as f:
    stateHistory = dict(json.load(f))

#Iterate through each station.
for station in stationStates:
    #If we haven't seen this station, we'll add it to our history file and ignore it.
    station_id = str(station["station_id"])
    if station_id not in stateHistory:
        stateHistory.update({station_id: str(station["state"])})
    #Otherwise, we'll check if the state has changed.
    else:
        # If the state has changed to "blocked", post a tweet.
        if int(station["state"]) > int(stateHistory[station_id]):
            location = api.getLocation(station_id)
            twitter.post(location, station['date'])
            print(f"Posted tweet for station {station_id}")
        stateHistory.update({station_id: str(station["state"])})

print(stateHistory)
with open("stateHistory.json", "w") as f:
    json.dump(stateHistory, f)
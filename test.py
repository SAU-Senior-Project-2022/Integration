import requests, json

res = requests.post("http://train.jpeckham.com:5000/state/4", json = {"state": True})
print(res.text)
import requests, json

res = requests.post("http://train.jpeckham.com:5000/state/1", json = {"state": True})
print(res.text)
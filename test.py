import requests, json

res = requests.post("http://localhost:5000/state/1", json = {"state": True})
print(res.text)
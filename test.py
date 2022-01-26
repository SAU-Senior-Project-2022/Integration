import requests, json

res = requests.post("http://train.jpeckham.com:5000/state/3", json = {"state": False})
print(res.text)
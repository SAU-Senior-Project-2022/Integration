import requests, json

class TrainAPI:
    def __init__(self,baseURL = "http://train.jpeckham.com:5000"):
        self.baseURL = baseURL

    def _get(self, endpoint):
        url = self.baseURL + endpoint
        response = requests.get(url)
        # print(response.text)
        return response.json()
    
    def getLocationIds(self):
        return [i['id'] for i in self._get("/location")]

    def getLocation(self, locationId):
        return self._get(f"/location/{locationId}")
    
    def getState(self, locationId):
        return self._get(f"/state/{locationId}")
    
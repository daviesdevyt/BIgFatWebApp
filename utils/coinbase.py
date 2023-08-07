import requests, json

class Coinbase():
    headers = {"X-CC-Version": "2018-03-22"}

    BASE_URL = "https://api.commerce.coinbase.com"

    def __init__(self, api_key) -> None:
        self.headers["X-CC-Api-Key"] = api_key

    def create_charge(self, **kwargs):
        res = requests.post(self.BASE_URL+"/charges", json=kwargs, headers=self.headers)
        return json.loads(res.content)
    
    def get_charge(self, charge_id_or_code):
        res = requests.get(self.BASE_URL+"/charges/"+charge_id_or_code, headers=self.headers)
        return json.loads(res.content)

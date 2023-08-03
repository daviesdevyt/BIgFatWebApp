import requests
from django.conf import settings

class Oxapay:
    base_url = "https://api.oxapay.com"

    def __init__(self, merchant=None):
        if not merchant:
            merchant = settings.OXAPAY_MERCHANT
        self.merchant = merchant

    def make_request(self, *, method="get", endpoint, data=None):
        # Make request to Oxapay
        method = method.upper()
        methods = {"GET": requests.get, "POST": requests.post}
        if data:
            data["merchant"] = self.merchant
        response = methods[method](self.base_url + endpoint, data=data)

        response = response.json()
        if response.get("result") in [100, 202, 201, 203]:
            return response

        else:
            raise Exception(response.get("message"))

    def payment_request(self, amount, webhook_url, **kwargs):
        return self.make_request(method="post", endpoint="/merchants/request", data={
            "amount": amount,
            "callbackUrl": webhook_url,
            **kwargs
        })

    def get_transaction(self, track_id):
        return self.make_request(method="post", endpoint="/merchants/inquiry", data={"trackId": track_id})

    def verify_transaction(self, track_id):
        return self.make_request(method="post", endpoint="/merchants/verify", data={"trackId": track_id})

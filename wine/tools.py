import requests

SCANDIT_URL = "https://api.scandit.com/v2/products/"
API_KEY = "QMXnoEqepvSpQe0cRC--7PUBKocQQmMoN29FxKYMO96"

def _make_scandit_url(barcode):
    return "%s/%s?key=%s" % (SCANDIT_URL, barcode, API_KEY)

def query_scandit_api(barcode):
    url = _make_scandit_url(barcode)
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None
